'''
Question:
Write a Python program to demonstrate inheritance using a general Shape class
and two derived classes: Circle and Rectangle. The base class Shape should
contain a method area() which returns 0. The derived classes must override
the area() method to compute the correct area of a circle and rectangle.
Accept dimensions from the user, create objects of Circle and Rectangle,
and display their areas.
'''

class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shapes = []

n = int(input("Enter number of shapes: "))

for i in range(n):
    print(f"\nShape {i+1}:")
    print("1. Rectangle")
    print("2. Circle")
    choice = int(input("Choose shape type: "))

    if choice == 1:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        shapes.append(Rectangle(l, w))

    elif choice == 2:
        r = float(input("Enter radius: "))
        shapes.append(Circle(r))

    else:
        print("Invalid choice.")


print("\n--- Areas of Shapes ---")
for s in shapes:
    print(f"Area = {s.area()}")


'''
Sample Output:

Enter number of shapes: 2

Shape 1:
1. Rectangle
2. Circle
Choose shape type: 1
Enter length: 10
Enter width: 5

Shape 2:
1. Rectangle
2. Circle
Choose shape type: 2
Enter radius: 5

--- Areas of Shapes ---
Area = 50.0
Area = 78.5
'''