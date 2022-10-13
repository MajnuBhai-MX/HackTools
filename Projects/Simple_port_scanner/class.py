import sys


class student:

    all_student = []

    def __init__(self, name, age, std):
        self.name = name
        self.std = std
        self.age = age
        student.all_student.append(self)

    def __str__(self):
        return f"Detail: {self.name}, {self.age}, {self.std}"


stu1 = student("Mayank", 19, "Btech")
stu2 = student("Harsh", 22, "Btech")

while True:

    try:
        print("\n")
        n, a, s = input("Enter -->  ").split(",")
        student(n, a, s)
        print("\r")
        print("\n\r----STUDENTS DETAILS-----\n\n\n")
        for detail in student.all_student:
            print(detail)
        # break
    except:
        print("QUITTING")
        sys.exit()
