"""
Problem:
Write a Python program to demonstrate runtime polymorphism using method overriding.
Create a base class Animal with a method sound(). 
Derive Dog and Cat classes that override the sound() method.
Read N animals from user input and print the sound made by each animal.
"""

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


animals = []

n = int(input("Enter number of animals: "))

for i in range(n):
    print(f"\nEnter animal type for animal {i+1}:")
    print("Eg: Dog, cat etc.")
    choice = input().strip().lower()

    if choice == "dog":
        animals.append(Dog())
    elif choice == "cat":
        animals.append(Cat())
    else:
        animals.append(Animal())

print("\n--- Animal Sounds ---")
for obj in animals:
    print(obj.sound())


"""
Sample Output:
Enter number of animals: 3

Enter animal type for animal 1:
Eg: Dog, cat etc.
dog

Enter animal type for animal 2:
Eg: Dog, cat etc.
 CAT

Enter animal type for animal 3:
Eg: Dog, cat etc.
cow 

--- Animal Sounds ---
Bark
Meow
Some generic animal sound
"""
