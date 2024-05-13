import csv

def import_inventory(file_name):

    # Read the data from the CSV file
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.DictReader(file)
            # initialise empty dictionary to store the row
            # the first row is the inventory to return
            for row in reader:
                print(f'row: {row}')
                return row
        print('Inventory imported successfully.')
    except FileNotFoundError:
        print('File not found. Creating now...')
        # creating empty file
        with open(file_name, 'w') as file: 
            print("Empty file created Successfully")
            pass 
        return dict()
    
def export_inventory(output_file_name, inventory):
    # Write the data to the CSV file
    try:
        with open(output_file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=list(inventory.keys()))
            # Write the header row (dictionary keys)
            writer.writeheader()
            # Write the dictionary row to the csv file
            writer.writerow(inventory)
        print('Inventory exported successfully.')
    except Exception as e:
        print(f'Error exporting inventory: {e}')

'''
How the inventory looks in two different formats

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