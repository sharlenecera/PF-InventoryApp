import Inventory

def view_inventory():
    # Load existing inventory
    inventory = Inventory.import_inventory('inventory.csv')
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