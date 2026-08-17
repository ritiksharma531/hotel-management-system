from controllers.auth_controller import AuthController
from database.db import initialize_db
from menus.admin_menu import admin_menu
from menus.user_menu import user_menu

initialize_db()
user_input = ''
authController = AuthController()
while user_input!='4':
    print(f'{"Welcome to Hotel Management":>70}')
    print('Choose Option')
    print('1. Register')
    print('2. Login')
    print('3. Login as Admin')
    print('4. Exit')
    user_input = input('Enter you choice: ')

    if user_input == '1':
        authController.register_user()
        print('Registered successfully, Please Login')

    elif user_input == '2':
        user = authController.login_user('user')
        if user:
            print('Logged in successfully')
            user_menu(user)

    elif user_input == '3':
        user = authController.login_user('admin')
        if user:
            admin_menu(user)

    elif user_input == '4':
        print('Thank You for using our Service')

    else:
        print('Invalid Choice, Please try again...')