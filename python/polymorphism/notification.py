"""
Problem:
Write a Python program to demonstrate runtime polymorphism using method overriding.
Create a base class Notification with a method send().
Derive classes EmailNotification and SMSNotification that override the send() method.
Read N notifications from the user and display how each notification is sent.

This program demonstrates:
- Polymorphism
- Method overriding
- Runtime method resolution
"""

class Notification:
    def send(self,message):
        print("Sending notification: ",message)

class EmailNotification(Notification):
    def send(self,message):
        print("Sending email notification: ",message)

class SMSNotification(Notification):
    def send(self,message):
        print("Sending SMS notification: ",message)

notifications=[]

n=int(input("Enter number of notifications:"))\

for i in range(n):
    print(f"\nNotification {i+1}")
    print("1.Email\n2.SMS")
    choice=int(input("Enter your choice: "))

    message=input("Enter message: ")

    if choice==1:
        notifications.append(EmailNotification())
    elif choice==2:
        notifications.append(SMSNotification())
    else:
        print("Invalid choice. Using default notification")
        notifications.append(Notification())

    notifications[-1].send(message)      
              
        
'''
Enter number of notifications:3

Notification 1
1.Email
2.SMS
Enter your choice: 1
Enter message: Hello
Sending email notification:  Hello

Notification 2
1.Email
2.SMS
Enter your choice: 2    
Enter message: Good morning
Sending SMS notification:  Good morning

Notification 3
1.Email
2.SMS
Enter your choice: 5
Enter message: Welcome
Invalid choice. Using default notification
Sending notification:  Welcome
'''        