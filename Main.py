import AddInv, RemInv, EditInv, ViewInv
import bcrypt

# password is same as username
login_details = {
    'admin': bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt(10)) 
}

def login():
    login_successful = False
    # Loops until login is successful
    while not login_successful:
        # Input login details
        username = input("Enter username: ")
        password = str(input("Enter password: "))

        # Checks if username is valid and if the password matches the stored hashed password
        if username in login_details and bcrypt.checkpw(password.encode('utf-8'),login_details[username]):
            print(f'\033[92mLogin successful! Welcome {username}\033[0m')
            login_successful = True
        else:
            print('\033[91mInvalid login credentials, try again...\033[0m')

def print_menu():
    print('\033[96m\n============================================')
    print('|               Main Menu                   |')
    print('============================================')
    print('|   1. Add new item                         |')
    print('|   2. Remove item                          |')
    print('|   3. Edit item                            |')
    print('|   4. View Inventory                       |')
    print('|   5. Exit                                 |')
    print('============================================\033[0m')

def main():
    login()
    
    while True:
        print_menu()

        choice = input('\033[35m~~~~~~Enter the choice: ')
        print(f'You have picked option: {choice} \033[0m')

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
            print('\033[91mInvalid choice. Please try again\033[0m]')

if __name__ == '__main__':
    main()