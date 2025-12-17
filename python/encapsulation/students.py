"""
Problem:
Write a Python program to demonstrate encapsulation using a Student class.
The class should contain private attributes __roll_no, __name, and __marks.
Provide getter methods to access student details and a method to calculate
and return the grade based on marks.

Read details of N students from the user and display their details and grades.
"""

class Student:
    def __init__(self,roll,name,marks):
        self.__roll=roll
        self.__name=name
        self.__marks=marks

    def get_roll(self):
        return self.__roll
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks
    
    def get_grade(self):
        if self.__marks>=90:
            return "A" 
        elif self.__marks>=75:
            return "B"
        elif self.__marks>=60:
            return "C"
        else:
            return "D"
        
students=[]
n=int(input("Enter number of students:"))

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    roll=input("Roll number: ")
    name=input("Name: ")
    marks=float(input("Marks: "))
    
    students.append(Student(roll,name,marks))

print("\n---Student Details---\n")
for j in range(n):
    print("Student ",j+1)
    print(f"Roll number: {students[j].get_roll()}")
    print(f"Name: {students[j].get_name()}")
    print(f"Marks: {students[j].get_marks()}")
    print(f"Grade: {students[j].get_grade()}")
    print()


"""
Sample Output:

Enter number of students:2

Enter details for student 1
Roll number: 8
Name: Steve
Marks: 82

Enter details for student 2
Roll number: 14
Name: Tony
Marks: 98

---Student Details---

Student  1
Roll number: 8
Name: Steve
Marks: 82.0
Grade: B

Student  2
Roll number: 14
Name: Tony
Marks: 98.0
Grade: A
"""    