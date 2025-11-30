/*
Experiment 4

String Handling Methods- 1

Aim
Perform the following operations on strings
i. Find the length of the string
ii. Character at second and fourth position
iii. Find the sub string using start index only
iv. Find the sub string using start index and end index
v. Compare two strings lexicographically.
vi. Compare two strings lexicographically, ignoring case differences.
vii. Concatenate a given string to the end of another string.
viii. Replace a specified character with another character.
ix. Check whether a given string starts with another string.
x. Convert all characters in a string to lowercase
xii. Convert all characters in a string to uppercase.
*/

import java.util.Scanner;
public class StringOperations {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        // i. Find the length of the string
        System.out.println("length of a string.");

        System.out.print("Enter a string: ");
        String str = s.nextLine();
        System.out.println("Length of string: " + str.length());
        System.out.println();

        // ii. Character at second and fourth position
        System.out.println("Character at second and fourth position.");

        System.out.println("Character at second position: " + (str.length() > 1 ? str.charAt(1) :"Nil"));
        System.out.println("Character at fourth position: " + (str.length() > 3 ? str.charAt(3) :"Nil"));
        System.out.println();

        // iii. Find the substring using start index only
        System.out.println("substring using start index only.");

        System.out.print("Enter the starting index: ");
        int i=s.nextInt();
        System.out.println("Substring from starting index : "+str.substring(i));
        System.out.println();

        // iv. Find the substring using start index and end index
        System.out.println("substring using start index and end index.");

        System.out.print("Enter the start index and the end index: ");
        int st = s.nextInt();
        int e = s.nextInt();
        System.out.println("Substring from index "+st+" to index "+e+ ": "+str.substring(st,e));
        System.out.println();

        // v. Compare two strings lexicographically
        System.out.println("Compare two strings lexicographically.");

        s.nextLine();
        System.out.print("Enter the String 1: ");
        String str1 = s.nextLine();
        System.out.print("Enter the String 2: ");
        String str2 = s.nextLine();

        int result = str1.compareTo(str2);
        if (result == 0) {
            System.out.println("Both Strings are equal .");
        } 
        else if (result < 0) {
            System.out.println("String 1 is less than String 2.");
        } 
        else {
            System.out.println("String 1 is greater than String 2.");
        }
        System.out.println();    

        // vi. Compare two strings lexicographically, ignoring case differences
        System.out.println("Compare two strings lexicographically, ignoring case differences.");

        int result1 = str1.compareToIgnoreCase(str2);
        if (result1 == 0) {
            System.out.println("Both Strings are equal (ignoring case).");
        } 
        else if (result1 < 0) {
            System.out.println("String1 is less than String2 (ignoring case).");
        } 
        else {
            System.out.println("String1 is greater than String2 (ignoring case).");
        }
        System.out.println();

        // vii. Concatenate a given string to the end of another string
        System.out.println("Concatenate a given string to the end of another string.");

        System.out.print("Enter a string s1:");
        String s1 = s.nextLine();

        System.out.print("Enter a string s2 to concatenate with s1: ");
        String s2 = s.nextLine();

        String s3 = s1.concat(s2);
        System.out.println("Concatenated String is : " + s3);
        System.out.println();

        // viii. Replace a specified character with another character
        System.out.println("Replace a specified character with another character.");

        System.out.print("Enter a string:");
        String s4=s.nextLine(); 

        System.out.print("Enter the character to be replaced: ");
        char c = s.next().charAt(0);

        System.out.print("Enter the character to replace with: ");
        char r = s.next().charAt(0);

        String modifieds4 = s4.replace(c, r);
        System.out.println("Modified string: " + modifieds4);
        System.out.println();

        // ix. Check whether a given string starts with another string
        System.out.println("Check whether a given string starts with another string");

        s.nextLine();
        System.out.print("Enter the string to check if it starts with "+str+":");
        String s5 = s.nextLine();
        System.out.println(str.startsWith(s5) ? "The string starts with the given string." : "The string does not start with the given string.");
        System.out.println();

        // x. Convert all characters in a string to lowercase
        System.out.println(" Convert all characters in a string to lowercase.");

        System.out.println("String "+str+" in lowercase: " + str.toLowerCase());
        System.out.println();

        // xi. Convert all characters in a string to uppercase
        System.out.println("Convert all characters in a string to uppercase.");

        System.out.println("String  "+str+" in uppercase: " + str.toUpperCase());
        System.out.println();   
    }
}

/*
Sample Output:

length of a string.
Enter a string: Vishnu
Length of string: 6

Character at second and fourth position.
Character at second position: i
Character at fourth position: h

substring using start index only.
Enter the starting index: 2
Substring from starting index : shnu

substring using start index and end index.
Enter the start index and the end index: 1 4
Substring from index 1 to index 4: ish

Compare two strings lexicographically.
Enter the String 1: Hello
Enter the String 2: World
String 1 is less than String 2.

Compare two strings lexicographically, ignoring case differences.
String1 is less than String2 (ignoring case).

Concatenate a given string to the end of another string.
Enter a string s1:Good
Enter a string s2 to concatenate with s1: Morning
Concatenated String is : GoodMorning

Replace a specified character with another character.
Enter a string:Java
Enter the character to be replaced: J 
Enter the character to replace with: m
Modified string: mava

Check whether a given string starts with another string
Enter the string to check if it starts with Vishnu:Vis 
The string starts with the given string.

 Convert all characters in a string to lowercase.
String Vishnu in lowercase: vishnu

Convert all characters in a string to uppercase.
String  Vishnu in uppercase: VISHNU
*/