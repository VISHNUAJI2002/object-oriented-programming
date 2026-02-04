"""
Problem Statement:
Design a Python program to calculate ride fares using runtime polymorphism.
Create a base class that defines a method for calculating fare. Different ride
types such as Economy Ride, Premium Ride, and Shared Ride should override this
method to apply their own fare calculation logic. The program should accept
details for multiple rides from the user, store the corresponding ride objects
in a single list, and calculate the fare for each ride using polymorphism
without using conditional logic for fare calculation.
"""

class Ride:
    def calculate_fare(self, distance):
        pass


class EconomyRide(Ride):
    def calculate_fare(self, distance):
        return distance * 10


class PremiumRide(Ride):
    def calculate_fare(self, distance):
        return distance * 18 + 50


class SharedRide(Ride):
    def calculate_fare(self, distance):
        return distance * 7


rides = []
n = int(input("Enter number of rides: "))

for i in range(n):
    print(f"\nRide {i + 1}")
    ride_type = input("Enter ride type (economy/premium/shared): ").lower()
    distance = float(input("Enter distance travelled (km): "))

    if ride_type == "economy":
        rides.append((EconomyRide(), distance))
    elif ride_type == "premium":
        rides.append((PremiumRide(), distance))
    elif ride_type == "shared":
        rides.append((SharedRide(), distance))


print("\n--- Ride Fare Details ---")
i = 1
for ride, distance in rides:
    print(f"Fare for ride {i}:", ride.calculate_fare(distance))
    i += 1


"""
Sample Output:

Enter number of rides: 3

Ride 1
Enter ride type (economy/premium/shared): economy
Enter distance travelled (km): 12

Ride 2
Enter ride type (economy/premium/shared): premium
Enter distance travelled (km): 10

Ride 3
Enter ride type (economy/premium/shared): shared
Enter distance travelled (km): 15

--- Ride Fare Details ---
Fare for ride 1: 120.0
Fare for ride 2: 230.0
Fare for ride 3: 105.0
"""
