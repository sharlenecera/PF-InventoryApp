import Inventory

def view_inventory():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')
    if inventory is None:
        print('\033[91mInventory is empty.\033[0m')
        return

    
    try:
        # Display current inventory
        print('Current inventory:')
        for item, quantity in inventory.items():
            print(f'{item}: {quantity}')
    except TypeError as error:
        print(f'{error}: Inventory is empty.')
    except Exception as e:
        print(f'Error: {e}')