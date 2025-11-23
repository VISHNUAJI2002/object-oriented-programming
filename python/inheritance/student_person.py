'''
Write a Python program to demonstrate single inheritance.
Create a base class Person with attributes name and age.
Derive a class Student from Person with additional attributes rollno and mark.
Read details of N students from the user and display them.
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self,name,age,rollno,mark):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark

    def show_student(self):
        self.show_person()
        print("Roll number:",self.rollno)      
        print("Mark :",self.mark)


students=[]
n=int(input("Enter number of students:"))        

for i in range(n):
    roll=int(input("\nRoll no.:"))
    name=input("Name:")
    age=int(input("Age:"))
    mark=float(input("Mark in % :"))
    
    obj=Student(name,age,roll,mark)
    students.append(obj)


print("\n---Student Details---\n")
for i in students:
    i.show_student()    
    print()


'''
Sample Output:

Enter number of students:2

Roll no.:1
Name:Dom
Age:15
Mark in % :67.4

Roll no.:2
Name:Tej
Age:15
Mark in % :99.8

---Student Details---

Name: Dom
Age: 15
Roll number: 1
Mark : 67.4

Name: Tej
Age: 15
Roll number: 2
Mark : 99.8
'''
