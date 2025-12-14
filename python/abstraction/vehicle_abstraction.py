"""
Problem:
Write a Python program to demonstrate abstraction using an abstract base class.
Create an abstract class Vehicle with an abstract method mileage().
Derive classes Car and Bike that implement the mileage() method.
Read details of N vehicles from the user and display their mileage.

This program demonstrates:
- Abstraction using abstract base class
- Abstract methods
- Implementation of abstract methods in derived classes
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def mileage(self):
        pass

class Car(Vehicle):
    def __init__(self,distance,fuel):
        self.distance=distance
        self.fuel=fuel

    def mileage(self):
        print(f"mileage: {(self.distance/self.fuel):.2f} km/l")

class Bike(Vehicle):
    def __init__(self,distance,fuel):
        self.distance=distance
        self.fuel=fuel

    def mileage(self):
        print(f"mileage: {(self.distance/self.fuel):.2f} km/l")


vehicles=[]
n=int(input("Enter the number of vehicles:"))

for i in range(n):
    print(f"\nVehicle {i+1}:")
    print("1. Car\n2. Bike")
    choice = int(input("Enter choice: "))

    distance=float(input(f"Enter distance travelled (km):"))
    fuel=float(input("Enter fuel consumed (litres):"))

    if choice==1:
        vehicles.append(Car(distance,fuel))
    elif choice==2:
        vehicles.append(Bike(distance,fuel))
    else:
        print("Invalid entry")

for v in vehicles:
    v.mileage() 

"""
Sample Output:

Enter the number of vehicles:2

Vehicle 1:
1. Car
2. Bike
Enter choice: 1
Enter distance travelled (km):150
Enter fuel consumed (litres):7

Vehicle 2:
1. Car
2. Bike
Enter choice: 2
Enter distance travelled (km):150
Enter fuel consumed (litres):5
mileage: 21.43 km/l
mileage: 30.00 km/l
"""                   