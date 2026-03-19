/*
Problem Statement:
Design a Java program to manage bank account details using encapsulation.
Each account should store account number, account holder name, and balance
as private attributes. Direct access to these attributes must be restricted.
Provide controlled access using getter methods and allow balance updates only
through deposit and withdraw methods with proper validation. The program should
accept details for multiple accounts and perform transactions, then display
account details and final balance.
*/

import java.util.Scanner;

class BankAccount {

    private int accountNumber;
    private String accountHolder;
    private double balance;

    public BankAccount(int accountNumber, String accountHolder, double balance) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = balance;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public String getAccountHolder() {
        return accountHolder;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        } else {
            System.out.println("Invalid deposit amount");
        }
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid withdrawal amount");
        } else if (amount > balance) {
            System.out.println("Insufficient balance");
        } else {
            balance -= amount;
        }
    }
}

public class BankAccountApp {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of accounts: ");
        int n = sc.nextInt();

        BankAccount[] accounts = new BankAccount[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nAccount " + (i + 1));

            System.out.print("Enter account number: ");
            int accNo = sc.nextInt();
            sc.nextLine();

            System.out.print("Enter account holder name: ");
            String name = sc.nextLine();

            System.out.print("Enter initial balance: ");
            double balance = sc.nextDouble();

            accounts[i] = new BankAccount(accNo, name, balance);

            System.out.print("Enter deposit amount: ");
            double deposit = sc.nextDouble();
            accounts[i].deposit(deposit);

            System.out.print("Enter withdrawal amount: ");
            double withdraw = sc.nextDouble();
            accounts[i].withdraw(withdraw);
        }

        System.out.println("\n--- Account Details ---");

        for (BankAccount acc : accounts) {
            System.out.println("\nAccount Number: " + acc.getAccountNumber());
            System.out.println("Account Holder: " + acc.getAccountHolder());
            System.out.println("Final Balance: " + acc.getBalance());
        }

        sc.close();
    }
}

/*
Sample Output:

Enter number of accounts: 1

Account 1
Enter account number: 101
Enter account holder name: Rahul
Enter initial balance: 5000
Enter deposit amount: 2000
Enter withdrawal amount: 1000

--- Account Details ---

Account Number: 101
Account Holder: Rahul
Final Balance: 6000.0
*/