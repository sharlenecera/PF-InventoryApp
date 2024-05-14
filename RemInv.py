import Inventory
from EditInv import get_position_input, validate_position_input

def remove_item():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')

    # Display current inventory
    print('Current inventory:')
    for i, item in enumerate(inventory):
        print(f'{i+1} -> {item['name']}')

    # Get index for item to remove
    index = validate_position_input(get_position_input(), len(inventory)) - 1

    # Remove item from inventory
    del inventory[index]
    Inventory.export_inventory('inventory.csv', inventory)
    print('\033[92mItem removed successfully.\033[0m')