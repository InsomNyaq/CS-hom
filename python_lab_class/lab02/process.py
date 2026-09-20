def student_entry(students)->list:
    id_entry = int(input("请输入要添加的学生的学号: "))

    for student in students:
        if id_entry == student["student"][0]:
            print("学号已存在，添加失败\n")
            return students 
    #stop store new student by return

    # for i in range(len(students)):
    #     if id_entry == students[i]["student"][0]:
    #         print("学号已存在，添加失败\n")

    student_name, chinese, math, english = input("请依次输入学生姓名, 语文成绩, 数学成绩, 英语成绩: (以空格分隔)\n").split()

    chinese = int(chinese)
    math = int(math)
    english = int(english)

    stu_entry = {"student":(id_entry,student_name),"scores": {"语文":chinese, "数学":math, "英语":english}}
    students.append(stu_entry)
    return students

def search(students)->list:
    '''search for student info by student id'''
    id_se = int(input("请输入需要查询的学生的学号： "))

    for student in students:
        student_id, student_name = student["student"]
        if id_se == student_id:
            print(student_name, student_id)
            scores = student["scores"]
            for key, value in scores.items():
                print(key, value)
        else:
            print("未找到该学生\n")


def student_sorted(students, reverse=True)->list:
    '''sort students by total scores and append it.'''
    new_students = []

    for student in students:
        new_student = student.copy()
        total = sum(student["scores"].values())
        new_student["total"] = total

        new_students.append(new_student)

    sorted_students = sorted(
        new_students,
        key=lambda student: student["total"],
        reverse = reverse
    )

    return sorted_students



def scores_static(students)->list:
    '''Extract the average scores of the courses 
    and output students'name of both the max and min scores in each course'''

    courses = ["语文", "数学", "英语"]
    for course in courses:
        scores = [student["scores"][course] for student in students]
        max_score = max(scores)
        min_score = min(scores)

        avg_score = sum(scores)/len(students)
        best_student = max(students, key = lambda student: student["scores"][course])
        worst_student = min(students, key = lambda student: student["scores"][course])

        print(f"\n{course} 平均分：{avg_score}\n")
        print(f"最高分: {max_score}\n"
              f"学号: {best_student["student"][0]}\n")

        print(f"最高分: {min_score}\n"
              f"学号: {worst_student["student"][0]}\n"
              f"姓名: {worst_student["scores"]["course"]}\n")

def fail_warning(students):
    '''Output students who are fail the course'''
    print("任意课程不及格学生:\n")
    courses = ["语文", "数学", "英语"]
    for course in courses:
        for student in students:
            student_score = student["scores"][course]
            if student_score < 60:
                student_id = student["student"][0]
                student_name = student["student"][1]
                print(f"课程名: {course} "
                      f"学号: {student_id}"
                      f"姓名: {student_name}"
                      f"成绩: {student_score}\n")

def grade_classification(students)->list:
    a_count, b_count, c_count, d_count = 0, 0, 0, 0
    courses = ["语文", "数学", "英语"]
    grade_student = {
        "A":[],
        "B":[],
        "C":[],
        "D":[]
    }

    choice = input("输入你想按照哪门课程给学生排序(语文,数学,英语): ")
    if choice not in courses:
        print("输入的课程不在选择之中")
        return
    
    for student in students:
        student_score = student["scores"][choice]
        student_name  = student["student"][1]

        if student_score >= 90:
            grade_student["A"].append(student_name)
            a_count +=1
        elif student_score >= 80:
            grade_student["B"].append(student_name)
            b_count +=1
        elif student_score >= 60:
            grade_student["C"].append(student_name)
            c_count +=1
        else:
            grade_student["D"].append(student_name)
            d_count +=1

    count = (a_count,b_count,c_count,d_count)
    return grade_student, count