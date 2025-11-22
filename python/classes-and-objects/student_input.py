'''
Write a Python program using class and objects to read details of N students (where N is entered by the user).
Store each student as an object and display the details of all students.
'''

class Student:
    def __init__(self,rollno,name,mark):
        self.rollno=rollno
        self.name=name
        self.mark=mark

    def display(self):
        print("Roll number:",self.rollno) 
        print("Name:",self.name)
        print("Mark (%):",self.mark)


students=[]
n=int(input("Enter number of students:"))

for i in range(n):
    roll=int(input("Roll no:"))
    name=input("Name:")
    mark=input("Mark in %:")

    stud=Student(roll,name,mark)
    students.append(stud)


print("\n---Student Details---")
for s in students:
    s.display()
    print()    



'''
Sample Output:

Enter number of students:3
Roll no:1
Name:Abhi
Mark in %:82
Roll no:2
Name:Adwaith
Mark in %:76
Roll no:3
Name:Allen
Mark in %:91

---Student Details---
Roll number: 1
Name: Abhi
Mark (%): 82

Roll number: 2
Name: Adwaith
Mark (%): 76

Roll number: 3
Name: Allen
Mark (%): 91
'''