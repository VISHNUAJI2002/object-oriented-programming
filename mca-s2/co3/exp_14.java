/*
Experiment 14 :

Method Overloading

Aim:
Write a java program to calculate the area of different shapes namely circle, rectangle
and triangle using the concept of method overloading.
*/

import java.util.Scanner;

class ShapesArea{
    
    void area(int length,int breadth){
        System.out.println("Rectangle Area: " + length*breadth);
    }

    void area(float radius){
        System.out.println("Circle area: " + 3.14*radius*radius);
    }

    void area(float base, float height){
        System.out.println("Triangle Area: " + 0.5*base*height);
    }
}

class Area{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        ShapesArea obj=new ShapesArea();

        while (true){
            System.out.println("\n1.Rectangle area");
            System.out.println("2.Circle area");
            System.out.println("3.Triangle area");
            System.out.println("4.Exit");
            System.out.print("Enter your choice:");

            int choice=s.nextInt();

            switch (choice){
                case 1:
                    System.out.println("Enter length and breadth:");
                    int l = s.nextInt();
                    int b = s.nextInt();
                    obj.area(l, b);
                    break;

                    case 2:
                    System.out.print("Enter radius: ");
                    float r = s.nextFloat();
                    obj.area(r);
                    break;

                    case 3:
                    System.out.print("Enter base and height: ");
                    float base = s.nextFloat();
                    float height = s.nextFloat();
                    obj.area(base, height);
                    break;    

                    case 4:
                    System.out.println("Exited.");
                    return;

                    default:
                        System.out.println("Invalid Choice!");
            }
        }
    }
}

/*

Sample Output:

1.Rectangle area
2.Circle area
3.Triangle area
4.Exit
Enter your choice:1
Enter length and breadth:
10 5
Rectangle Area: 50

1.Rectangle area
2.Circle area
3.Triangle area
4.Exit
Enter your choice:2
Enter radius: 4
Circle area: 50.24

1.Rectangle area
2.Circle area
3.Triangle area
4.Exit
Enter your choice:3
Enter base and height: 10 4
Triangle Area: 20.0

1.Rectangle area
2.Circle area
3.Triangle area
4.Exit
Enter your choice:4
Exited

*/