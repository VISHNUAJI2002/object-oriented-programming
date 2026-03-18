/*
Problem Statement:
Design a Java program to manage inventory items using encapsulation.
Each item should store item ID, item name, unit price, and quantity
as private attributes. Direct access to these attributes must be restricted.
Provide controlled access through getter methods and calculate the total
stock value of an item using a method that internally operates on private
attributes. The program should accept details for multiple items from the
user and display item ID, item name, and total stock value.
*/

import java.util.Scanner;

class InventoryItem {

    private int itemId;
    private String itemName;
    private double unitPrice;
    private int quantity;

    public InventoryItem(int itemId, String itemName, double unitPrice, int quantity) {
        this.itemId = itemId;
        this.itemName = itemName;
        this.unitPrice = unitPrice;
        this.quantity = quantity;
    }

    public int getItemId() {
        return itemId;
    }

    public String getItemName() {
        return itemName;
    }

    public double calculateStockValue() {
        return unitPrice * quantity;
    }
}

public class InventoryItemApp {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        InventoryItem[] items = new InventoryItem[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nItem " + (i + 1));

            System.out.print("Enter item ID: ");
            int id = sc.nextInt();
            sc.nextLine();

            System.out.print("Enter item name: ");
            String name = sc.nextLine();

            System.out.print("Enter unit price: ");
            double price = sc.nextDouble();

            System.out.print("Enter quantity: ");
            int qty = sc.nextInt();

            items[i] = new InventoryItem(id, name, price, qty);
        }

        System.out.println("\n--- Inventory Details ---");

        for (InventoryItem item : items) {
            System.out.println("\nItem ID: " + item.getItemId());
            System.out.println("Item Name: " + item.getItemName());
            System.out.println("Total Stock Value: " + item.calculateStockValue());
        }

        sc.close();
    }
}

/*
Sample Output:

Enter number of items: 2

Item 1
Enter item ID: 501
Enter item name: Keyboard
Enter unit price: 750
Enter quantity: 20

Item 2
Enter item ID: 502
Enter item name: Mouse
Enter unit price: 400
Enter quantity: 35

--- Inventory Details ---

Item ID: 501
Item Name: Keyboard
Total Stock Value: 15000.0

Item ID: 502
Item Name: Mouse
Total Stock Value: 14000.0
*/