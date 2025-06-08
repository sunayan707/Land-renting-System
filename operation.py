import read  # Importing functions for reading data from read.py
import write  # Importing functions for writing data from write.py
import datetime  # Importing datetime module for date-related operations

def display_available_lands():
    """
    Function to display available lands by reading land information from a file.
    """
    try:
        lands = read.read_lands()  # Read land information from file
        available_lands = [land for land in lands if land['Status'] == 'Available']  # Filter available lands
        if available_lands:
            print("Available Lands:")
            for land in available_lands:
                print(land)  # Print details of available lands
        else:
            print("No lands available for rent.")
    except FileNotFoundError:
        print("Error: File 'land.txt' not found.")
    except Exception as e:
        print("An error occurred:", str(e))

def rent_land():
    """
    Function to rent a land.
    """
    try:
        lands = read.read_lands()  # Read land information from file
        read.display_available_lands()  # Display available lands
        kitta_number = input("Enter the kitta number of the land you want to rent: ")

        land = next((land for land in lands if land['Kitta'] == kitta_number), None)  # Find land by kitta number
        if land is None:
            print("Invalid kitta number. Please try again.")
            return

        if land['Status'] != 'Available':
            print("Land is not available for rent.")
            return

        name = input("Enter your name: ")  # Get renter's name
        while True:
            try:
                rent_duration = int(input("Enter the duration of rent (in months): "))  # Get rent duration
                if rent_duration <= 0:
                    raise ValueError("Rent duration must be a positive integer.")
                break
            except ValueError as ve:
                print("Error:", str(ve))

        rent_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current date
        total_amount = int(land['Price']) * rent_duration  # Calculate total rent amount
        invoice_info = {
            'Kitta': land['Kitta'],
            'City/District': land['City/District'],
            'Direction': land['Direction'],
            'Area': land['Area'],
            'Name': name,
            'Rent Date': rent_date,
            'Rent Duration': rent_duration,
            'Total Amount': total_amount
        }
        write.generate_invoice(invoice_info, action='rent')  # Generate invoice for rent
        write.store_rent_info(invoice_info)  # Store rental information
        land['Status'] = 'Not Available'  # Update land status
        write.write_lands(lands)  # Write updated land information to file
        print("Land rented successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

# Function to return a rented land is similar in structure, so detailed comments are omitted

def return_land():
    """
    Function to return a rented land.
    """
    try:
        kitta_number = input("Enter the kitta number of the land you want to return: ")

        lands = read.read_lands()
        land = next((land for land in lands if land['Kitta'] == kitta_number), None)
        if land is None or land['Status'] != 'Not Available':
            print("Invalid kitta number. Please try again.")
            return

        rent_info = read.get_rent_info_by_kitta(kitta_number)
        if rent_info:
            name = rent_info['Name']
            rent_date_str = rent_info['Rent Date']
            rent_date = datetime.datetime.strptime(rent_date_str, "%Y-%m-%d %H:%M:%S")
            rent_duration = rent_info['Rent Duration']
            
            while True:
                try:
                    rented_months = int(input("Enter the duration of months the land was rented: "))
                    if rented_months < 0:
                        raise ValueError("Rented months cannot be negative.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")
            return_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")            

            # Check if the return is late
            if rented_months > rent_duration:
                late_months = rented_months - rent_duration
                fine_amount = late_months * 1000
            else:
                late_months = 0
                fine_amount = 0

            # Calculate total amount to be paid
            total_amount = int(land['Price']) * rent_duration + fine_amount

            invoice_info = {
                'Kitta': land['Kitta'],
                'City/District': land['City/District'],
                'Direction': land['Direction'],
                'Area': land['Area'],
                'Name': name,
                'Return Date': return_date,
                'Rent Duration': rent_duration,
                'Rented Months': rented_months,
                'Late Months': late_months,
                'Fine Amount': fine_amount,
                'Total Amount': total_amount
            }
            write.generate_invoice(invoice_info, action='return')
            write.remove_rent_info(kitta_number)  # Remove rental information
            land['Status'] = 'Available'
            write.write_lands(lands)
            print("Land returned successfully.")
            
        else:
            print("No rental information found for this land.")     
    except Exception as e:
        print("An error occurred:", str(e))
