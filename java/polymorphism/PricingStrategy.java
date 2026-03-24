/*
Problem Statement:
Design a Java program to calculate final product prices using runtime polymorphism.
Create a base class Pricing with a method calculatePrice().

Derive RegularPricing, DiscountPricing, and PremiumPricing classes and override
the method to apply different pricing strategies.

Apply the following conditions:
- RegularPricing: no change in price
- DiscountPricing: apply percentage discount
- PremiumPricing: add premium charge

The program should accept multiple pricing entries and display final prices.
*/

import java.util.Scanner;

class Pricing {

    public double calculatePrice(double amount) {
        return amount;
    }
}

class RegularPricing extends Pricing {

    @Override
    public double calculatePrice(double amount) {
        return amount;
    }
}

class DiscountPricing extends Pricing {

    private double discountPercent;

    public DiscountPricing(double discountPercent) {
        this.discountPercent = discountPercent;
    }

    @Override
    public double calculatePrice(double amount) {
        return amount - (amount * discountPercent / 100);
    }
}

class PremiumPricing extends Pricing {

    private double premiumCharge;

    public PremiumPricing(double premiumCharge) {
        this.premiumCharge = premiumCharge;
    }

    @Override
    public double calculatePrice(double amount) {
        return amount + premiumCharge;
    }
}

public class PricingStrategy {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of entries: ");
        int n = sc.nextInt();

        Pricing[] strategies = new Pricing[n];
        double[] amounts = new double[n];

        for (int i = 0; i < n; i++) {

            System.out.println("\nEntry " + (i + 1));

            System.out.print("Enter type (regular/discount/premium): ");
            String type = sc.next();

            System.out.print("Enter amount: ");
            double amount = sc.nextDouble();
            amounts[i] = amount;

            if (type.equalsIgnoreCase("regular")) {
                strategies[i] = new RegularPricing();

            } else if (type.equalsIgnoreCase("discount")) {
                System.out.print("Enter discount percentage: ");
                double discount = sc.nextDouble();
                strategies[i] = new DiscountPricing(discount);

            } else if (type.equalsIgnoreCase("premium")) {
                System.out.print("Enter premium charge: ");
                double charge = sc.nextDouble();
                strategies[i] = new PremiumPricing(charge);

            } else {
                System.out.println("Invalid type");
                i--;
                continue;
            }
        }

        System.out.println("\n--- Final Prices ---");

        for (int i = 0; i < n; i++) {
            double finalPrice = strategies[i].calculatePrice(amounts[i]);
            System.out.println("Final Price: " + finalPrice);
        }

        sc.close();
    }
}

/*
Sample Output:

Enter number of entries: 1

Entry 1
Enter type (regular/discount/premium): discount
Enter amount: 1000
Enter discount percentage: 10

--- Final Prices ---
Final Price: 900.0
*/