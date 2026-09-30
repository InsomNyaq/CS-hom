from process import *
import ast
import json

def main():

    students = []
    sorted_students = []
    grade_student = {}
    count=()

    with open("student.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line:
                student = ast.literal_eval(line)
                students.append(student)

    print("请选择你想要进行的操作并输入对应的序号：\n")
    print_choice()
    user_choice = input()
    choice = ['1','2','3','4','5','6','q']
    if user_choice not in choice:
        print("输入的序号不正确，请重新输入")
        return
    
    while(user_choice != 'q'):
        if user_choice == '1':
            students = student_entry(students)
        elif user_choice == '2':
            search(students)
        elif user_choice == '3':
            scores_static(students)
        elif user_choice == '4':
            sorted_students = student_sorted(students, reverse=True)
            with open("sorted_students.json", "w", encoding="utf-8") as f:
                json.dump(sorted_students, f, ensure_ascii=False, indent = 4)
                print("排序后的列表已存储到sorted_students.json文件\n")
        elif user_choice == '5':
            fail_warning(students)
        elif user_choice == '6':
            grade_student, count = grade_classification(students)
            print("请选择你想要进行的操作并输入对应的序号：\n")
            print_choice()
            user_choice = input()
            choice = ['1','2','3','4','5','6','q']
            if user_choice not in choice:
                print("输入的序号不正确，请重新输入")
                return




if __name__ == "__main__":
        main()