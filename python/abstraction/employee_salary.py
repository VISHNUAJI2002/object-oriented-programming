"""
Problem:
Write a Python program to demonstrate abstraction using an abstract base class.
Create an abstract class Employee with an abstract method calculate_salary().
Derive two classes:
 - FullTimeEmployee (monthly salary + bonus)
 - PartTimeEmployee (hourly wage × hours worked)

Read details of N employees and display their salary details.

This program demonstrates abstraction by defining a common salary structure
while allowing different salary calculations for different employee types.
"""

from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,empid,name):
        self.empid=empid
        self.name=name

    def basic_info(self):
        print(f"Employee ID: {self.empid}")
        print(f"Name: {self.name}")    

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,empid,name,salary,bonus):
        super().__init__(empid,name)
        self.salary=salary
        self.bonus=bonus

    def calculate_salary(self):
        return self.salary + self.bonus
    
class PartTimeEmployee(Employee):
    def __init__(self,empid,name,wage,hours):
        super().__init__(empid,name)
        self.wage=wage
        self.hours=hours

    def calculate_salary(self):
        return self.wage * self.hours
    

employees=[]
n=int(input("Enter number of employees:"))

for i in range(n):
    print(f"\nEmployee {i+1}")
    print("1.Full time employee")
    print("2.Part time employee")
    choice=int(input("Enter your choice (1/2): "))

    id=int(input("Enter employee ID: "))
    name=input("Enter employee name: ")

    if choice==1:
        sal=float(input("Enter salary:"))
        bonus=float(input("Enter Bonus:"))
        employees.append(FullTimeEmployee(id,name,sal,bonus))

    elif choice==2:
        wage=float(input("Enter hourly wage: "))
        hours=float(input("Enter hours worked:"))
        employees.append(PartTimeEmployee(id,name,wage,hours))

    else:
        print("Invalid entry! Skipping employee.")

print("\n--- Employee Salary Details ---")
for emp in employees:
    emp.basic_info()

    print(f"Salary: {emp.calculate_salary()}")  
    print("-----------------------------")       

            
'''
Sample Output:

Enter number of employees:2

Employee 1
1.Full time employee
2.Part time employee
Enter your choice (1/2): 1
Enter employee ID: 101
Enter employee name: Natasha
Enter salary:95000
Enter Bonus:5000

Employee 2
1.Full time employee
2.Part time employee
Enter your choice (1/2): 2
Enter employee ID: 102
Enter employee name: Romanoff
Enter hourly wage: 900
Enter hours worked:94

--- Employee Salary Details ---
Employee ID: 101
Name: Natasha
Salary: 100000.0
-----------------------------
Employee ID: 102
Name: Romanoff
Salary: 84600.0
-----------------------------
'''