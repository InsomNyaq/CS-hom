from django.urls import path

from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("lessons/", views.lesson_list, name="lesson_list"),
    path("lessons/<slug:slug>/", views.lesson_detail, name="lesson_detail"),
    path("lessons/<slug:slug>/complete/", views.complete_lesson, name="complete_lesson"),
    path("quiz/", views.quiz, name="quiz"),
]
