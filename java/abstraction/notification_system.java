/*
Problem Statement:
Design a Java program to demonstrate abstraction using a notification system.
Create an abstract class that defines a method for sending notifications.
Different notification types such as Email, SMS, and Push Notification
should implement this method with their own behavior. The program should
accept multiple notification requests from the user and display how each
notification is sent.
*/

import java.util.Scanner;

abstract class Notification {
    abstract void sendNotification(String message);
}

class EmailNotification extends Notification {
    @Override
    void sendNotification(String message) {
        System.out.println("Email sent with message: " + message);
    }
}

class SMSNotification extends Notification {
    @Override
    void sendNotification(String message) {
        System.out.println("SMS sent with message: " + message);
    }
}

class PushNotification extends Notification {
    @Override
    void sendNotification(String message) {
        System.out.println("Push notification sent with message: " + message);
    }
}

public class notification_system {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of notifications: ");
        int n = sc.nextInt();
        sc.nextLine();

        Notification[] notifications = new Notification[n];
        String[] messages = new String[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nNotification " + (i + 1));
            System.out.print("Enter type (email/sms/push): ");
            String type = sc.nextLine();

            System.out.print("Enter message: ");
            String message = sc.nextLine();
            messages[i] = message;

            if (type.equalsIgnoreCase("email")) {
                notifications[i] = new EmailNotification();
            } 
            else if (type.equalsIgnoreCase("sms")) {
                notifications[i] = new SMSNotification();
            } 
            else if (type.equalsIgnoreCase("push")) {
                notifications[i] = new PushNotification();
            }
            else {
                System.out.println("Invalid notification type. Please try again.");
                i--; 
            }
        }

        System.out.println("\n--- Sending Notifications ---");

        for (int i = 0; i < n; i++) {
            notifications[i].sendNotification(messages[i]);
        }

        sc.close();
    }
}

/*
Sample Output:

Enter number of notifications: 2

Notification 1
Enter type (email/sms/push): email
Enter message: Welcome to the platform

Notification 2
Enter type (email/sms/push): sms
Enter message: Your OTP is 2451

--- Sending Notifications ---
Email sent with message: Welcome to the platform
SMS sent with message: Your OTP is 2451
*/