import Inventory

def view_inventory():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')
    if not inventory:
        print('\033[91mInventory is empty.\033[0m')
        return

    try:
        # Display current inventory
        print('\033[93mCurrent inventory:\n')
        for item in inventory:
            print(f'Name: {item['name']} \nQuantity: {item['quantity']} \nPrice: {item['price']} \n')
        print('\033[0m')
    except Exception as e:
        print(f'Error: {e}')