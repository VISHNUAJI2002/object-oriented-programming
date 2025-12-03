/*
Experiment 5:

String Handling Methods-2

Aim:
Write a Java program to
i. Check whether a given string is palindrome or not.
ii. Sorting a given list of names in ascending order.(check file NameSort.java)
*/

import java.util.*;

class PalindromeString {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the string:");
        String s = sc.nextLine().toLowerCase();

        int left = 0;
        int right = s.length() - 1;
        boolean isPalindrome = true;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }

        if (isPalindrome) {
            System.out.println(s + " is palindrome.");
        } else {
            System.out.println(s + " is not palindrome.");
        }

        sc.close();
    }
}

/*
Sample Output:

Enter the string:malayalam
malayalam is palindrome.

*/