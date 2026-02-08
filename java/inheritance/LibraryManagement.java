/*
Problem Statement:
Design a Java program to manage a library system using inheritance.
Create a base class that stores common book details such as book ID and title.
Derive a class that adds author information, and further derive another class
that manages book issue details. The program should accept details for multiple
issued books from the user and display complete book and issue information
using multilevel inheritance.
*/

import java.util.Scanner;

class Book {
    protected int bookId;
    protected String title;

    public Book(int bookId, String title) {
        this.bookId = bookId;
        this.title = title;
    }
}

class AuthorBook extends Book {
    protected String author;

    public AuthorBook(int bookId, String title, String author) {
        super(bookId, title);
        this.author = author;
    }
}

class IssuedBook extends AuthorBook {
    private String issuedTo;
    private int days;

    public IssuedBook(int bookId, String title, String author, String issuedTo, int days) {
        super(bookId, title, author);
        this.issuedTo = issuedTo;
        this.days = days;
    }

    public int calculateFine() {
        if (days > 14) {
            return (days - 14) * 5;
        }
        return 0;
    }

    public void displayDetails() {
        System.out.println("Book ID: " + bookId);
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Issued To: " + issuedTo);
        System.out.println("Fine Amount: " + calculateFine());
    }
}

public class LibraryManagement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of issued books: ");
        int n = sc.nextInt();

        IssuedBook[] books = new IssuedBook[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nBook " + (i + 1));
            System.out.print("Enter book ID: ");
            int id = sc.nextInt();
            sc.nextLine();

            System.out.print("Enter book title: ");
            String title = sc.nextLine();

            System.out.print("Enter author name: ");
            String author = sc.nextLine();

            System.out.print("Enter issued to: ");
            String issuedTo = sc.nextLine();

            System.out.print("Enter number of days issued: ");
            int days = sc.nextInt();

            books[i] = new IssuedBook(id, title, author, issuedTo, days);
        }

        System.out.println("\n--- Issued Book Details ---");
        for (IssuedBook book : books) {
            System.out.println();
            book.displayDetails();
        }

        sc.close();
    }
}

/*
Sample Output:

Enter number of issued books: 2

Book 1
Enter book ID: 101
Enter book title: Clean Code
Enter author name: Robert Martin
Enter issued to: Arun
Enter number of days issued: 10

Book 2
Enter book ID: 102
Enter book title: Design Patterns
Enter author name: Erich Gamma
Enter issued to: Meera
Enter number of days issued: 20

--- Issued Book Details ---

Book ID: 101
Title: Clean Code
Author: Robert Martin
Issued To: Arun
Fine Amount: 0

Book ID: 102
Title: Design Patterns
Author: Erich Gamma
Issued To: Meera
Fine Amount: 30
*/
