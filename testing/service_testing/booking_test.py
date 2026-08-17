from unittest import TestCase
from unittest.mock import Mock, patch

from exceptions.exception import NoBookingFound
from services.booking_service import BookingService


class Testing(TestCase):
    @patch('services.booking_service.DB')
    def test_get_my_bookings_none_found(self, mocked_DB):
        booking_service = BookingService()
        user = Mock(uid = 1, name = 'Ritik')
        mocked_DB.get_items.return_value = None
        with self.assertRaises(NoBookingFound):
            booking_service.get_my_bookings(user)

    @patch('services.booking_service.DB')
    def test_get_my_bookings_success(self, mocked_DB):
        booking_service = BookingService()
        user = Mock(uid = 1, name = 'Ritik')
        mocked_DB.get_items.return_value = [
            (1, 1, 1, '2026-08-15', '2026-08-16', '2026-08-18', 'booked')
        ]
        result = booking_service.get_my_bookings(user)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].bid, 1)

    @patch('services.booking_service.DB')
    def test_get_all_bookings_none_found(self, mocked_DB):
        booking_service = BookingService()
        mocked_DB.get_items.return_value = None
        with self.assertRaises(NoBookingFound):
            booking_service.get_all_bookings()

    @patch('services.booking_service.DB')
    def test_get_all_bookings_success(self, mocked_DB):
        booking_service = BookingService()
        mocked_DB.get_items.return_value = [
            (1, 1, 1, '2026-08-15', '2026-08-16', '2026-08-18', 'booked'),
            (2, 2, 3, '2026-08-15', '2026-08-17', '2026-08-19', 'checked_in'),
        ]
        result = booking_service.get_all_bookings()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[1].room_id, 3)