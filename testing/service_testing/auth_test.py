import hashlib
from unittest import TestCase
from unittest.mock import patch
from exceptions.exception import UserExistsError, UserNotExistError, IncorrectPasswordError
from services.auth_service import AuthService


class Testing(TestCase):
    @patch('services.auth_service.DB')
    def test_register_existing_user(self, mocked_DB):
        auth_service = AuthService()
        mocked_DB.get_item.return_value = (1, 'Ritik', '9876543210')
        with self.assertRaises(UserExistsError):
            auth_service.register_user('9876543210', 'Pass123!', 'Ritik', 'user')

    @patch('services.auth_service.DB')
    def test_register_new_user(self, mocked_DB):
        auth_service = AuthService()
        mocked_DB.get_item.side_effect = [None, (2, 'Aman', '9998887776')]
        auth_service.register_user('9998887776', 'Pass123!', 'Aman', 'user')
        self.assertEqual(mocked_DB.add_item.call_count, 2)

    @patch('services.auth_service.DB')
    def test_login_user_not_exist(self, mocked_DB):
        auth_service = AuthService()
        mocked_DB.get_item.return_value = None
        with self.assertRaises(UserNotExistError):
            auth_service.login_user('0000000000', 'Pass123!', 'user')

    @patch('services.auth_service.DB')
    def test_login_wrong_password(self, mocked_DB):
        auth_service = AuthService()
        mocked_DB.get_item.side_effect = [(1, 'Ritik', '9876543210'), ('Asdf123456!', 'user')]
        with self.assertRaises(IncorrectPasswordError):
            auth_service.login_user('9876543210', '325423dfs$#D', 'user')

    @patch('services.auth_service.DB')
    def test_login_success(self, mocked_DB):
        auth_service = AuthService()
        hashed_password = hashlib.sha256('Asdf123!'.encode()).hexdigest()
        mocked_DB.get_item.side_effect = [(1, 'Ritik', '9876543210'), (hashed_password, 'user')]
        user = auth_service.login_user('9876543210', 'Asdf123!', 'user')
        self.assertEqual(user.uid, 1)
        self.assertEqual(user.name, 'Ritik')
        self.assertEqual(user.mobile, '9876543210')