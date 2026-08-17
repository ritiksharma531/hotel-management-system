from unittest import TestCase
from unittest.mock import Mock, patch
from controllers.auth_controller import AuthController
from exceptions.exception import UserExistsError, UserNotExistError, IncorrectPasswordError


class Testing(TestCase):
    @patch('controllers.auth_controller.AuthService')
    @patch('services.validation.getpass.getpass', return_value='Pass123!')
    @patch('builtins.input', side_effect=['Ritik', '9876543210'])
    def test_register_user_success(self, mocked_input, mocked_getpass, mocked_AuthService):
        auth_controller = AuthController()
        mocked_AuthService.return_value.register_user.return_value = 'User registered successfully'
        auth_controller.register_user()
        mocked_AuthService.return_value.register_user.assert_called_once_with(
            '9876543210', 'Pass123!', 'Ritik', 'user'
        )

    @patch('controllers.auth_controller.AuthService')
    @patch('services.validation.getpass.getpass', return_value='Pass123!')
    @patch('builtins.input', side_effect=['Ritik', '9876543210'])
    def test_register_user_already_exists(self, mocked_input, mocked_getpass, mocked_AuthService):
        auth_controller = AuthController()
        mocked_AuthService.return_value.register_user.side_effect = UserExistsError
        auth_controller.register_user()

    @patch('controllers.auth_controller.AuthService')
    @patch('services.validation.getpass.getpass', return_value='Pass123!')
    @patch('builtins.input', return_value='9876543210')
    def test_login_user_success(self, mocked_input, mocked_getpass, mocked_AuthService):
        auth_controller = AuthController()
        user = Mock(uid=1, name='Ritik', mobile = 9998887776)
        mocked_AuthService.return_value.login_user.return_value = user
        result = auth_controller.login_user('user')
        self.assertEqual(result, user)

    @patch('controllers.auth_controller.AuthService')
    @patch('services.validation.getpass.getpass', return_value='Pass123!')
    @patch('builtins.input', return_value='9876543210')
    def test_login_user_not_exist(self, mocked_input, mocked_getpass, mocked_AuthService):
        auth_controller = AuthController()
        mocked_AuthService.return_value.login_user.side_effect = UserNotExistError
        result = auth_controller.login_user('user')
        self.assertIsNone(result)

    @patch('controllers.auth_controller.AuthService')
    @patch('services.validation.getpass.getpass', return_value='WrongPass1!')
    @patch('builtins.input', return_value='9876543210')
    def test_login_user_wrong_password(self, mocked_input, mocked_getpass, mocked_AuthService):
        auth_controller = AuthController()
        mocked_AuthService.return_value.login_user.side_effect = IncorrectPasswordError
        result = auth_controller.login_user('user')
        self.assertIsNone(result)