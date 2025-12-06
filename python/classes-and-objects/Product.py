"""
Problem:
Create a Python class Product with attributes name, price, and quantity.
Read details of N products from the user, store them as objects,
and display the total value of each product (price * quantity).

This program demonstrates basic OOP concepts:
- Class
- Object
- Constructor (__init__)
- Instance variables
- Instance method
"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: {self.total_value()}")
        print()


products = []

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details of product {i+1}:")
    name = input("Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    obj = Product(name, price, quantity)
    products.append(obj)

print("\n--- Product Details ---")
for p in products:
    p.display()


"""
Sample Output:

Enter number of products: 2

Enter details of product 1:
Name: Pen
Price: 10
Quantity: 5

Enter details of product 2:
Name: Notebook
Price: 40
Quantity: 3

--- Product Details ---
Product: Pen
Price: 10.0
Quantity: 5
Total Value: 50.0

Product: Notebook
Price: 40.0
Quantity: 3
Total Value: 120.0
"""
