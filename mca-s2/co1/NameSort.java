/*
Experiment 5:

String Handling Methods-2

Aim:
Write a Java program to
i. Check whether a given string is palindrome or not.(Check file PalindromeString.java)
ii. Sorting a given list of names in ascending order.
*/

import java.util.Scanner;

class NameSort{
    public static void main (String args[]){

        Scanner s=new Scanner(System.in);

        System.out.print("Enter list size:");
        int n=s.nextInt();
        s.nextLine();

        String names[] = new String[n];
        
        for (int i=0;i<n;i++){
            names[i]=s.nextLine();
        }

        for (int i=0;i<n-1;i++){
            for (int j=i+1;j<n;j++){
                if (names[i].compareToIgnoreCase(names[j])>0){
                    String temp = names[i];
                    names[i]=names[j];
                    names[j]=temp;
                }
            }
        }

        System.out.println("\nSorted list:");

        for (int i=0;i<n;i++){
            System.out.println(names[i]);
        }
    }
}

/*

Sample output:
   
Enter list size:5
allen
thomman
kunju
ashi
abhi

Sorted list:
abhi
allen
ashi
kunju
thomman
*/