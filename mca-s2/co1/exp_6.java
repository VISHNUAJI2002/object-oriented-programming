/*
Experiment 6:

StringBuffer Class Methods

Aim
Write a program in java for string handling which performs the following
i. Check the capacity of the StringBuffer object.
ii. Reverse the content of this string and convert the resultant string in upper case
iii. Read another string and append it to the resultant string of above.
*/

import java.util.Scanner;

class StrBuffer {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        // i. Check the capacity of the StringBuffer object
        System.out.print("Enter a string:");
        String str = sc.nextLine();
        StringBuffer s = new StringBuffer(str);
        int capacity = s.capacity();
        System.out.println("Capacity is: " + capacity);

        // ii. Reverse the content and convert to uppercase
        s.reverse();
        String res = s.toString().toUpperCase();
        System.out.println("After reversing and converting to uppercase: " + res);

        // iii. Read another string and append it
        System.out.print("Enter a string to append:");
        String appStr = sc.nextLine();

        String result = res + appStr;
        System.out.println("New String is: " + result);

        sc.close();
    }
}

/*
Sample Output:

Enter a string:hello
Capacity is: 21
After reversing and converting to uppercase: OLLEH
Enter a string to append:world
New String is: OLLEHworld
*/