/*
Experiment 8 :

Initialize instance variables inside the class using constructor

Aim
Program to demonstrate use of constructors to initialize values to member
variables in a class and to display them.

Hint:- empno , empname and salary are the class members of the class
employee1. From the main function we are passing the values directly to a
constructor, the constructor initializes the values to member variables. The display
function is used to display the stored values of the member variables.
*/

import java.util.Scanner;

class Emp{
    int empno,salary;
    String name;
    Emp(int eno, String ename, int esal){
        empno=eno;
        name=ename;
        salary=esal;
    }
    void display(){
        System.out.println("Employee Number:"+empno);
        System.out.println("Name:"+name);
        System.out.println("Salary:"+salary);
    }

    public static void main (String args[]){
        Scanner s=new Scanner(System.in);
        System.out.print("Enter employee no.:");
        int eno=s.nextInt();
        s.nextLine();
        System.out.print("Enter employee name:");
        String ename=s.nextLine();
        System.out.print("Enter employee salary:");
        int esal=s.nextInt();

        Emp e=new Emp(eno,ename,esal);
        e.display();
    }
}

/*
Sample Output:

PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co2> java Emp
Enter employee no.:10
Enter employee name:vishnu
Enter employee salary:85000
Employee Number:10
Name:vishnu
Salary:85000
*/