/*
Problem Statement:
Design a Java program to calculate tax using runtime polymorphism.
Create a base class that defines a method for calculating tax.
Different tax types such as Income Tax, Corporate Tax, and Service Tax
should override this method to provide their own tax calculation logic.
The program should accept multiple tax entries from the user and display
the calculated tax for each entry using polymorphism.
*/

import java.util.Scanner;

class Tax {
    public double calculateTax(double amount) {
        return 0;
    }
}

class IncomeTax extends Tax {
    @Override
    public double calculateTax(double amount) {
        return amount * 0.10;
    }
}

class CorporateTax extends Tax {
    @Override
    public double calculateTax(double amount) {
        return amount * 0.25;
    }
}

class ServiceTax extends Tax {
    @Override
    public double calculateTax(double amount) {
        return amount * 0.15;
    }
}

public class TaxCalculation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of tax entries: ");
        int n = sc.nextInt();

        Tax[] entries = new Tax[n];
        double[] amounts = new double[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nEntry " + (i + 1));
            System.out.print("Enter tax type (income/corporate/service): ");
            String type = sc.next();

            System.out.print("Enter taxable amount: ");
            double amount = sc.nextDouble();
            amounts[i] = amount;

            if (type.equalsIgnoreCase("income")) {
                entries[i] = new IncomeTax();
            } else if (type.equalsIgnoreCase("corporate")) {
                entries[i] = new CorporateTax();
            } else if (type.equalsIgnoreCase("service")) {
                entries[i] = new ServiceTax();
            }
        }

        System.out.println("\n--- Tax Calculation Details ---");
        for (int i = 0; i < n; i++) {
            System.out.println("Tax for entry " + (i + 1) + ": " +
                    entries[i].calculateTax(amounts[i]));
        }

        sc.close();
    }
}

/*
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
*/