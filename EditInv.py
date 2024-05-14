import Inventory
from AddInv import validate_name_input, get_name_input, validate_price_input, get_price_input, validate_quantity_input, get_quantity_input

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
            # Check if index is > length of the dictionary
            if int(index) > max:
                raise ValueError('Invalid index, try again...')
            return int(index)
        except ValueError as error:
            print(f'\033[91m{error}\033[0m')
            # Asks for user input again
            index = get_position_input()
        except Exception as e:
            print(f'\033[91mError: {e}\033[0m]')


def edit_item():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')

    # Display current inventory
    print('Current inventory:')
    for i, item in enumerate(inventory):
        print(f'{i+1} -> {item['name']}')

    # Get input for item to edit and - 1 to get index
    index = validate_position_input(get_position_input(),len(inventory)) - 1

    # Gets any changes to the fields
    print('Enter the new value if you wish to change it, otherwise leave blank.')
    item_name = validate_name_input(inventory, get_name_input(), True)
    item_price = validate_price_input(get_price_input(), True)
    item_quantity = validate_quantity_input(get_quantity_input(), True)
    
    # If a new value is given, overwrite the existing value
    if item_name:
        inventory[index]['name'] = item_name
    if item_price:
        inventory[index]['price'] = item_price
    if item_quantity:
        inventory[index]['quantity'] = item_quantity

    # Export the changes
    Inventory.export_inventory('inventory.csv', inventory)
    print('\033[92mItem edited successfully.\033[0m')