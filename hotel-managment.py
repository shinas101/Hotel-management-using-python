# Hotel Management System

# Define a Room class to store room details
class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.available = True  # Initially, room is available

    def update_room(self, room_type, price_per_night):
        self.room_type = room_type
        self.price_per_night = price_per_night
        print(f"Room {self.room_number} updated successfully!")

    def check_availability(self):
        return self.available


# Define a Booking class to handle guest bookings and invoice creation
class Booking:
    def __init__(self, guest_name, room, duration, discount=0):
        self.guest_name = guest_name
        self.room = room
        self.duration = duration
        self.discount = discount
        self.total_amount = 0
        self.invoice = None

    def calculate_bill(self):
        # Calculate total bill
        self.total_amount = self.room.price_per_night * self.duration
        # Apply discount if applicable
        if self.discount > 0:
            discount_amount = (self.total_amount * self.discount) / 100
            self.total_amount -= discount_amount
        return self.total_amount

    def generate_invoice(self):
        # Generate invoice for the guest
        self.invoice = {
            "Guest Name": self.guest_name,
            "Room Number": self.room.room_number,
            "Room Type": self.room.room_type,
            "Duration": self.duration,
            "Total Bill": self.total_amount,
            "Discount": self.discount
        }

    def show_invoice(self):
        # Display invoice
        if self.invoice:
            print("\nInvoice Details:")
            for key, value in self.invoice.items():
                print(f"{key}: {value}")
        else:
            print("No invoice generated yet.")


# Function to add a new room
def add_room(room_list):
    room_number = int(input("Enter room number: "))
    room_type = input("Enter room type (Ac/Non-Ac/Suite): ")
    price_per_night = float(input("Enter price per night: "))
    new_room = Room(room_number, room_type, price_per_night)
    room_list.append(new_room)
    print(f"Room {room_number} added successfully!")


# Function to update room details
def update_room_details(room_list):
    room_number = int(input("Enter the room number to update: "))
    for room in room_list:
        if room.room_number == room_number:
            room_type = input("Enter new room type (Ac/Non-Ac/Suite): ")
            price_per_night = float(input("Enter new price per night: "))
            room.update_room(room_type, price_per_night)
            return
    print(f"Room {room_number} not found!")


# Function to check room availability
def check_room_availability(room_list):
    for room in room_list:
        if room.check_availability():
            print(f"Room no : {room.room_number}/{room.room_type}/{room.price_per_night}/(available)")
        else:
            print(f"Room no : {room.room_number}/{room.room_type}/{room.price_per_night}/(not-available)")
    # room_number = int(input("Enter room number to check availability: "))
    # for room in room_list:
    #     if room.room_number == room_number:
    #         if room.check_availability():
    #             print(f"Room {room_number} is available.")
    #             return True
    #         else:
    #             print(f"Room {room_number} is not available.")
    #             return False
    # print(f"Room {room_number} not found!")
    return False


# Function to book a room
def book_room(room_list):
    guest_name = input("Enter guest name: ")
    room_number = int(input("Enter room number to book: "))
    duration = int(input("Enter number of nights: "))
    discount_input = input("Enter discount percentage (if any, else press Enter): ")
    discount = float(discount_input) if discount_input else 0.0
    for room in room_list:
        if room.room_number == room_number:
            if room.check_availability():
                room.available = False  # Mark room as booked
                booking = Booking(guest_name, room, duration, discount)
                total_amount = booking.calculate_bill()
                booking.generate_invoice()
                print(f"Booking successful for {guest_name} in Room {room_number} for {duration} nights.")
                booking.show_invoice()
                return booking
            else:
                print(f"Room {room_number} is already booked.")
                return None
    print(f"Room {room_number} not found!")
    return None


# Function to check-in a guest
def check_in(booking):
    if booking:
        print(f"Guest {booking.guest_name} has checked in successfully!")
    else:
        print("No booking found to check in.")


# Function to check-out a guest
def check_out(booking,room_list):
    for room in room_list:
        if room.check_availability():
            pass
        else:
            print(f"{booking.guest_name} - {room.room_number} - {room.room_type}")
    choice = int(input("Enter room number : "))
    for room in room_list:
        if choice == room.room_number:
            booking.room.available = True
            print(f"Guest {booking.guest_name} has checked out successfully!")
            booking.generate_invoice()
            booking.show_invoice()
    
    # if booking:
    #     booking.room.available = True  # Mark room as available after check-out
    #     print(f"Guest {booking.guest_name} has checked out successfully!")
    # else:
    #     print("No booking found to check out.")


# Main program to test the system
if __name__ == "__main__":
    # List to store all rooms in the hotel
    room_list = []
    new_room = Room(1, 'Ac', 2000)
    room_list.append(new_room)
    new_room = Room(2, 'Non-Ac', 1200)
    room_list.append(new_room)
    new_room = Room(3, 'Suite', 3500)
    room_list.append(new_room)
    while True:
        print("\nHotel Management System")
        print("1. Add Room")
        print("2. Update Room Details")
        print("3. Check Room Availability")
        print("4. Book Room")
        # print("5. Check-In Guest")
        print("5. Check-Out Guest")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_room(room_list)
        elif choice == "2":
            update_room_details(room_list)
        elif choice == "3":
            check_room_availability(room_list)
        elif choice == "4":
            booking = book_room(room_list)
        elif choice == "500":
            if 'booking' in locals():
                check_in(booking)
            else:
                print("No booking found to check in.")
        elif choice == "5":
            if 'booking' in locals():
                check_out(booking,room_list)
            else:
                print("No booking found to check out.")
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
