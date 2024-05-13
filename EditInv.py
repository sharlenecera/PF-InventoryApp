import Inventory
from AddInv import validate_quantity_input, get_quantity_input

def get_position_input():
    return input('Enter the position of the item to edit: ')

# max is the length of the dictionary
def validate_position_input(index, max):
    while True:
        try:
            # Check if the input is an integer >= 0
            if not index.isnumeric():
                raise ValueError('Invalid index, try again...')
            # Check if index is 0
            if index=='0':
                raise ValueError('Invalid index, try again...')
            # Check if index is >= length of the dictionary
            if int(index) > max:
                raise ValueError('Invalid index, try again...')
            return int(index)
        except ValueError as error:
            print(f'\033[91m{error}\033[0m')
            index = get_position_input()
        except Exception as e:
            print(f'Error: {e}')

def get_item_by_index(inventory, index):
    for i, item in enumerate(inventory):
        if i == index:
            return item

def edit_item():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')

    # Display current inventory
    print('Current inventory:')
    for i, item in enumerate(inventory):
        print(f'{i+1}, {item}: {inventory[item]}')

    # Get input for item to edit and - 1 to get index
    index = validate_position_input(get_position_input(),len(inventory)) - 1
    item_to_edit = get_item_by_index(inventory, index)

    # Get new quantity

    # Edit item in inventory
    inventory[item_to_edit] = validate_quantity_input(get_quantity_input())
    Inventory.export_inventory('inventory.csv', inventory)
    print('\033[92mItem edited successfully.\033[0m')