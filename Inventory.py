import csv

class Inventory:

    def __init__(self, file_name):
        self.__file_name = file_name

##########   VIEW INVENTORY   ########################################################

    def view_inventory(self):
        # Load existing inventory
        inventory = self.import_inventory()
        if not inventory:
            print('\033[91mInventory is empty.\033[0m')
            return

        # Some ANSI escape sequences
        bs = '\033[1m' # bold start
        reset = '\033[0m\033[93m' # bold end
        us = '\033[4m' # Underline start

        try:
            # Display current inventory
            print('\033[93m\n ============================================')
            print(f'|            {us}Current inventory{reset}:              |')
            print(f' ============================================')
            for item in inventory:
                print(f'| ==  {bs}Name{reset}: {item['name']}')
                print(f'|     {bs}Price{reset}: {item['price']}')
                print(f'|     {bs}Quantity{reset}: {item['quantity']}')
                print('|')
            print(' ============================================\033[0m')
        except Exception as e:
            print(f'\033[91mError: {e}\033[0m]')


##########   ADD INVENTORY   ########################################################


    def get_name_input(self):
        return input('Enter item name: ')

    def validate_name_input(self, inventory, name, optional=False):
        while True:
            try:
                # Check if input is optional
                if optional and name == '':
                    return None
                # Check if name already exists in inventory
                if name in [item['name'] for item in inventory]:
                    raise ValueError('Item name already exists, try again...')
                return name
            except ValueError as error:
                print(f'\033[91mError: {error}\033[0m]')
                name = self.get_name_input()
            except Exception as e:
                print(f'\033[91mError: {e}\033[0m]')


    def get_price_input(self):
        return input('Enter the price: ')


    def validate_price_input(self, price, optional=False):
        while True:
            try:
                # Check if input is optional
                if optional and price == '':
                    return None
                # Check if the input is an integer >= 0
                if not price.isnumeric():
                    raise ValueError('This inventory only allows positive integer prices, try again...')
                # Check if quantity is 0
                if price=='0':
                    raise ValueError('You cannot have a price of 0, try again...')
                return int(price)
            except ValueError as error:
                print(f'\033[91mError: {error}\033[0m]')
                price = self.get_price_input()
            except Exception as e:
                print(f'\033[91mError: {e}\033[0m]')


    def get_quantity_input(self):
        return input('Enter item quantity: ')


    def validate_quantity_input(self, quantity, optional=False):
        while True:
            try:
                # Check if input is optional
                if optional and quantity == '':
                    return None
                # Check if the input is an integer >= 0
                if not quantity.isnumeric():
                    raise ValueError('You can only have positive integer quantities, try again...')
                # Check if quantity is 0
                # if quantity=='0':
                #     raise ValueError('You cannot have a quantity of 0, try again...')
                return int(quantity)
            except ValueError as error:
                print(f'\033[91mError: {error}\033[0m]')
                quantity = self.get_quantity_input()
            except Exception as e:
                print(f'\033[91mError: {e}\033[0m]')


    def add_item(self):
        # Load existing inventory
        inventory = self.import_inventory()
        
        # Get input for new item and validate the inputs
        item_name = self.validate_name_input(inventory, self.get_name_input())
        item_price = self.validate_price_input(self.get_price_input())
        item_quantity = self.validate_quantity_input(self.get_quantity_input())

        # Add new item to inventory
        inventory.append({
            'name': item_name,
            'price': item_price,
            'quantity': item_quantity
        })

        # Export updated inventory
        self.export_inventory(inventory)


##########   IMPORT INVENTORY   ######################################################


    def import_inventory(self):
        # Read the data from the CSV file
        try:
            # Read the data from the CSV file
            with open(self.__file_name, 'r', newline='') as file:
                inventory = []
                reader = csv.DictReader(file)
                for row in reader:
                    inventory.append(row)
            return inventory
        except FileNotFoundError:
            print('File not found. Creating now...')
            # creating empty file
            with open(self.__file_name, 'w') as file: 
                print("Empty file created Successfully")
            return []
        

    def export_inventory(self, inventory):
        # Write the data to the CSV file
        try:
            fieldnames = ['name', 'price', 'quantity']

            with open(self.__file_name, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                # Write the header row (dictionary keys)
                writer.writeheader()
                # Write the dictionary row to the csv file
                writer.writerows(inventory)
            print('Inventory exported successfully.')
        except Exception as e:
            print(f'\033[91mError exporting inventory: {e}\033[0m')

'''
How the inventory looks in two different formats

NEW ------------------------

List of Dictionaries:
[
    {
        'name': 'iPhone',
        'price': '999',
        'quantity': '200'
    },
    {
        'name': 'iPad',
        'price': '500',
        'quantity': '100'
    },
    {
        'name': 'mac',
        'price': '2000',
        'quantity': '50'
    }
]

CSV:
name,price,quantity
iPhone,999,200
iPad,500,100
mac,2000,50

OLD ------------------------
Dictionary:
{
    iPhone: 100
    iPad: 20
    mac: 30
}

CSV:
iPhone, iPad, mac
100, 20, 30

'''