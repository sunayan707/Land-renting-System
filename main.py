import operation  # Importing functions related to land operations from operation.py

def print_menu():
    """
    Function to print the menu options for the user.
    """
    print("\nWelcome to TechnoPropertyNepal Land Renting System")
    print("1. Display available lands")
    print("2. Rent land")
    print("3. Return land")
    print("4. Exit")

def main():
    """
    Main function to run the land renting system.
    """
    try:
        while True:
            print_menu()  # Display the menu options
            choice = input("Enter the number corresponding to your choice: ")  # Prompt user for choice

            if choice == '1':
                operation.display_available_lands()  # Call function to display available lands
            elif choice == '2':
                operation.rent_land()  # Call function to rent a land
            elif choice == '3':
                operation.return_land()  # Call function to return a rented land
            elif choice == '4':
                print("Thank you for using TechnoPropertyNepal Land Renting System")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    except KeyboardInterrupt:
        print("\nExiting the program.")  # Handle keyboard interrupt gracefully
    except Exception as e:
        print("An error occurred:", str(e))  # Catch and display any other exceptions

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly

