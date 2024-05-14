import Inventory

def get_name_input():
    return input('Enter item name: ')

def validate_name_input(inventory, name):
    while True:
        try:
            # Check if name already exists in inventory
            if name in [item['name'] for item in inventory]:
                raise ValueError('Item name already exists, try again...')
            return name
        except ValueError as error:
            print(error)
            name = get_name_input()
        except Exception as e:
            print(f'Error: {e}')

def get_price_input():
    return input('Enter the price: ')

def validate_price_input(price):
    while True:
        try:
            # Check if the input is an integer >= 0
            if not price.isnumeric():
                raise ValueError('This inventory only allows positive integer prices, try again...')
            # Check if quantity is 0
            if price=='0':
                raise ValueError('You cannot have a price of 0, try again...')
            return int(price)
        except ValueError as error:
            print(error)
            price = get_price_input()
        except Exception as e:
            print(f'Error: {e}')

def get_quantity_input():
    return input('Enter item quantity: ')

def validate_quantity_input(quantity):
    while True:
        try:
            # Check if the input is an integer >= 0
            if not quantity.isnumeric():
                raise ValueError('You can only have positive integer quantities, try again...')
            # Check if quantity is 0
            # if quantity=='0':
            #     raise ValueError('You cannot have a quantity of 0, try again...')
            return int(quantity)
        except ValueError as error:
            print(error)
            quantity = get_quantity_input()
        except Exception as e:
            print(f'Error: {e}')

def add_item():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')
    
    # Get input for new item
    item_name = validate_name_input(inventory, get_name_input())
    item_price = validate_price_input(get_price_input())
    item_quantity = validate_quantity_input(get_quantity_input())

    # Add new item to inventory
    inventory.append({
        'name': item_name,
        'price': item_price,
        'quantity': item_quantity
    })

    # Export updated inventory
    Inventory.export_inventory('inventory.csv', inventory)