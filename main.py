# main.py
from passenger_list import PassengerList
from luggage_queue import LuggageQueue
from boarding_stack import BoardingStack

# Main Function 
def main():

    # List of all passengers
    passengers = PassengerList()        
    # Queue for luggage
    luggage_queue = LuggageQueue()      
    # Stack for boarding
    boarding_stack = BoardingStack()     

    # Keep running until the user choos to exit
    while True:
        # Print the main menu
        print("\n=== Airplane Boarding Management System ===")
        print("1. Add Passenger")
        print("2. Remove Passenger")
        print("3. Update Passenger Seat")
        print("4. Display Passengers")
        print("5. Add Luggage")
        print("6. Unload Luggage")
        print("7. Display Luggage")
        print("8. Board Passenger")
        print("9. Exit Passenger")
        print("10. Display Boarded Passengers")
        print("0. Exit")

        # Input user choice
        choice = input("\nEnter your choice: ")

        # Handle each menu option
        
        if choice == '1':
            # Get passenger detail and add them
            name = input("Enter passenger name: ")
            # input seat number
            seat_number = int(input("Enter seat number: "))
            # check if this is a priority passenger
            is_priority = input("Is this a priority passenger? (y/n): ").lower() == 'y'
            # add the passenger
            passengers.add_passenger(name, seat_number, is_priority)

        elif choice == '2':
            # Remove a passenger
            seat_number = int(input("Enter seat number to remove: "))
            passengers.remove_passenger(seat_number)

        elif choice == '3':
            # Update a passenger seat
            old_seat = int(input("Enter current seat number: "))
            # new seat
            new_seat = int(input("Enter new seat number: "))
            # update passenger with new seat
            passengers.update_passenger(old_seat, new_seat)

        elif choice == '4':
            # Show all passenger
            passengers.display_passengers()

        elif choice == '5':
            # Add luggage for a passenger
            luggage_id = input("Enter luggage ID: ")
            # input seat number
            seat_number = int(input("Enter passenger seat number: "))
            # get that passenger by seat number
            passenger = passengers.get_passenger(seat_number)
            if passenger:
                # add the luggage
                if luggage_queue.add_luggage(luggage_id, seat_number):
                    passenger["luggage"].append(luggage_id)
            else:
                # passenger not found
                print("Passenger not found")

        elif choice == '6':
            # Unload luggage
            unloaded = luggage_queue.unload_luggage()
            if unloaded:
                # get passenger
                passenger = passengers.get_passenger(unloaded[1])
                if passenger and unloaded[0] in passenger["luggage"]:
                    # remove the luggage
                    passenger["luggage"].remove(unloaded[0])

        elif choice == '7':
            # Show all luggage
            luggage_queue.display_luggage()

        elif choice == '8':
            # Board a passenger by seat number
            seat_number = int(input("Enter seat number for boarding: "))
            # get passenger
            passenger = passengers.get_passenger(seat_number)
            if passenger:
                boarding_stack.board_passenger(passenger)
            else:
                # passenger not found
                print("Passenger not found")

        elif choice == '9':
            # Remove a passenger from the plane
            boarding_stack.exit_passenger()

        elif choice == '10':
            # Show all boarded passenger
            boarding_stack.display_boarded()

        elif choice == '0':
            # Exit the program
            print("Thank you for using the Airplane Boarding Management System!")
            break

        else:
            # Handle invalid choice
            print("Invalid choice please try again")

# Start the program 
# calling main function
if _name_ == "_main_":
    main()
