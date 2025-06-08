
def read_lands():
    with open('land.txt', 'r') as file:
        lines = file.readlines()
        lands = []
        for line in lines:
            data = line.strip().split(', ')
            if len(data) == 6:  # Ensure all fields are present
                land_info = {
                    'Kitta': data[0],
                    'City/District': data[1],
                    'Direction': data[2],
                    'Area': data[3],
                    'Price': data[4],
                    'Status': data[5]  # Status is the last item
                }
                lands.append(land_info)
            else:
                print("Invalid data format:", line)
        return lands


def display_available_lands():
    lands = read_lands()
    available_lands = [land for land in lands if land['Status'] == 'Available']
    print("Available Lands:")
    for land in available_lands:
        print(land)

def get_rent_info_by_kitta(kitta_number):
    try:
        with open('rental_info.txt', 'r') as file:  # Assuming rental information is stored in 'rental_info.txt'
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(', ')
                if data[0] == kitta_number:
                    rent_info = {
                        'Kitta': data[0],
                        'Name': data[1],
                        'Rent Date': data[2],  # No need to parse 'Rent Date' since it's stored as a string
                        'Rent Duration': int(data[3])
                    }
                    return rent_info
        return None  # Return None if rental information not found
    except FileNotFoundError:
        print("Error: File 'rental_info.txt' not found.")
    except Exception as e:
        print("An error occurred:", str(e))
        return None