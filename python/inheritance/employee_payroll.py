"""
Problem:
Write a Python program to demonstrate multilevel inheritance.
Create a base class Employee with attributes emp_id and name.
Derive a class PermanentEmployee that adds basic_salary.
Further derive a class Payroll that calculates total salary
by adding HRA and DA based on basic salary.

Read details of N employees from the user and display their
complete salary details.
"""

class Employee:
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name

    def display_basic_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")

class PermanentEmployee(Employee):
    def __init__(self,emp_id,name,basic_salary):
        super().__init__(emp_id,name)
        self.basic_salary=basic_salary

    def display_basic_sal(self):
        print(f"Basic salary: {self.basic_salary}")    

class Payroll(PermanentEmployee):
    def __init__(self, emp_id, name, basic_salary):
        super().__init__(emp_id, name, basic_salary)
        self.hra = 0
        self.da = 0
        self.total_salary = 0

    def calculate_salary(self):
        self.hra = 0.20 * self.basic_salary
        self.da = 0.10 * self.basic_salary
        self.total_salary = self.basic_salary + self.hra + self.da

    def display_full_details(self):
        self.calculate_salary()
        self.display_basic_info()
        self.display_basic_sal()
        print(f"HRA: {self.hra}")
        print(f"DA: {self.da}")
        print(f"Total Salary: {self.total_salary}")
        print("-----------------------------")   

employees=[]
n=int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEnter details of employee {i+1}:")
    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    basic_salary = float(input("Basic Salary: "))

    employees.append(Payroll(emp_id, name, basic_salary))

print("\n--- Employee Payroll Details ---")
for emp in employees:
    emp.display_full_details()    


'''
Sample Output:

Enter number of employees: 2

Enter details of employee 1:
Employee ID: 101
Name: Bruce
Basic Salary: 75000

Enter details of employee 2:
Employee ID: 102
Name: Romanoff
Basic Salary: 86000

--- Employee Payroll Details ---
Employee ID: 101
Name: Bruce
Basic salary: 75000.0
HRA: 15000.0
DA: 7500.0
Total Salary: 97500.0
-----------------------------
Employee ID: 102
Name: Romanoff
Basic salary: 86000.0
HRA: 17200.0
DA: 8600.0
Total Salary: 111800.0
-----------------------------
'''