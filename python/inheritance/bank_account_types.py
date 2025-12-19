"""
Problem:
Write a Python program to demonstrate hierarchical inheritance.
Create a base class BankAccount with account number and balance.
Derive two classes SavingsAccount and CurrentAccount.
SavingsAccount should calculate interest.
CurrentAccount should check minimum balance and apply penalty if required.

Read details of N accounts from the user and display account information.
"""

class BankAccount:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    
    def basic_info(self):
        print(f"Account number: {self.account_no}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self,account_no,balance,rate):
        super().__init__(account_no,balance)
        self.rate=rate
    
    def calculate_interest(self):
        interest=(self.balance*self.rate)/100
        print(f"Interest for {self.balance}rs: {interest}")        
        self.balance+=interest
        print(f"Updated balance: {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self,account_no,balance,minbalance):
        super().__init__(account_no,balance)
        self.minbalance=minbalance

    def check_min_balance(self):
        if self.balance < self.minbalance:
            penalty = 500
            self.balance -= penalty
            print("Minimum balance not maintained.")
            print(f"Penalty applied: {penalty}")
        else:
            print("Minimum balance maintained.")
        print(f"Updated Balance: {self.balance}") 

accounts = []

n = int(input("Enter number of accounts: "))

for i in range(n):
    print(f"\nAccount {i+1}:")
    print("1. Savings Account\n2. Current Account")
    choice = int(input("Enter choice: "))

    acc_no = int(input("Enter account number: "))
    balance = float(input("Enter balance: "))

    if choice == 1:
        rate = float(input("Enter interest rate: "))
        accounts.append(SavingsAccount(acc_no, balance, rate))

    elif choice == 2:
        min_balance = float(input("Enter minimum balance: "))
        accounts.append(CurrentAccount(acc_no, balance, min_balance))

    else:
        print("Invalid choice.")

print("\n--- Account Details ---")
for acc in accounts:
    acc.basic_info()

    if isinstance(acc, SavingsAccount):
        acc.calculate_interest()

    elif isinstance(acc, CurrentAccount):
        acc.check_min_balance()

    print("-----------------------------")


"""
Sample Output:

Enter number of accounts: 2

Account 1:
1. Savings Account
2. Current Account
Enter choice: 1 
Enter account number: 101
Enter balance: 10000
Enter interest rate: 2

Account 2:
1. Savings Account
2. Current Account
Enter choice: 2
Enter account number: 102
Enter balance: 900
Enter minimum balance: 1000

--- Account Details ---
Account number: 101
Balance: 10000.0
Interest for 10000.0rs: 200.0
Updated balance: 10200.0
-----------------------------
Account number: 102
Balance: 900.0
Minimum balance not maintained.
Penalty applied: 500
Updated Balance: 400.0
-----------------------------
"""    