import Inventory

def view_inventory():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')

    # Display current inventory
    print('Current inventory:')
    for item in inventory:
        print(f'{item[0]} - {item[1]}')