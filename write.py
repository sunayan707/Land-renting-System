def write_lands(lands):
    """
    Function to write land information to a file.
    """
    with open('land.txt', 'w') as file:
        for land in lands:
            line = ', '.join([str(land[key]) for key in land])  # Convert land information to comma-separated string
            file.write(line + '\n')  # Write land information to the file

def generate_invoice(invoice_info, action):
    """
    Function to generate an invoice and write it to a file.
    """
    filename = f"{action}_invoice_{invoice_info['Name']}.txt"  # Generate filename for the invoice
    with open(filename, 'a') as file:
        if action == 'rent':
            file.write("Rent Invoice\n")
            file.write("--------------\n")
            file.write(f"{'Kitta':<15}{'City/District':<20}{'Direction':<20}{'Area':<10}{'Name':<15}{'Rent Date':<20}{'Rent Duration':<15}{'Total Amount':<15}\n")
            file.write("-" * 120 + '\n')
            file.write(f"{invoice_info['Kitta']:<15}{invoice_info['City/District']:<20}{invoice_info['Direction']:<20}{invoice_info['Area']:<10}{invoice_info['Name']:<15}{invoice_info['Rent Date']:<20}{invoice_info['Rent Duration']: <15}NPR {invoice_info['Total Amount']: <15}\n")
        elif action == 'return':
            file.write("Return Invoice\n")
            file.write("--------------\n")
            file.write(f"{'Kitta':<15}{'City/District':<20}{'Direction':<20}{'Area':<10}{'Name':<15}{'Return Date':<20}{'Rent Duration':<15}{'Rented Months':<15}{'Late Months':<15}{'Fine Amount':<15}{'Total Amount':<15}\n")
            file.write("-" * 150 + '\n')
            file.write(f"{invoice_info['Kitta']:<15}{invoice_info['City/District']:<20}{invoice_info['Direction']:<20}{invoice_info['Area']:<10}{invoice_info['Name']:<15}{invoice_info['Return Date']:<20}{invoice_info['Rent Duration']:<15}{invoice_info['Rented Months']:<15}{invoice_info['Late Months']:<15}NPR {invoice_info['Fine Amount']:<15}NPR {invoice_info['Total Amount']:<15}\n")

def store_rent_info(invoice_info):
    """
    Function to store rental information in a file.
    """
    with open('rental_info.txt', 'a') as file:
        file.write(f"{invoice_info['Kitta']}, {invoice_info['Name']}, {invoice_info['Rent Date']}, {invoice_info['Rent Duration']}\n")

def remove_rent_info(kitta_number):
    """
    Function to remove rental information from a file.
    """
    try:
        with open('rental_info.txt', 'r') as file:
            lines = file.readlines()  # Read all lines from the file
        with open('rental_info.txt', 'w') as file:
            for line in lines:
                if not line.startswith(kitta_number):  # Skip line with specified kitta number
                    file.write(line)  # Write remaining lines back to the file
    except FileNotFoundError:
        pass  # Ignore file not found error
