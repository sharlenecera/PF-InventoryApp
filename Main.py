import AddInv, RemInv, EditInv, ViewInv

login_details = {
    'admin': 'admin'
}

def login():
    login_successful = False
    while not login_successful:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in login_details and login_details[username] == password:
            print(f'Login successful! Welcome {username}')
            login_successful = True
        else:
            print('Invalid login credentials, try again...')

def main():
    login()

    while True:
        print('\033[96m\n1. Add new item')
        print('2. Remove item')
        print('3. Edit item')
        print('4. View Inventory')
        print('5. Exit\033[0m')

        choice = input('Enter the choice: ')
        print(f'\033[96mYou have picked option: {choice} \033[0m')

        if choice == '1':
            AddInv.add_item()
        elif choice == '2':
            RemInv.remove_item()
        elif choice == '3':
            EditInv.edit_item()
        elif choice == '4':
            ViewInv.view_inventory()
        elif choice == '5':
            print('\033[91mExiting program...\033[0m')
            break
        else:
            print('Invalid choice. Please try again')

if __name__ == '__main__':
    main()