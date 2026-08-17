from unittest import TestCase
from unittest.mock import Mock, patch

from controllers.room_controller import RoomController
from exceptions.exception import RoomNotAvailableError, PaymentCancelledError, RoomNotBookedError


class Testing(TestCase):
    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', side_effect=['1', '20-08-2026'])
    def test_book_room_success(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        room_controller.book_room(user)
        mocked_RoomService.return_value.book_room.assert_called_once_with(1, user, '20-08-2026')

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', side_effect=['1', '20-08-2026'])
    def test_book_room_not_available(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        mocked_RoomService.return_value.book_room.side_effect = RoomNotAvailableError
        room_controller.book_room(user)

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', side_effect=['1', '20-08-2026'])
    def test_book_room_payment_cancelled(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        mocked_RoomService.return_value.book_room.side_effect = PaymentCancelledError
        room_controller.book_room(user)

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', return_value='1')
    def test_cancel_room_booking_success(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        mocked_RoomService.return_value.cancel_room_booking.return_value = 'Booking successfully cancelled'
        room_controller.cancel_room_booking(user)
        mocked_RoomService.return_value.cancel_room_booking.assert_called_once_with(1, user)

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', return_value='1')
    def test_cancel_room_booking_not_booked(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        mocked_RoomService.return_value.cancel_room_booking.side_effect = RoomNotBookedError
        room_controller.cancel_room_booking(user)

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', return_value='1')
    def test_check_in_success(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        mocked_RoomService.return_value.check_in_room.return_value = 'Successfully checked in'
        room_controller.check_in(user)
        mocked_RoomService.return_value.check_in_room.assert_called_once_with(1, user)

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', return_value='1')
    def test_check_in_not_booked(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        mocked_RoomService.return_value.check_in_room.side_effect = RoomNotBookedError
        room_controller.check_in(user)

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', return_value='1')
    def test_check_out_success(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        mocked_RoomService.return_value.check_out_room.return_value = 'Successfully checked out'
        room_controller.check_out(user)
        mocked_RoomService.return_value.check_out_room.assert_called_once_with(1, user)

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', return_value='1')
    def test_check_out_not_booked(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        user = Mock(uid=1, name='Ritik')
        mocked_RoomService.return_value.check_out_room.side_effect = RoomNotBookedError
        room_controller.check_out(user)

    @patch('controllers.room_controller.RoomService')
    @patch('builtins.input', side_effect=['1', 'regular', '2000'])
    def test_add_room_success(self, mocked_input, mocked_RoomService):
        room_controller = RoomController()
        room_controller.add_room()
        mocked_RoomService.return_value.add_room.assert_called_once_with('regular', 2000, 'available', 1)