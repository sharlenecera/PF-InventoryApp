import Inventory

def get_quantity_input():
    return input('Enter item quantity: ')

def validate_quantity_input(quantity):
    while True:
        try:
            # Check if the input is an integer >= 0
            if not quantity.isnumeric():
                raise ValueError('You cannot have a negative quantity, try again...')
            # Check if quanity is 0
            if quantity=='0':
                raise ValueError('You cannot have a quantity of 0, try again...')
            return int(quantity)
        except ValueError as error:
            print(error)
            quantity = get_quantity_input()
        except Exception as e:
            print(f'Error: {e}')

def add_item():
    # Get input for new item
    item_name = input('Enter item name: ')
    item_quantity = validate_quantity_input(get_quantity_input())

    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')

    # Add new item to inventory
    inventory.append([item_name, item_quantity])

    # Export updated inventory
    Inventory.export_inventory('inventory.csv', inventory)