"""
Problem Statement:
Design a Python program to manage a library system using inheritance.
Create a base class that stores common book details such as book ID and title.
Derive a class that adds author information, and further derive another class
that handles borrowing details. The program should accept details for multiple
books from the user and display complete borrowing information using multilevel
inheritance.
"""

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title


class AuthorBook(Book):
    def __init__(self, book_id, title, author):
        super().__init__(book_id, title)
        self.author = author


class BorrowedBook(AuthorBook):
    def __init__(self, book_id, title, author, borrower_name, days):
        super().__init__(book_id, title, author)
        self.borrower_name = borrower_name
        self.days = days

    def calculate_fine(self):
        if self.days > 14:
            return (self.days - 14) * 5
        return 0


books = []
n = int(input("Enter number of borrowed books: "))

for i in range(n):
    print(f"\nBook {i + 1}")
    book_id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    borrower = input("Enter borrower name: ")
    days = int(input("Enter number of days borrowed: "))

    books.append(BorrowedBook(book_id, title, author, borrower, days))


print("\n--- Borrowed Book Details ---")
for book in books:
    print("\nBook ID:", book.book_id)
    print("Title:", book.title)
    print("Author:", book.author)
    print("Borrower:", book.borrower_name)
    print("Fine Amount:", book.calculate_fine())


"""
Sample Output:

Enter number of borrowed books: 2

Book 1
Enter book ID: 201
Enter book title: Clean Code
Enter author name: Robert Martin
Enter borrower name: Arun
Enter number of days borrowed: 10

Book 2
Enter book ID: 202
Enter book title: Design Patterns
Enter author name: Erich Gamma
Enter borrower name: Meera
Enter number of days borrowed: 18

--- Borrowed Book Details ---

Book ID: 201
Title: Clean Code
Author: Robert Martin
Borrower: Arun
Fine Amount: 0

Book ID: 202
Title: Design Patterns
Author: Erich Gamma
Borrower: Meera
Fine Amount: 20
"""