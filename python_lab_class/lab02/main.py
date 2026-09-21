from process import *
import ast

def main():

    students = []

    with open("student.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line:
                student = ast.literal_eval(line)
                students.append(student)

    print("请选择你想要进行的操作并输入对应的序号：\n")
    print_choice()
    user_choice = input()
    while(user_choice != 'q'):
        if user_choice == ''





if __name__ == "__main__":
        main()