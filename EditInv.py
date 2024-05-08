import Inventory

def edit_item():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')

    # Display current inventory
    print('Current inventory:')
    for i, item in enumerate(inventory):
        print(f'{i+1}, {item[0]} - {item[1]}')

    # Get input for item to edit
    index = int(input('Enter the index of the item to edit: ')) - 1

    # Edit item in inventory
    if 0<= index < len(inventory):
        new_quantity = int(input('Enter the new quantity: '))
        inventory[index][1] = new_quantity
        Inventory.export_inventory('inventory.csv', inventory)
        print('Item edited successfully.')
    else:
        print('Invalid index.')