"""
Problem:
Write a Python program to demonstrate classes and objects using a Library system.
Create a class Book with attributes book_id, title, author, and copies.
Provide methods to:
 - display book details
 - issue a book (reduce copies)
 - return a book (increase copies)

Read details of N books from the user and perform issue/return operations.
"""

class Book:
    def __init__(self,book_id,title,author,copies):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.copies=copies

    def display(self):
        print(f"\nBook ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available copies: {self.copies}")

    def issue_book(self):
        if self.copies>0:
            self.copies-=1
            print("Book issued Successfully.")
        else:
            print("No copies available!")

    def return_book(self):
        self.copies+=1
        print("Book returned successfully.")

books=[]
n=int(input("Enter number of books: "))

for i in range(n):
    print(f"\nEnter details of book {i+1}")
    id=int(input("Book Id: "))
    title=input("Title: ")
    author=input("Author: ")
    copies=int(input("No. of copies: "))

    books.append(Book(id,title,author,copies))

while True:
    print("\n---Library meny---")
    print("1. Display all books")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        print("\n---Book Details---")
        for i in books:
            i.display()
        print("----------------")            

    elif choice==2:
        bid=int(input("Enter Book ID to issue: "))
        for i in books:
            if i.book_id==bid:
                i.issue_book()
                break
        else:
            print("Book not found!")

    elif choice==3:
        bid=int(input("Enter Book ID to return: "))                
        for i in books:
            if i.book_id==bid:
                i.return_book()
                break
        else:
            print("Book not found!")

    elif choice==4:
        print("Exiting")
        break
    else:
        print("Envalid Entry, Try again.")            

'''
Sample Outout:

Enter number of books: 2

Enter details of book 1
Book Id: 101
Title: Optics
Author: Newton
No. of copies: 55

Enter details of book 2
Book Id: 102
Title: Quantum Entaglement
Author: Heisenberg & Dirac
No. of copies: 36

---Library meny---
1. Display all books
2. Issue a book
3. Return a book
4. Exit
Enter your choice: 1

---Book Details---

Book ID: 101
Title: Optics
Author: Newton
Available copies: 55

Book ID: 102
Title: Quantum Entaglement
Author: Heisenberg & Dirac
Available copies: 36
----------------

---Library meny---
1. Display all books
2. Issue a book
3. Return a book
4. Exit
Enter your choice: 2
Enter Book ID to issue: 101
Book issued Successfully.

---Library meny---
1. Display all books
2. Issue a book
3. Return a book
4. Exit
Enter your choice: 3
Enter Book ID to return: 101
Book returned successfully.

---Library meny---
1. Display all books
2. Issue a book
3. Return a book
4. Exit
Enter your choice: 4
Exiting
'''