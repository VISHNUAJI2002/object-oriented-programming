/*
Experiment 11 

Class and Objects.

Aim:Define a class ‘product’ with data members pcode, pname and price. Create 3
objects of the class and find the product having the lowest price.
*/

import java.util.*;

class Product {
    int pcode, price;
    String pname;
    Product(int a, String b, int c) {
        pcode = a;
        pname = b;
        price = c;
    }
    void display() {
        System.out.println("Product Code: " + pcode);
        System.out.println("Product Name: " + pname);
        System.out.println("Price: " + price);
    }
}

class Pro {
    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);
        int n = 3;
        Product[] p = new Product[n];

        for (int i = 0; i < n; i++) {
            System.out.println("Enter details for Product ");
            System.out.print("Product Code: ");
            int code = s.nextInt();
            s.nextLine();
            System.out.print("Product Name: ");
            String name = s.nextLine();
            System.out.print("Price: ");
            int price = s.nextInt();
            s.nextLine();
            p[i] = new Product(code, name, price);
        }
        Product lowest = p[0];
        for (int i = 1; i < n; i++) {
            if (p[i].price < lowest.price) {
                lowest = p[i];
            }
        }
        System.out.println("Product with the lowest price:");
        lowest.display();
    }
}

/*
Sample Output:

PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co2> java Pro
Enter details for Product 
Product Code: 123
Product Name: Redmi
Price: 15000
Enter details for Product 
Product Code: 124 
Product Name: Poco
Price: 14000
Enter details for Product 
Product Code: 125
Product Name: Samsung
Price: 25000
Product with the lowest price:
Product Code: 124
Product Name: Poco
Price: 14000
*/
