/*
Problem Statement:
Design a Java program to manage different types of loans using inheritance.
Create a base class Loan with common details like loan ID, applicant name,
principal amount, and interest rate. Derive HomeLoan, EducationLoan, and
CarLoan classes with additional attributes.

Apply the following conditions while calculating interest:
- HomeLoan: reduce interest rate for high property value
- EducationLoan: increase interest rate for longer course duration
- CarLoan: increase interest rate for older cars

Override the method to calculate interest accordingly. The program should
accept multiple loan details and display calculated interest for each loan.
*/

import java.util.Scanner;

class Loan {

    protected String loanId;
    protected String applicantName;
    protected double principalAmount;
    protected double interestRate;

    public Loan(String loanId, String applicantName, double principalAmount, double interestRate) {
        this.loanId = loanId;
        this.applicantName = applicantName;
        this.principalAmount = principalAmount;
        this.interestRate = interestRate;
    }

    public double calculateInterest() {
        return principalAmount * interestRate / 100;
    }
}

class HomeLoan extends Loan {

    private double propertyValue;

    public HomeLoan(String loanId, String applicantName, double principalAmount, double interestRate, double propertyValue) {
        super(loanId, applicantName, principalAmount, interestRate);
        this.propertyValue = propertyValue;
    }

    @Override
    public double calculateInterest() {
        double rate = interestRate;

        if (propertyValue > 5000000) {
            rate -= 1;
        }

        return principalAmount * rate / 100;
    }
}

class EducationLoan extends Loan {

    private int courseDuration;

    public EducationLoan(String loanId, String applicantName, double principalAmount, double interestRate, int courseDuration) {
        super(loanId, applicantName, principalAmount, interestRate);
        this.courseDuration = courseDuration;
    }

    @Override
    public double calculateInterest() {
        double rate = interestRate;

        if (courseDuration > 4) {
            rate += 1.5;
        }

        return principalAmount * rate / 100;
    }
}

class CarLoan extends Loan {

    private int carAge;

    public CarLoan(String loanId, String applicantName, double principalAmount, double interestRate, int carAge) {
        super(loanId, applicantName, principalAmount, interestRate);
        this.carAge = carAge;
    }

    @Override
    public double calculateInterest() {
        double rate = interestRate;

        if (carAge > 5) {
            rate += 2;
        } else if (carAge > 2) {
            rate += 1;
        }

        return principalAmount * rate / 100;
    }
}

public class LoanProcessing {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of loans: ");
        int n = sc.nextInt();
        sc.nextLine();

        Loan[] loans = new Loan[n];

        for (int i = 0; i < n; i++) {

            System.out.println("\nLoan " + (i + 1));

            System.out.print("Enter loan type (home/education/car): ");
            String type = sc.nextLine().toLowerCase();

            System.out.print("Enter loan ID: ");
            String loanId = sc.nextLine();

            System.out.print("Enter applicant name: ");
            String name = sc.nextLine();

            System.out.print("Enter principal amount: ");
            double principal = sc.nextDouble();

            System.out.print("Enter interest rate: ");
            double rate = sc.nextDouble();

            if (type.equals("home")) {
                System.out.print("Enter property value: ");
                double value = sc.nextDouble();
                loans[i] = new HomeLoan(loanId, name, principal, rate, value);

            } else if (type.equals("education")) {
                System.out.print("Enter course duration: ");
                int duration = sc.nextInt();
                loans[i] = new EducationLoan(loanId, name, principal, rate, duration);

            } else if (type.equals("car")) {
                System.out.print("Enter car age: ");
                int age = sc.nextInt();
                loans[i] = new CarLoan(loanId, name, principal, rate, age);

            } else {
                System.out.println("Invalid type");
                i--;
                sc.nextLine();
                continue;
            }

            sc.nextLine();
        }

        System.out.println("\n--- Loan Details ---");

        for (Loan loan : loans) {
            System.out.println("\nLoan ID: " + loan.loanId);
            System.out.println("Applicant: " + loan.applicantName);
            System.out.println("Interest: " + loan.calculateInterest());
        }

        sc.close();
    }
}

/*
Sample Output:

Enter number of loans: 1

Loan 1
Enter loan type (home/education/car): home
Enter loan ID: L101
Enter applicant name: Arun
Enter principal amount: 500000
Enter interest rate: 8
Enter property value: 6000000

--- Loan Details ---

Loan ID: L101
Applicant: Arun
Interest: 35000.0
*/