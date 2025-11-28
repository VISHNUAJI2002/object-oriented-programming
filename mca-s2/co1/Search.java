/*
Experiment 2

One-Dimensional Array

Aim: Write a Java program to search an element in an array/
*/

import java.util.Scanner;

class Search{
    public static void main(String args[]){
        int a[]=new int[args.length];

        for (int i=0;i<args.length;i++){
            a[i]=Integer.parseInt(args[i]);
        }

        Scanner s=new Scanner(System.in);

        System.out.print("Enter element to search:");
        int num=s.nextInt();

        boolean found=false;

        for (int i=0;i<a.length;i++){
            if (a[i]==num){
                System.out.println(num+" is found at index "+i);
                found=true;
                break;
            }
        }

        if (!found){
            System.out.print("element "+num+" is not found in the array");
        }
    }
}

/*
Sample Output:

PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co1> java Search 5 10 15 20 25
Enter element to search:20
20 is found at index 3

*/