"""
Problem Statement:
Design a Python program to manage employee payroll details using encapsulation.
The program should store employee information such as employee ID, name, basic
salary, allowances, and deductions as private attributes. Direct access to these
attributes must be restricted. Provide controlled access using getter methods
and compute the net salary using a method of the class that internally operates on private attributes. 
The program should accept input from the user and display the employee ID, employee name, 
and net salary.
"""

class EmployeePayroll:
    def __init__(self,emp_id,name,salary,allowances,deductions):
        self.__emp_id=emp_id
        self.__name=name
        self.__salary=salary
        self.__allowances=allowances
        self.__deductions=deductions

    def get_emp_id(self):
        return self.__emp_id
    def get_name(self):
        return self.__name
    def calculate_net_salary(self):
        return self.__salary + self.__allowances - self.__deductions    
    
employees=[]
n=int(input("Enter number of employees: "))

for i in range(n):
    print(f"Employee {i+1}")
    id=int(input("Enter Employee ID: "))
    name=input("Enter name: ")
    sal=float(input("Enter salary: "))
    allowance=float(input("Enter allowances: "))
    deduction=float(input("Enter deductions: "))

    employees.append(EmployeePayroll(id,name,sal,allowance,deduction))

print("\n--- Employee Details ---")
for emp in employees:
    print("\nEmployee ID: ",emp.get_emp_id())
    print("Employee name: ",emp.get_name())
    print("Net salary: ",emp.calculate_net_salary())

'''
Sample Output:

Enter number of employees: 2
Employee 1
Enter Employee ID: 101
Enter name: Chadwick
Enter salary: 47500
Enter allowances: 15000
Enter deductions: 2500
Employee 2
Enter Employee ID: 102
Enter name: Bossman
Enter salary: 48000
Enter allowances: 14000
Enter deductions: 4500

--- Employee Details ---

Employee ID:  101
Employee name:  Chadwick
Net salary:  60000.0

Employee ID:  102
Employee name:  Bossman
Net salary:  57500.0
'''    