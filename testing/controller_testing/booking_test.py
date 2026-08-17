from unittest import TestCase
from unittest.mock import Mock, patch

from controllers.booking_controller import BookingController
from exceptions.exception import NoBookingFound


class Testing(TestCase):
    @patch('controllers.booking_controller.BookingService')
    def test_view_my_bookings_success(self, mocked_BookingService):
        booking_controller = BookingController()
        user = Mock(uid=1, name='Ritik')
        mocked_BookingService.return_value.get_my_bookings.return_value = [
            (1, 1, 1, '2026-08-15', '2026-08-16', '2026-08-18', 'booked')
        ]
        booking_controller.view_my_bookings(user)
        mocked_BookingService.return_value.get_my_bookings.assert_called_once_with(user)

    @patch('controllers.booking_controller.BookingService')
    def test_view_my_bookings_none_found(self, mocked_BookingService):
        booking_controller = BookingController()
        user = Mock(uid=1, name='Ritik')
        mocked_BookingService.return_value.get_my_bookings.side_effect = NoBookingFound
        booking_controller.view_my_bookings(user)

    @patch('controllers.booking_controller.BookingService')
    def test_view_all_bookings_success(self, mocked_BookingService):
        booking_controller = BookingController()
        mocked_BookingService.return_value.get_all_bookings.return_value = [
            (1, 1, 1, '2026-08-15', '2026-08-16', '2026-08-18', 'booked')
        ]
        booking_controller.view_all_bookings()
        mocked_BookingService.return_value.get_all_bookings.assert_called_once()

    @patch('controllers.booking_controller.BookingService')
    def test_view_all_bookings_none_found(self, mocked_BookingService):
        booking_controller = BookingController()
        mocked_BookingService.return_value.get_all_bookings.side_effect = NoBookingFound
        booking_controller.view_all_bookings()