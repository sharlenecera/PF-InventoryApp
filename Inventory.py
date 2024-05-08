import csv

def import_inventory(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            inventory = list(reader)
        return inventory
    except FileNotFoundError:
        print('File not found. Creating now...')
        return []
    
def export_inventory(file_name, inventory):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(inventory)
        print('Inventory exported successfully.')
    except Exception as e:
        print(f'Error exporting inventory: {e}')