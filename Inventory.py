import csv

def import_inventory(file_name):

    # Read the data from the CSV file
    try:
        # Read the data from the CSV file
        with open(file_name, 'r', newline='') as file:
            inventory = []
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append(row)
        return inventory
    except FileNotFoundError:
        print('File not found. Creating now...')
        # creating empty file
        with open(file_name, 'w') as file: 
            print("Empty file created Successfully")
        return []
    
def export_inventory(output_file_name, inventory):
    # Write the data to the CSV file
    try:

        fieldnames = ['name', 'price', 'quantity']

        with open(output_file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Write the header row (dictionary keys)
            writer.writeheader()
            # Write the dictionary row to the csv file
            writer.writerows(inventory)
        print('Inventory exported successfully.')
    except Exception as e:
        print(f'\033[91mError exporting inventory: {e}\033[0m')

'''
How the inventory looks in two different formats

NEW ------------------------

List of Dictionaries:
[
    {
        'name': 'iPhone'
        'price': '999',
        'quantity': '200'
    },
    {
        'name': 'iPad'
        'price': '500',
        'quantity': '100'
    },
    {
        'name': 'mac'
        'price': '2000',
        'quantity': '50'
    }
]

CSV:
name,price,quantity
iPhone,999,200
iPad,500,100
mac,2000,50

OLD ------------------------
Dictionary:
{
    iPhone: 100
    iPad: 20
    mac: 30
}

CSV:
iPhone, iPad, mac
100, 20, 30

'''