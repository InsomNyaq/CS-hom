import ast
import json
from pathlib import Path

from process import (
    fail_warning,
    grade_classification,
    print_choice,
    scores_static,
    search,
    student_entry,
    student_sorted,
)


def load_students(file_path):
    """Read one literal student record per line from a text file."""
    students = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                students.append(ast.literal_eval(line))
    return students


def main():
    data_file = Path(__file__).with_name("student.txt")
    students = load_students(data_file)
    print(f"已读取 {len(students)} 名学生的信息")

    while True:
        print_choice()
        user_choice = input("请输入选项: ").strip().lower()

        if user_choice == "q":
            print("程序已退出")
            break
        if user_choice == "1":
            student_entry(students)
        elif user_choice == "2":
            search(students)
        elif user_choice == "3":
            sorted_students = student_sorted(students)
            print("按总分降序排列:")
            for student in sorted_students:
                print(student)
            output_file = data_file.with_name("sorted_students.json")
            with open(output_file, "w", encoding="utf-8") as file:
                json.dump(sorted_students, file, ensure_ascii=False, indent=4)
            print(f"排序后的列表已存储到 {output_file.name}")
        elif user_choice == "4":
            scores_static(students)
        elif user_choice == "5":
            fail_warning(students)
        elif user_choice == "6":
            grade_student, count = grade_classification(students)
            print(f"等级名单: {grade_student}")
            print(f"各等级人数（A、B、C、D）: {count}")
        else:
            print("输入的序号不正确，请重新输入")


if __name__ == "__main__":
    main()
