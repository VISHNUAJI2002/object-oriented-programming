"""
Problem Statement:
Design a Python program to manage a hotel reservation system using classes and objects.
The system should maintain room details and booking information. Each room should have
a room number, room type, price per night, and availability status. A booking should
store guest name, room number, and number of nights. The program should allow multiple
rooms and multiple bookings, allocate rooms only if available, calculate total booking
cost, and update room availability accordingly. The program should accept all details
from the user and display confirmed booking details.
"""

class Room:
    def __init__(self, room_no, room_type, price_per_night):
        self.room_no = room_no
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

    def mark_booked(self):
        self.is_available = False


class Booking:
    def __init__(self, guest_name, room, nights):
        self.guest_name = guest_name
        self.room = room
        self.nights = nights

    def calculate_total_cost(self):
        return self.room.price_per_night * self.nights


rooms = []
bookings = []

room_count = int(input("Enter number of rooms: "))

for i in range(room_count):
    print(f"\nRoom {i + 1}")
    room_no = int(input("Enter room number: "))
    room_type = input("Enter room type: ")
    price = float(input("Enter price per night: "))

    rooms.append(Room(room_no, room_type, price))


booking_count = int(input("\nEnter number of booking requests: "))

for i in range(booking_count):
    print(f"\nBooking {i + 1}")
    guest_name = input("Enter guest name: ")
    room_no = int(input("Enter required room number: "))
    nights = int(input("Enter number of nights: "))

    selected_room = None
    for room in rooms:
        if room.room_no == room_no and room.is_available:
            selected_room = room
            break

    if selected_room:
        booking = Booking(guest_name, selected_room, nights)
        selected_room.mark_booked()
        bookings.append(booking)
        print("Booking confirmed")
    else:
        print("Room not available")


print("\n--- Confirmed Bookings ---")
for booking in bookings:
    print("\nGuest Name:", booking.guest_name)
    print("Room Number:", booking.room.room_no)
    print("Room Type:", booking.room.room_type)
    print("Total Cost:", booking.calculate_total_cost())


"""
Sample Output:

Enter number of rooms: 2

Room 1
Enter room number: 101
Enter room type: Deluxe
Enter price per night: 2500

Room 2
Enter room number: 102
Enter room type: Standard
Enter price per night: 1800

Enter number of booking requests: 2

Booking 1
Enter guest name: Rahul
Enter required room number: 101
Enter number of nights: 3
Booking confirmed

Booking 2
Enter guest name: Anu
Enter required room number: 101
Enter number of nights: 2
Room not available

--- Confirmed Bookings ---

Guest Name: Rahul
Room Number: 101
Room Type: Deluxe
Total Cost: 7500.0
"""
