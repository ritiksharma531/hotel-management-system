from exceptions.exception import UserNotExistError, IncorrectPasswordError, UserExistsError
from services.auth_service import AuthService
from services.validation import validate_input, validate_password, password_regex


class AuthController:
    def __init__(self):
        self.auth_service = AuthService()

    def register_user(self):
        try:
            full_name = validate_input('Enter your Full Name: ', lambda name: len(name) >= 2 and len(name) <= 30, "Name must be between 2 and 30 characters, try again")
            mobile = validate_input('Enter your mobile: ', lambda mobile: mobile.isdigit() and len(mobile) == 10, "Mobile must be 10 digits, try again")
            password = validate_password('Enter password: ', password_regex, 'Password length must be between 8 and 30 and password must contain at least one uppercase letter, one lowercase letter, one number between 0 and 9 and one special character out of !, @, #, $, %, ^, & and *')
            self.auth_service.register_user(mobile, password, full_name, 'user')
        except UserExistsError:
            print('User already exists')

    def login_user(self, role):
        try:
            mobile = validate_input('Enter Mobile: ', lambda mobile: mobile.isdigit() and len(mobile) == 10, "Mobile must be 10 digits, try again")
            password = validate_password('Enter password: ', password_regex, 'Password length must be between 8 and 30 and password must contain at least one uppercase letter, one lowercase letter, one number between 0 and 9 and one special character out of !, @, #, $, %, ^, & and *')
            result = self.auth_service.login_user(mobile, password, role)
            if isinstance(result, str):
                print(result)
            else:
                user = result
                return user

        except UserNotExistError:
            print('User not found')
        except IncorrectPasswordError:
            print('Password is incorrect')

