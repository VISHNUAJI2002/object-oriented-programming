/*
Experiment 17

Interface 1- Find area and perimeter of objects

Aim
Create an interface having prototypes of functions area() and perimeter(). Create two
classes Circle and Rectangle which implements the above interface. Create a menu
driven program to find area and perimeter of objects.
*/

import java.util.*;

interface Shape {
    double area();
    double perimeter();
}

class Circle implements Shape {
    double r;
    Circle(double r){
        this.r = r;
    }

    public double area(){
        return 3.14 * r * r;
    }
    
    public double perimeter(){
        return 2 * 3.14 * r;
    }
}

class Rectangle implements Shape{
    double l, w;
    Rectangle(double l, double w){
        this.l = l;
        this.w = w;
    }

    public double area(){
        return l * w;
    }

    public double perimeter(){
        return 2 * (l + w);
    }
}

class Shapes{
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);

        while (true){
            System.out.println("\nMenu:");
            System.out.println("1. Circle");
            System.out.println("2. Rectangle");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int choice = in.nextInt();

            if (choice == 3) {
            System.out.println("Exiting ....");
            break;
            }

            switch (choice) {

            case 1:
            System.out.print("Enter radius of the circle: ");
            double ra = in.nextDouble();
            Circle c = new Circle(ra);

            System.out.println("Area of Circle: " + c.area());
            System.out.println("Perimeter of Circle: " + c.perimeter());
            break;

            case 2:
            System.out.print("Enter length of the rectangle: ");
            double l = in.nextDouble();
            System.out.print("Enter width of the rectangle: ");
            double w = in.nextDouble();

            Rectangle rect= new Rectangle(l,w);

            System.out.println("Area of Rectangle: " + rect.area());
            System.out.println("Perimeter of Rectangle: " + rect.perimeter());
            break;

            default: System.out.println("Invalid choice. ");
            }
        }
    }
}    

/*

Sample Output:


Menu:
1. Circle
2. Rectangle
3. Exit
Choose an option: 1
Enter radius of the circle: 4
Area of Circle: 50.24
Perimeter of Circle: 25.12

Menu:
1. Circle
2. Rectangle
3. Exit
Choose an option: 2
Enter length of the rectangle: 5
Enter width of the rectangle: 3
Area of Rectangle: 15.0
Perimeter of Rectangle: 16.0

Menu:
1. Circle
2. Rectangle
3. Exit
Choose an option: 3
Exiting ....

*/