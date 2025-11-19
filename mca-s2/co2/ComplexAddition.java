/*
Experiment 10:
Complex number addition.
Aim: Write a Java program to add to complex numbers using object as argument
*/

import java.util.Scanner;
class Complex {
    int real;
    int imag;
    Complex(int r, int i) {
        real = r;
        imag = i;
    }
    void addNumber(Complex other) {
        int real1 = real + other.real;
        int imag1 = imag + other.imag;
        System.out.println(real1 + " + " + imag1 + "i");
    }
    void display() {
        System.out.println(real + " + " + imag + "i");
    }
}

public class ComplexAddition {
    public static void main(String args[]) {
        int a1, a2, b1, b2;
        Scanner s1 = new Scanner(System.in);

        System.out.println("First Complex number");
        System.out.println("Enter complex parts:");
        a1 = s1.nextInt();
        System.out.println("Enter imaginary parts:");
        b1 = s1.nextInt();
        Complex c1 = new Complex(a1, b1);

        System.out.println("Second Complex number");
        System.out.println("Enter complex parts:");
        a2 = s1.nextInt();
        System.out.println("Enter imaginary parts:");
        b2 = s1.nextInt();
        Complex c2 = new Complex(a2, b2);

        System.out.println("First Complex Number");
        c1.display();
        System.out.println("Second Complex Number");
        c2.display();
        System.out.println("Complex number addition");
        c1.addNumber(c2);
    }
}

/*
Sample Output:
PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co2> java ComplexAddition
First Complex number
Enter complex parts:
3
Enter imaginary parts:
5
Second Complex number
Enter complex parts:
4
Enter imaginary parts:
11
First Complex Number
3 + 5i
Second Complex Number
4 + 11i
Complex number addition
7 + 16i
*/