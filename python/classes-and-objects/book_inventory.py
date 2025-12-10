"""
Problem:
Create a Python class Book with attributes title, author, and price.
Read details of N books from the user, create Book objects, store them in a list,
and display the details of each book.

This program demonstrates:
- Class definition
- Constructor (__init__)
- Instance variables
- Instance methods
- Creating multiple objects
- Storing objects in a list
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print()


books = []

n = int(input("Enter number of books: "))

for i in range(n):
    print(f"\nEnter details of book {i+1}:")
    title = input("Title: ")
    author = input("Author: ")
    price = float(input("Price: "))

    obj = Book(title, author, price)
    books.append(obj)

print("\n--- Book Details ---")
for b in books:
    b.display()


"""
Sample Output:

Enter number of books: 2

Enter details of book 1:
Title: The Alchemist
Author: Paulo Coelho
Price: 499

Enter details of book 2:
Title: Atomic Habits
Author: James Clear
Price: 550

--- Book Details ---
Title: The Alchemist
Author: Paulo Coelho
Price: 499.0

Title: Atomic Habits
Author: James Clear
Price: 550.0
"""
