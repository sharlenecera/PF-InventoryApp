import Inventory

def view_inventory():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')
    if inventory is None:
        print('Inventory is empty.')
        return

    # Display current inventory
    print('Current inventory:')
    try:
        for item, quantity in inventory:
            print(f'{item}: {quantity}')
    except TypeError as error:
        print(f'{error}: Inventory is empty.')