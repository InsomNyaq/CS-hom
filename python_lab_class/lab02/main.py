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

    print(students)




if __name__ == "__main__":
        main()