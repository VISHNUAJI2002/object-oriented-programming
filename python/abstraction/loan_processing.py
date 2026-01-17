"""
Problem Statement:
Design a Python program to process different types of loans using abstraction.
Create an abstract base class that defines common operations for loan processing
such as checking eligibility and calculating EMI. Different loan types such as
Home Loan, Education Loan, and Personal Loan should provide their own
implementation for these operations. The program should accept details for
multiple loan applications from the user, store the corresponding loan objects
in a list, and display eligibility status and EMI amount using abstraction.
The abstract class should define what operations are required, but not how they
are implemented.
"""

from abc import ABC, abstractmethod


class Loan(ABC):
    @abstractmethod
    def check_eligibility(self, income, amount):
        pass

    @abstractmethod
    def calculate_emi(self, amount, years):
        pass


class HomeLoan(Loan):
    def check_eligibility(self, income, amount):
        return income >= (amount * 0.02)

    def calculate_emi(self, amount, years):
        return amount / (years * 12)


class EducationLoan(Loan):
    def check_eligibility(self, income, amount):
        return income >= 15000

    def calculate_emi(self, amount, years):
        return amount / (years * 12) * 0.9


class PersonalLoan(Loan):
    def check_eligibility(self, income, amount):
        return income >= (amount * 0.05)

    def calculate_emi(self, amount, years):
        return amount / (years * 12) * 1.2


applications = []
n = int(input("Enter number of loan applications: "))

for i in range(n):
    print(f"\nApplication {i + 1}")
    loan_type = input("Enter loan type (home/education/personal): ").lower()
    income = float(input("Enter monthly income: "))
    amount = float(input("Enter loan amount: "))
    years = int(input("Enter loan tenure (years): "))

    if loan_type == "home":
        applications.append((HomeLoan(), income, amount, years))
    elif loan_type == "education":
        applications.append((EducationLoan(), income, amount, years))
    elif loan_type == "personal":
        applications.append((PersonalLoan(), income, amount, years))


print("\n--- Loan Processing Results ---")
i = 1
for loan, income, amount, years in applications:
    print(f"\nApplication {i}")
    if loan.check_eligibility(income, amount):
        print("Status: Eligible")
        print("Monthly EMI:", loan.calculate_emi(amount, years))
    else:
        print("Status: Not Eligible")
    i += 1


"""
Sample Output:

Enter number of loan applications: 2

Application 1
Enter loan type (home/education/personal): home
Enter monthly income: 60000
Enter loan amount: 2000000
Enter loan tenure (years): 20

Application 2
Enter loan type (home/education/personal): personal
Enter monthly income: 25000
Enter loan amount: 800000
Enter loan tenure (years): 5

--- Loan Processing Results ---

Application 1
Status: Eligible
Monthly EMI: 8333.333333333334

Application 2
Status: Not Eligible
"""
