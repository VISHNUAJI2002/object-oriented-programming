"""
Problem Statement:
Design a Python program to manage inventory items using encapsulation.
Each inventory item should store item ID, item name, unit price, and quantity
as private attributes. Direct access to these attributes must be restricted.
Provide controlled access through getter methods and calculate the total stock
value of an item using a method that internally operates on private attributes.
The program should accept details for multiple inventory items from the user
and display the item ID, item name, and total stock value.
"""

class InventoryItem:
    def __init__(self, item_id, name, unit_price, quantity):
        self.__item_id = item_id
        self.__name = name
        self.__unit_price = unit_price
        self.__quantity = quantity

    def get_item_id(self):
        return self.__item_id

    def get_item_name(self):
        return self.__name

    def calculate_stock_value(self):
        return self.__unit_price * self.__quantity


items = []
n = int(input("Enter number of inventory items: "))

for i in range(n):
    print(f"\nItem {i + 1}")
    item_id = int(input("Enter item ID: "))
    name = input("Enter item name: ")
    unit_price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    items.append(InventoryItem(item_id, name, unit_price, quantity))


print("\n--- Inventory Stock Details ---")
for item in items:
    print("\nItem ID:", item.get_item_id())
    print("Item Name:", item.get_item_name())
    print("Total Stock Value:", item.calculate_stock_value())


'''
Sample Output:

Enter number of inventory items: 2

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

--- Inventory Stock Details ---

Item ID: 501
Item Name: Keyboard
Total Stock Value: 15000.0

Item ID: 502
Item Name: Mouse
Total Stock Value: 14000.0
'''
