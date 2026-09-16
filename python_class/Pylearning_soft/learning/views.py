from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Lesson, Progress, QuizAttempt, QuizQuestion


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "账号或密码不正确，请检查后重试。")
    return render(request, "login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("login")


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    lessons = list(Lesson.objects.filter(is_published=True))
    completed_ids = set(
        Progress.objects.filter(user=request.user, completed=True).values_list(
            "lesson_id", flat=True
        )
    )
    completed_count = len(completed_ids)
    total_count = len(lessons)
    percent = round(completed_count / total_count * 100) if total_count else 0
    recent = QuizAttempt.objects.filter(user=request.user)[:3]
    return render(
        request,
        "dashboard.html",
        {
            "lessons": lessons,
            "completed_ids": completed_ids,
            "completed_count": completed_count,
            "total_count": total_count,
            "percent": percent,
            "recent_attempts": recent,
            "next_lesson": next(
                (lesson for lesson in lessons if lesson.id not in completed_ids),
                lessons[0] if lessons else None,
            ),
        },
    )


@login_required
def lesson_list(request: HttpRequest) -> HttpResponse:
    level = request.GET.get("level", "")
    lessons = Lesson.objects.filter(is_published=True)
    if level:
        lessons = lessons.filter(level=level)
    completed_ids = set(
        Progress.objects.filter(user=request.user, completed=True).values_list(
            "lesson_id", flat=True
        )
    )
    return render(
        request,
        "lessons.html",
        {
            "lessons": lessons,
            "completed_ids": completed_ids,
            "active_level": level,
        },
    )


@login_required
def lesson_detail(request: HttpRequest, slug: str) -> HttpResponse:
    lesson = get_object_or_404(Lesson, slug=slug, is_published=True)
    completed = Progress.objects.filter(
        user=request.user, lesson=lesson, completed=True
    ).exists()
    return render(
        request,
        "lesson_detail.html",
        {"lesson": lesson, "completed": completed, "questions": lesson.questions.all()},
    )


@login_required
def complete_lesson(request: HttpRequest, slug: str) -> HttpResponse:
    if request.method != "POST":
        return JsonResponse({"error": "method not allowed"}, status=405)
    lesson = get_object_or_404(Lesson, slug=slug, is_published=True)
    progress, _ = Progress.objects.get_or_create(user=request.user, lesson=lesson)
    progress.completed = True
    progress.save(update_fields=["completed", "updated_at"])
    return JsonResponse({"ok": True, "message": "课程已标记为完成"})


@login_required
def quiz(request: HttpRequest) -> HttpResponse:
    questions = list(
        QuizQuestion.objects.select_related("lesson").filter(
            lesson__is_published=True
        )
    )
    if request.method == "POST":
        correct = 0
        feedback = []
        for question in questions:
            chosen = request.POST.get(f"question_{question.id}", "")
            is_correct = chosen == question.answer
            correct += int(is_correct)
            feedback.append(
                {"question": question, "chosen": chosen, "correct": is_correct}
            )
        if questions:
            QuizAttempt.objects.create(
                user=request.user, score=correct, total=len(questions)
            )
        return render(
            request,
            "quiz.html",
            {
                "questions": questions,
                "feedback": feedback,
                "score": correct,
                "submitted": True,
            },
        )
    return render(request, "quiz.html", {"questions": questions, "submitted": False})
