"""
Problem Statement:
Design a Python program to calculate shipping costs using runtime polymorphism.
Create a base class that defines a common method for calculating shipping cost.
Different shipping modes such as Standard, Express, and International should
override this method to apply their own pricing logic. The program should accept
details for multiple shipments from the user, store the corresponding shipping
objects in a list, and calculate the shipping cost for each shipment using
polymorphism without using conditional logic for cost calculation.
"""

class Shipping:
    def calculate_cost(self,weight,distance):
        pass

class StandardShipping(Shipping):
    def calculate_cost(self, weight, distance):
        return weight * distance * 2


class ExpressShipping(Shipping):
    def calculate_cost(self, weight, distance):
        return weight * distance * 4 + 50


class InternationalShipping(Shipping):
    def calculate_cost(self, weight, distance):
        return weight * distance * 6 + 150
    

shipments=[]
n=int(input("Enter number of shipments: "))

for i in range(n):
    print(f"\nShipment {i + 1}")
    mode = input("Enter shipping mode (standard/express/international): ").lower()
    weight = float(input("Enter package weight: "))
    distance = float(input("Enter shipping distance: "))

    if mode == "standard":
        shipments.append((StandardShipping(), weight, distance))
    elif mode == "express":
        shipments.append((ExpressShipping(), weight, distance))
    elif mode == "international":
        shipments.append((InternationalShipping(), weight, distance))


print("\n--- Shipping Cost Details ---")
i=1
for ship, weight, distance in shipments:
    print(f"Shipping Cost for shipment {i}:", ship.calculate_cost(weight, distance))
    i+=1


'''
Sample Output:

Enter number of shipments: 2 

Shipment 1
Enter shipping mode (standard/express/international): standard
Enter package weight: 5
Enter shipping distance: 12

Shipment 2
Enter shipping mode (standard/express/international): International
Enter package weight: 20
Enter shipping distance: 800

--- Shipping Cost Details ---
Shipping Cost for shipment 1: 120.0
Shipping Cost for shipment 2: 96150.0
'''