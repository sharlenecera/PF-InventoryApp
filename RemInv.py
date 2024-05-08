import Inventory

def remove_item():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')

    # Display current inventory
    print('Current inventory:')
    for i, item in enumerate(inventory):
        print(f'{i+1}, {item[0]} - {item[1]}')

    # Get input for item to remove
    index = int(input('Enter the index of the item to remove: ')) - 1

    # Remove item from inventory
    if 0 <= index < len(inventory):
        del inventory[index]
        Inventory.export_inventory('inventory.csv', inventory)
        print('Item removed successfully.')
    else:
        print('Invalid index.')