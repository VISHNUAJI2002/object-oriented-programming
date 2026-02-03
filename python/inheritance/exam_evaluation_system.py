"""
Problem Statement:
Design a Python program to evaluate university examination results using
inheritance. Create a base class that stores common student details. Derive
a class that adds internal and external marks. Further derive different
evaluation classes for Undergraduate and Postgraduate students, where
grading rules differ. The program should accept details for multiple students
from the user and display final marks and grade using inheritance and method
overriding.
"""

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class ExamStudent(Student):
    def __init__(self, student_id, name, internal_marks, external_marks):
        super().__init__(student_id, name)
        self.internal_marks = internal_marks
        self.external_marks = external_marks

    def total_marks(self):
        return self.internal_marks + self.external_marks


class UndergraduateStudent(ExamStudent):
    def calculate_grade(self):
        total = self.total_marks()
        if total >= 80:
            return "A"
        elif total >= 60:
            return "B"
        elif total >= 50:
            return "C"
        else:
            return "Fail"


class PostgraduateStudent(ExamStudent):
    def calculate_grade(self):
        total = self.total_marks()
        if total >= 85:
            return "A"
        elif total >= 70:
            return "B"
        elif total >= 60:
            return "C"
        else:
            return "Fail"


students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i + 1}")
    course_type = input("Enter course type (ug/pg): ").lower()
    sid = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    internal = int(input("Enter internal marks: "))
    external = int(input("Enter external marks: "))

    if course_type == "ug":
        students.append(UndergraduateStudent(sid, name, internal, external))
    elif course_type == "pg":
        students.append(PostgraduateStudent(sid, name, internal, external))


print("\n--- Examination Results ---")
for student in students:
    print("\nStudent ID:", student.student_id)
    print("Name:", student.name)
    print("Total Marks:", student.total_marks())
    print("Grade:", student.calculate_grade())


"""
Sample Output:

Enter number of students: 2

Student 1
Enter course type (ug/pg): ug
Enter student ID: 101
Enter student name: Arun
Enter internal marks: 28
Enter external marks: 55

Student 2
Enter course type (ug/pg): pg
Enter student ID: 201
Enter student name: Meera
Enter internal marks: 35
Enter external marks: 50

--- Examination Results ---

Student ID: 101
Name: Arun
Total Marks: 83
Grade: A

Student ID: 201
Name: Meera
Total Marks: 85
Grade: A
"""
