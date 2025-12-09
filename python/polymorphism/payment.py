"""
Problem:
Write a Python program to demonstrate runtime polymorphism using method overriding.
Create a base class Payment with a method pay().
Derive classes UPI, Card, and Cash that override the pay() method.
Read N payments from the user and display how each payment is processed.
"""

class Payment:
    def pay(self, amount):
        return f"Processing payment of {amount} units."

class UPI(Payment):
    def pay(self, amount):
        return f"Processing UPI payment of {amount} units."

class Card(Payment):
    def pay(self, amount):
        return f"Processing Card payment of {amount} units."

class Cash(Payment):
    def pay(self, amount):
        return f"Processing Cash payment of {amount} units."


payments = []

n = int(input("Enter number of payments: "))

for i in range(n):
    print(f"\nEnter payment method for transaction {i+1}:")
    print("Options: upi / card / cash")

    method = input().strip().lower()
    amount = float(input("Enter amount: "))

    if method == "upi":
        payments.append((UPI(), amount))
    elif method == "card":
        payments.append((Card(), amount))
    elif method == "cash":
        payments.append((Cash(), amount))
    else:
        print("Unknown method, using generic Payment.")
        payments.append((Payment(), amount))

print("\n--- Payment Processing ---")
for p, amt in payments:
    print(p.pay(amt))


'''
Sample Output:

Enter number of payments: 3

Enter payment method for transaction 1:
Options: upi / card / cash
UPI
Enter amount: 100

Enter payment method for transaction 2:
Options: upi / card / cash
cash
Enter amount: 5000

Enter payment method for transaction 3:
Options: upi / card / cash
card
Enter amount: 10500

--- Payment Processing ---
Processing UPI payment of 100.0 units.
Processing Cash payment of 5000.0 units.
Processing Card payment of 10500.0 units.
'''