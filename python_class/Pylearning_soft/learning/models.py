from django.conf import settings
from django.db import models


class Lesson(models.Model):
    LEVELS = [
        ("入门", "入门"),
        ("基础", "基础"),
        ("进阶", "进阶"),
    ]

    title = models.CharField("标题", max_length=120)
    slug = models.SlugField("标识", unique=True)
    summary = models.CharField("简介", max_length=240)
    content = models.TextField("课程内容")
    code = models.TextField("代码示例", blank=True)
    output = models.CharField("运行结果", max_length=240, blank=True)
    level = models.CharField("难度", max_length=20, choices=LEVELS, default="入门")
    duration = models.PositiveIntegerField("预计分钟", default=20)
    order = models.PositiveIntegerField("排序", default=1)
    is_published = models.BooleanField("已发布", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "课程"
        verbose_name_plural = "课程"

    def __str__(self):
        return self.title


class Progress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField("已完成", default=False)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "lesson"], name="unique_user_lesson_progress"
            )
        ]
        verbose_name = "学习进度"
        verbose_name_plural = "学习进度"


class QuizQuestion(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name="questions"
    )
    question = models.CharField("题目", max_length=240)
    options = models.JSONField("选项")
    answer = models.CharField("正确答案", max_length=1)
    explanation = models.CharField("解析", max_length=300)
    order = models.PositiveIntegerField("排序", default=1)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "测验题目"
        verbose_name_plural = "测验题目"


class QuizAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.PositiveIntegerField("得分")
    total = models.PositiveIntegerField("总题数")
    created_at = models.DateTimeField("提交时间", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "测验记录"
        verbose_name_plural = "测验记录"
