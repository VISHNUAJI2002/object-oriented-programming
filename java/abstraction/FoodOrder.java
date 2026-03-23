/*
Problem Statement:
Design a Java program to manage different types of food orders using abstraction.
Create an abstract class Order with common details like order ID, customer name,
and quantity. Define an abstract method calculateBill().

Derive DineInOrder, TakeAwayOrder, and DeliveryOrder classes with specific attributes.

Apply the following conditions:
- DineInOrder: include service charge
- TakeAwayOrder: apply packaging charge
- DeliveryOrder: include delivery fee based on distance

The program should accept multiple orders and display the total bill for each order.
*/

import java.util.Scanner;

abstract class Order {

    protected String orderId;
    protected String customerName;
    protected int quantity;
    protected double pricePerItem;

    public Order(String orderId, String customerName, int quantity, double pricePerItem) {
        this.orderId = orderId;
        this.customerName = customerName;
        this.quantity = quantity;
        this.pricePerItem = pricePerItem;
    }

    abstract double calculateBill();
}

class DineInOrder extends Order {

    private double serviceCharge;

    public DineInOrder(String orderId, String customerName, int quantity, double pricePerItem, double serviceCharge) {
        super(orderId, customerName, quantity, pricePerItem);
        this.serviceCharge = serviceCharge;
    }

    @Override
    double calculateBill() {
        return (quantity * pricePerItem) + serviceCharge;
    }
}

class TakeAwayOrder extends Order {

    private double packagingCharge;

    public TakeAwayOrder(String orderId, String customerName, int quantity, double pricePerItem, double packagingCharge) {
        super(orderId, customerName, quantity, pricePerItem);
        this.packagingCharge = packagingCharge;
    }

    @Override
    double calculateBill() {
        return (quantity * pricePerItem) + packagingCharge;
    }
}

class DeliveryOrder extends Order {

    private double distance;

    public DeliveryOrder(String orderId, String customerName, int quantity, double pricePerItem, double distance) {
        super(orderId, customerName, quantity, pricePerItem);
        this.distance = distance;
    }

    @Override
    double calculateBill() {
        double deliveryFee;

        if (distance <= 5) {
            deliveryFee = 50;
        } else if (distance <= 10) {
            deliveryFee = 100;
        } else {
            deliveryFee = 150;
        }

        return (quantity * pricePerItem) + deliveryFee;
    }
}

public class FoodOrder {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of orders: ");
        int n = sc.nextInt();
        sc.nextLine();

        Order[] orders = new Order[n];

        for (int i = 0; i < n; i++) {

            System.out.println("\nOrder " + (i + 1));

            System.out.print("Enter order type (dinein/takeaway/delivery): ");
            String type = sc.nextLine().toLowerCase();

            System.out.print("Enter order ID: ");
            String id = sc.nextLine();

            System.out.print("Enter customer name: ");
            String name = sc.nextLine();

            System.out.print("Enter quantity: ");
            int qty = sc.nextInt();

            System.out.print("Enter price per item: ");
            double price = sc.nextDouble();

            if (type.equals("dinein")) {
                System.out.print("Enter service charge: ");
                double service = sc.nextDouble();
                orders[i] = new DineInOrder(id, name, qty, price, service);

            } else if (type.equals("takeaway")) {
                System.out.print("Enter packaging charge: ");
                double pack = sc.nextDouble();
                orders[i] = new TakeAwayOrder(id, name, qty, price, pack);

            } else if (type.equals("delivery")) {
                System.out.print("Enter delivery distance: ");
                double dist = sc.nextDouble();
                orders[i] = new DeliveryOrder(id, name, qty, price, dist);

            } else {
                System.out.println("Invalid type");
                i--;
                sc.nextLine();
                continue;
            }

            sc.nextLine();
        }

        System.out.println("\n--- Order Bills ---");

        for (Order order : orders) {
            System.out.println("\nOrder ID: " + order.orderId);
            System.out.println("Customer: " + order.customerName);
            System.out.println("Total Bill: " + order.calculateBill());
        }

        sc.close();
    }
}

/*
Sample Output:

Enter number of orders: 1

Order 1
Enter order type (dinein/takeaway/delivery): delivery
Enter order ID: F101
Enter customer name: Anu
Enter quantity: 2
Enter price per item: 200
Enter delivery distance: 8

--- Order Bills ---

Order ID: F101
Customer: Anu
Total Bill: 500.0
*/