from unittest import TestCase
from unittest.mock import Mock, patch

from exceptions.exception import HotelNotExistError, RoomNotAvailableError, PaymentCancelledError, RoomNotBookedError
from services.room_service import RoomService


class Testing(TestCase):
    @patch('services.room_service.DB')
    def test_add_room_no_hotel(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = None
        with self.assertRaises(HotelNotExistError):
            room_service.add_room('regular', 2000, 'available', 1)

    @patch('services.room_service.DB')
    def test_add_room_success(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = (1, 'h1', 4)
        result = room_service.add_room('regular', 2000, 'available', 1)
        mocked_DB.return_value.add_item.assert_called_once()
        self.assertEqual(result, None)

    @patch('services.room_service.DB')
    def test_book_room_not_available(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = None
        user = Mock(uid=1, name='Ritik')
        with self.assertRaises(RoomNotAvailableError):
            room_service.book_room(1, user, '20-08-2026')

    @patch('builtins.input', return_value='n')
    @patch('services.room_service.DB')
    def test_book_room_payment_cancelled(self, mocked_DB, mocked_input):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = (1, 'regular', 2000, 'available', 1)
        user = Mock(uid=1, name='Ritik')
        with self.assertRaises(PaymentCancelledError):
            room_service.book_room(1, user, '20-08-2026')

    @patch('builtins.input', return_value='y')
    @patch('services.room_service.DB')
    def test_book_room_success(self, mocked_DB, mocked_input):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = (1, 'regular', 2000, 'available', 1)
        user = Mock(uid=1, name='Ritik')
        room_service.book_room(1, user, '20-08-2026')
        self.assertEqual(mocked_DB.return_value.add_item.call_count, 2)

    @patch('services.room_service.DB')
    def test_check_in_no_booking(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = None
        user = Mock(uid=1, name='Ritik')
        with self.assertRaises(RoomNotBookedError):
            room_service.check_in_room(1, user)

    @patch('services.room_service.DB')
    def test_check_in_already_checked_in(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = (
            1, 1, 1, '2026-08-15', None, '2026-08-20', 'checked_in'
        )
        user = Mock(uid=1, name='Ritik')
        result = room_service.check_in_room(1, user)
        self.assertEqual(result, 'You already checked in')

    @patch('services.room_service.DB')
    def test_check_in_already_cancelled(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = (
            1, 1, 1, '2026-08-15', None, '2026-08-20', 'cancelled'
        )
        user = Mock(uid=1, name='Ritik')
        with self.assertRaises(RoomNotBookedError):
            room_service.check_in_room(1, user)

    @patch('services.room_service.DB')
    def test_check_in_success(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = (
            1, 1, 1, '2026-08-15', None, '2026-08-20', 'booked'
        )
        user = Mock(uid=1, name='Ritik')
        result = room_service.check_in_room(1, user)
        mocked_DB.return_value.update_item.assert_called_once()
        self.assertEqual(result, 'Successfully checked in')

    @patch('services.room_service.DB')
    def test_check_out_no_booking(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = None
        user = Mock(uid=1, name='Ritik')
        with self.assertRaises(RoomNotBookedError):
            room_service.check_out_room(1, user)

    @patch('services.room_service.DB')
    def test_check_out_success(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = (
            1, 1, 1, '2026-08-15', '2026-08-16', '2026-08-20', 'checked_in'
        )
        user = Mock(uid=1, name='Ritik')
        result = room_service.check_out_room(1, user)
        self.assertEqual(mocked_DB.return_value.update_item.call_count, 2)
        self.assertEqual(result, 'Successfully checked out')

    @patch('services.room_service.DB')
    def test_cancel_no_booking(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = None
        user = Mock(uid=1, name='Ritik')
        with self.assertRaises(RoomNotBookedError):
            room_service.cancel_room_booking(1, user)

    @patch('services.room_service.DB')
    def test_cancel_success(self, mocked_DB):
        room_service = RoomService()
        mocked_DB.return_value.get_item.return_value = (
            1, 1, 1, '2026-08-15', None, '2026-08-20', 'booked'
        )
        user = Mock(uid=1, name='Ritik')
        result = room_service.cancel_room_booking(1, user)
        self.assertEqual(mocked_DB.return_value.update_item.call_count, 2)
        self.assertEqual(result, 'Booking successfully cancelled')