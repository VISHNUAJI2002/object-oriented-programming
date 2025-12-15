"""
Problem:
Write a Python program to demonstrate abstraction using an abstract base class.
Create an abstract class Payment with an abstract method make_payment().
Derive classes UPI and Card that implement the make_payment() method.
Read payment details from the user and display how the payment is processed.

This program demonstrates abstraction by defining what a payment should do,
while hiding how each payment method processes the payment.
"""

from abc import ABC , abstractmethod

class Payment(ABC):

    @abstractmethod
    def make_payment():
        pass

class UPI(Payment):
    def make_payment(self,amount):
        return f"UPI payment of {amount} rs.processed successfully."

class Card(Payment):
    def make_payment(self,amount):
        return f"Card payment of {amount} rs. processed successfully"

payments=[]
n=int(input("Enter number of payments:"))

for i in range(n):
    print(f"\nPayment {i+1}")
    print("1.UPI\n2.Card")
    amount=float(input("Enter the amount:"))

    choice=int(input("Enter method:"))
    if choice==1:
        payments.append(UPI())
    elif choice==2:
        payments.append(Card())
    else:
        print("Invalid choice. Skipping this payment.")
        continue

    print(payments[-1].make_payment(amount))        

"""
Sample Output:

Enter number of payments:3

Payment 1
1.UPI
2.Card
Enter the amount:1500
Enter method:1
UPI payment of 1500.0 rs.processed successfully.

Payment 2
1.UPI
2.Card
Enter the amount:3400
Enter method:2
Card payment of 3400.0 rs. processed successfully

Payment 3
1.UPI
2.Card
Enter the amount:5000
Enter method:3
Invalid choice. Skipping this payment.
"""    