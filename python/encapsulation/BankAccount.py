"""
Problem:
Write a Python program to demonstrate encapsulation using a BankAccount class.
The class should contain private attributes __account_no and __balance.
Provide methods to:
 - deposit money (with validation)
 - withdraw money (with validation)
 - display account details using getters

Read account details and multiple transactions from the user and display the results.
"""

class BankAccount:
    def __init__(self,account_no):
        self.__account_no=account_no
        self.__balance=0

    def get_account_no(self):
        return self.__account_no

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount<=0:
            print("Please enter a valid amount.")
        else:
            self.__balance+=amount
            print(f"Deposited amount:{amount}\nCurrent Balance:{self.__balance}")

    def withdraw(self,amount):
        if self.__balance<amount:
            print("Insufficient balance!")
            print(f"Current balance: {self.__balance}")
        elif amount<=0:
            print("Please enter a valid amount")    
        else:
            self.__balance-=amount 
            print(f"Withdrawn amount: {amount}")
            print(f"Current balance: {self.__balance}") 

acc_no=int(input("Enter account number:"))
account=BankAccount(acc_no)

n=int(input("Enter number of transactions:"))

for i in range(n):
    print(f"\nTransaction {i+1}:")
    print("1. Deposit\n2. Withdraw")
    choice = int(input("Enter choice: "))

    if choice==1:
        amount=int(input("Enter amount:"))
        account.deposit(amount)

    elif choice==2:
        amount=int(input("Enter amount to be withdrawn:"))
        account.withdraw(amount)
    
    else:
        print("Invalid choice.")

print("\n--- Final Account Details ---")
print(f"Account Number: {account.get_account_no()}")
print(f"Final Balance: {account.get_balance()}")    

"""
Sample Output:

Enter account number:12345
Enter number of transactions:5

Transaction 1:
1. Deposit
2. Withdraw
Enter choice: 1 
Enter amount:1000
Deposited amount:1000
Current Balance:1000

Transaction 2:
1. Deposit
2. Withdraw
Enter choice: 1
Enter amount:-500
Please enter a valid amount.

Transaction 3:
1. Deposit
2. Withdraw
Enter choice: 1
Enter amount:500
Deposited amount:500
Current Balance:1500

Transaction 4:
1. Deposit
2. Withdraw
Enter choice: 2
Enter amount to be withdrawn:2000
Insufficient balance!
Current balance: 1500

Transaction 5:
1. Deposit
2. Withdraw
Enter choice: 2
Enter amount to be withdrawn:800
Withdrawn amount: 800
Current balance: 700

--- Final Account Details ---
Account Number: 12345
Final Balance: 700
"""