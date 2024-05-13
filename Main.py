import AddInv, RemInv, EditInv, ViewInv

def main():
    while True:
        print('\n1. Add new item')
        print('2. Remove item')
        print('3. Edit item')
        print('4. View Inventory')
        print('5. Exit')

        choice = input('Enter the choice: ')
        print(f'You have picked option: {choice} ')

        if choice == '1':
            AddInv.add_item()
        elif choice == '2':
            RemInv.remove_item()
        elif choice == '3':
            EditInv.edit_item()
        elif choice == '4':
            ViewInv.view_inventory()
        elif choice == '5':
            print('Exiting program...')
            break
        else:
            print('Invalid choice. Please try again')

if __name__ == '__main__':
    main()