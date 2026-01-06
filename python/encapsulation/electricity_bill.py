"""
Problem Statement:
Design a Python program to calculate electricity bills using encapsulation.
Each consumer should have private attributes such as consumer ID, consumer name,
units consumed, and rate per unit. Direct access to these attributes must be
restricted. Provide controlled access through getter methods and calculate the
total electricity bill using a method that internally operates on private
attributes. The program should accept details for multiple consumers from the
user and display the consumer ID, consumer name, and total bill amount.
"""

class ElectricityBill:
    def __init__(self, consumer_id, name, units, rate):
        self.__consumer_id = consumer_id
        self.__name = name
        self.__units = units
        self.__rate = rate

    def get_consumer_id(self):
        return self.__consumer_id

    def get_consumer_name(self):
        return self.__name

    def calculate_bill_amount(self):
        return self.__units * self.__rate


bills = []
n = int(input("Enter number of consumers: "))

for i in range(n):
    print(f"\nConsumer {i + 1}")
    consumer_id = int(input("Enter consumer ID: "))
    name = input("Enter consumer name: ")
    units = float(input("Enter units consumed: "))
    rate = float(input("Enter rate per unit: "))

    bills.append(ElectricityBill(consumer_id, name, units, rate))


print("\n--- Electricity Bill Details ---")
for bill in bills:
    print("\nConsumer ID:", bill.get_consumer_id())
    print("Consumer Name:", bill.get_consumer_name())
    print("Total Bill Amount:", bill.calculate_bill_amount())


'''
Sample Output:

Enter number of consumers: 2

Consumer 1
Enter consumer ID: 301
Enter consumer name: Ramesh
Enter units consumed: 120
Enter rate per unit: 6.5

Consumer 2
Enter consumer ID: 302
Enter consumer name: Suresh
Enter units consumed: 85
Enter rate per unit: 7

--- Electricity Bill Details ---

Consumer ID: 301
Consumer Name: Ramesh
Total Bill Amount: 780.0

Consumer ID: 302
Consumer Name: Suresh
Total Bill Amount: 595.0
'''
