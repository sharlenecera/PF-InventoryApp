import Inventory

def add_item():
    # Get input for new item
    item_name = input('Enter item name: ')
    item_quantity = int(input('Enter item quantity: '))

    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')

    # Add new item to inventory
    inventory.append([item_name, item_quantity])

    # Export updated inventory
    Inventory.export_inventory('inventory.csv', inventory)