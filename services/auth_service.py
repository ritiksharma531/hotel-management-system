import logger
import hashlib
from database import queries
from database.db_functions import DB
from exceptions.exception import UserExistsError, UserNotExistError, IncorrectPasswordError
from models.user import User


class AuthService:
    def __init__(self):
        self.DB = DB
        self.logger = logger.get_logger(__name__)

    def register_user(self, mobile, password, name, role):
        try:
            if self.DB.get_item(queries.GET_USER, mobile):
                self.logger.info(f"Tried to register user with mobile {mobile}, but already exists")
                raise UserExistsError
            else:
                self.DB.add_item(queries.ADD_USER, name, mobile)
                res = self.DB.get_item(queries.GET_USER, mobile)
                user = User(*res)
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                self.DB.add_item(queries.ADD_AUTH, user.uid, hashed_password, 'user')
                print('Registered successfully, Please Login')
                self.logger.info(f"Registered user {user.name}")

        except UserExistsError:
            raise


    def login_user(self, mobile, password, role):
        try:
            user_res = self.DB.get_item(queries.GET_USER, mobile)
            if not user_res:
                self.logger.info(f"Tried to login user with mobile {mobile}, but doesn't exists")
                raise UserNotExistError

            user = User(*user_res)
            stored_password, user_role = self.DB.get_item(queries.GET_PASS, user.uid)
            if user_role != role:
                raise UserNotExistError
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if stored_password != hashed_password:
                self.logger.info(f"Tried to login user with mobile {mobile}, but wrong password")
                raise IncorrectPasswordError
            # return 'Logged in successfully'
            self.logger.info(f"Logged in user {user.name}")
            return user

        except UserNotExistError:
            raise
        except IncorrectPasswordError:
            raise