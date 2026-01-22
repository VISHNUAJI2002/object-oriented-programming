"""
Problem Statement:
Design a Python program to calculate tax amounts using runtime polymorphism.
Create a base class that defines a method for calculating tax. Different tax
types such as Income Tax, Corporate Tax, and Service Tax should override this
method to apply their own tax calculation logic. The program should accept
details for multiple tax calculations from the user, store the corresponding
tax objects in a list, and compute the tax amount for each entry using
polymorphism without using conditional logic for tax calculation.
"""

class Tax:
    def calculate_tax(self, amount):
        pass


class IncomeTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.10


class CorporateTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.25


class ServiceTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.15


tax_entries = []
n = int(input("Enter number of tax entries: "))

for i in range(n):
    print(f"\nEntry {i + 1}")
    tax_type = input("Enter tax type (income/corporate/service): ").lower()
    amount = float(input("Enter taxable amount: "))

    if tax_type == "income":
        tax_entries.append((IncomeTax(), amount))
    elif tax_type == "corporate":
        tax_entries.append((CorporateTax(), amount))
    elif tax_type == "service":
        tax_entries.append((ServiceTax(), amount))


print("\n--- Tax Calculation Details ---")
i = 1
for tax, amount in tax_entries:
    print(f"Tax for entry {i}:", tax.calculate_tax(amount))
    i += 1


"""
Sample Output:

Enter number of tax entries: 3

Entry 1
Enter tax type (income/corporate/service): income
Enter taxable amount: 500000

Entry 2
Enter tax type (income/corporate/service): corporate
Enter taxable amount: 800000

Entry 3
Enter tax type (income/corporate/service): service
Enter taxable amount: 120000

--- Tax Calculation Details ---
Tax for entry 1: 50000.0
Tax for entry 2: 200000.0
Tax for entry 3: 18000.0
"""
