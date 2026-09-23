COURSES = ("语文", "数学", "英语")


def student_entry(students):
    """Interactively add one student, rejecting duplicate student IDs."""
    id_entry = int(input("请输入要添加的学生的学号: ").strip())

    if any(student["student"][0] == id_entry for student in students):
        print("学号已存在，添加失败")
        return students

    student_name, chinese, math, english = input(
        "请依次输入学生姓名、语文成绩、数学成绩、英语成绩（以空格分隔）: "
    ).split()
    stu_entry = {
        "student": (id_entry, student_name),
        "scores": {
            "语文": int(chinese),
            "数学": int(math),
            "英语": int(english),
        },
    }
    students.append(stu_entry)
    print("学生信息添加成功")
    return students


def search(students):
    """Print and return one student's information by student ID."""
    id_se = int(input("请输入需要查询的学生的学号：").strip())

    for student in students:
        student_id, student_name = student["student"]
        if id_se == student_id:
            print(f"姓名: {student_name}")
            print(f"学号: {student_id}")
            for course, score in student["scores"].items():
                print(f"{course}: {score}")
            return student

    print("未找到该学生")
    return None


def student_sorted(students, reverse=True):
    """Return a new list sorted by total score without changing students."""
    new_students = []
    for student in students:
        new_student = {
            "student": student["student"],
            "scores": dict(student["scores"]),
            "total": sum(student["scores"].values()),
        }
        new_students.append(new_student)

    return sorted(new_students, key=lambda student: student["total"], reverse=reverse)


def scores_static(students):
    """Print average, maximum and minimum information for every course."""
    if not students:
        print("暂无学生数据")
        return {}

    statistics = {}
    for course in COURSES:
        scores = [student["scores"][course] for student in students]
        best_student = max(students, key=lambda student: student["scores"][course])
        worst_student = min(students, key=lambda student: student["scores"][course])
        best_id, best_name = best_student["student"]
        worst_id, worst_name = worst_student["student"]
        max_score = max(scores)
        min_score = min(scores)
        average = sum(scores) / len(scores)

        statistics[course] = {
            "average": average,
            "max": {"score": max_score, "student_id": best_id, "name": best_name},
            "min": {"score": min_score, "student_id": worst_id, "name": worst_name},
        }
        print(f"\n{course}平均分: {average:.2f}")
        print(f"最高分: {max_score}，学号: {best_id}，姓名: {best_name}")
        print(f"最低分: {min_score}，学号: {worst_id}，姓名: {worst_name}")

    return statistics


def fail_warning(students):
    """Print and return every course score below 60."""
    warnings = []
    for student in students:
        student_id, student_name = student["student"]
        for course, score in student["scores"].items():
            if score < 60:
                warning = {
                    "course": course,
                    "student_id": student_id,
                    "name": student_name,
                    "score": score,
                }
                warnings.append(warning)

    print("任意课程不及格学生:")
    if not warnings:
        print("无不及格记录")
    for warning in warnings:
        print(
            f"课程名: {warning['course']}，学号: {warning['student_id']}，"
            f"姓名: {warning['name']}，成绩: {warning['score']}"
        )
    return warnings


def grade_classification(students, course=None):
    """Classify students by one course and return names plus count tuple."""
    if course is None:
        course = input("输入要进行等级划分的课程（语文、数学、英语）: ").strip()
    if course not in COURSES:
        print("输入的课程不在选择之中")
        return {"A": [], "B": [], "C": [], "D": []}, (0, 0, 0, 0)

    grade_student = {"A": [], "B": [], "C": [], "D": []}
    for student in students:
        score = student["scores"][course]
        name = student["student"][1]
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 60:
            grade = "C"
        else:
            grade = "D"
        grade_student[grade].append(name)

    count = tuple(len(grade_student[grade]) for grade in ("A", "B", "C", "D"))
    return grade_student, count


def print_choice():
    print("\n请选择你想要进行的操作并输入对应的序号：")
    print("1. 添加学生信息")
    print("2. 查询学生信息")
    print("3. 按总分排序输出学生信息")
    print("4. 输出各科平均分及最高分和最低分的学生信息")
    print("5. 输出任意课程不及格的学生信息")
    print("6. 按照成绩等级分类输出学生信息")
    print("q. 退出程序")
