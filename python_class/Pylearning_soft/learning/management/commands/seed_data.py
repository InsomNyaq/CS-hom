from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from learning.models import Lesson, QuizQuestion


LESSONS = [
    {
        "title": "认识 Python 与开发环境",
        "slug": "python-start",
        "summary": "了解 Python 的特点、解释器与第一个可运行程序。",
        "level": "入门",
        "duration": 18,
        "order": 1,
        "content": "Python 是一种易读、用途广泛的编程语言。开发时通常会经历编写代码、运行程序、观察输出这三个步骤。先从 print 开始，让计算机向我们反馈信息。",
        "code": 'name = "InsomNya"\nprint(f"你好，{name}！")',
        "output": "你好，InsomNya！",
        "questions": [
            {
                "question": "下面哪个函数可以把内容输出到控制台？",
                "options": {"A": "input()", "B": "print()", "C": "show()", "D": "write()"},
                "answer": "B",
                "explanation": "print() 用于向标准输出打印内容。",
            }
        ],
    },
    {
        "title": "变量、数据类型与输入",
        "slug": "variables-types",
        "summary": "掌握变量赋值、字符串、数字和从用户获取信息。",
        "level": "入门",
        "duration": 25,
        "order": 2,
        "content": "变量是给数据起的名字。Python 会根据赋值内容自动推断类型，常见类型包括 str、int、float 和 bool。input() 获取到的内容默认是字符串。",
        "code": 'age_text = input("请输入年龄：")\nage = int(age_text)\nprint(age + 1)',
        "output": "输入 18 后输出 19",
        "questions": [
            {
                "question": "input() 返回的数据类型默认是？",
                "options": {"A": "str", "B": "int", "C": "bool", "D": "list"},
                "answer": "A",
                "explanation": "input() 接收到的用户输入始终以字符串形式返回。",
            }
        ],
    },
    {
        "title": "条件判断与逻辑表达式",
        "slug": "conditions",
        "summary": "使用 if、elif、else 让程序根据不同情况做决定。",
        "level": "基础",
        "duration": 28,
        "order": 3,
        "content": "条件语句是程序决策的基础。使用比较运算符得到 True 或 False，再通过 if、elif、else 组织不同分支。",
        "code": 'score = 86\nif score >= 60:\n    print("通过")\nelse:\n    print("继续努力")',
        "output": "通过",
        "questions": [
            {
                "question": "条件表达式 score >= 60 的结果是什么？",
                "options": {"A": "字符串", "B": "整数", "C": "布尔值", "D": "列表"},
                "answer": "C",
                "explanation": "比较表达式的结果是 True 或 False，也就是布尔值。",
            }
        ],
    },
    {
        "title": "循环与列表处理",
        "slug": "loops-lists",
        "summary": "用列表保存多个数据，再用 for 循环批量处理它们。",
        "level": "基础",
        "duration": 32,
        "order": 4,
        "content": "列表可以按顺序保存多个值。for 循环会依次取出列表中的元素，适合处理重复任务。range() 可以生成一组连续数字。",
        "code": 'topics = ["变量", "判断", "循环"]\nfor index, topic in enumerate(topics, 1):\n    print(index, topic)',
        "output": "1 变量\\n2 判断\\n3 循环",
        "questions": [
            {
                "question": "for 循环最适合用来做什么？",
                "options": {"A": "重复处理一组数据", "B": "关闭程序", "C": "创建窗口", "D": "安装 Python"},
                "answer": "A",
                "explanation": "for 适合遍历可迭代对象并重复执行代码块。",
            }
        ],
    },
    {
        "title": "函数与模块化思维",
        "slug": "functions",
        "summary": "把可复用逻辑封装成函数，让代码更清晰、更容易维护。",
        "level": "进阶",
        "duration": 35,
        "order": 5,
        "content": "函数通过 def 定义，可以接收参数并返回结果。把大问题拆成多个小函数，是从会写代码走向会设计代码的重要一步。",
        "code": 'def welcome(name):\n    return f"欢迎你，{name}！"\n\nmessage = welcome("Python 学习者")\nprint(message)',
        "output": "欢迎你，Python 学习者！",
        "questions": [
            {
                "question": "函数使用哪个关键字定义？",
                "options": {"A": "func", "B": "define", "C": "def", "D": "function"},
                "answer": "C",
                "explanation": "Python 使用 def 关键字定义函数。",
            }
        ],
    },
]


class Command(BaseCommand):
    help = "创建示例账号、课程和测验数据"

    def handle(self, *args, **options):
        User = get_user_model()
        user, created = User.objects.get_or_create(username="InsomNya")
        user.set_password("9019zhyq")
        user.is_staff = True
        user.is_superuser = True
        user.save()

        for source in LESSONS:
            item = {key: value for key, value in source.items() if key != "questions"}
            questions = source["questions"]
            lesson, _ = Lesson.objects.update_or_create(
                slug=item["slug"], defaults=item
            )
            for question in questions:
                QuizQuestion.objects.update_or_create(
                    lesson=lesson,
                    order=1,
                    defaults=question,
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"初始化完成：账号 InsomNya，课程 {Lesson.objects.count()} 门。"
            )
        )
