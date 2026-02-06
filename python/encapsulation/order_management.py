"""
Problem Statement:
Design a Python program to manage online orders using encapsulation.
Each order should store order ID, customer name, item price, quantity,
and discount percentage as private attributes. Direct access to these
attributes must be restricted. Provide controlled access using getter
methods and setter methods where necessary. The program should calculate
the final payable amount internally after applying discount. The program
should accept details for multiple orders from the user and display the
order ID, customer name, and final payable amount.
"""

class Order:
    def __init__(self, order_id, customer_name, price, quantity):
        self.__order_id = order_id
        self.__customer_name = customer_name
        self.__price = price
        self.__quantity = quantity
        self.__discount = 0.0   # percentage

    def get_order_id(self):
        return self.__order_id

    def get_customer_name(self):
        return self.__customer_name

    def set_discount(self, discount):
        if 0 <= discount <= 50:
            self.__discount = discount

    def calculate_total_amount(self):
        return self.__price * self.__quantity

    def calculate_final_amount(self):
        total = self.calculate_total_amount()
        discount_amount = total * (self.__discount / 100)
        return total - discount_amount


orders = []
n = int(input("Enter number of orders: "))

for i in range(n):
    print(f"\nOrder {i + 1}")
    oid = int(input("Enter order ID: "))
    name = input("Enter customer name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    discount = float(input("Enter discount percentage: "))

    order = Order(oid, name, price, quantity)
    order.set_discount(discount)

    orders.append(order)


print("\n--- Order Payment Details ---")
for order in orders:
    print("\nOrder ID:", order.get_order_id())
    print("Customer Name:", order.get_customer_name())
    print("Final Payable Amount:", order.calculate_final_amount())


'''
Sample Output:

Enter number of orders: 2

Order 1
Enter order ID: 401
Enter customer name: Akhil
Enter item price: 1200
Enter quantity: 3
Enter discount percentage: 10

Order 2
Enter order ID: 402
Enter customer name: Sneha
Enter item price: 850
Enter quantity: 2
Enter discount percentage: 20

--- Order Payment Details ---

Order ID: 401
Customer Name: Akhil
Final Payable Amount: 3240.0

Order ID: 402
Customer Name: Sneha
Final Payable Amount: 1360.0
'''
