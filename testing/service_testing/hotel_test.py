from unittest import TestCase
from unittest.mock import patch

from exceptions.exception import HotelExistError, NoHotelFoundError, HotelNotExistError, NoRoomsError
from services.hotel_service import HotelService


class Testing(TestCase):
    @patch('services.hotel_service.DB')
    def test_existing_add_hotel(self, mocked_DB):
        hotel_service = HotelService()
        mocked_DB.return_value.get_item.return_value = ('h1', 4)
        with self.assertRaises(HotelExistError):
            hotel_service.add_hotel('h1', 5)

    @patch('services.hotel_service.DB')
    def test_add_hotel(self, mocked_DB):
        hotel_service = HotelService()
        mocked_DB.return_value.get_item.return_value = None
        result = hotel_service.add_hotel('h2', 4)
        mocked_DB.return_value.add_item.assert_called_once()
        self.assertEqual(result, None)

    @patch('services.hotel_service.DB')
    def test_get_hotels_not_exist(self, mocked_DB):
        hotel_service = HotelService()
        mocked_DB.return_value.get_items.return_value = None
        with self.assertRaises(NoHotelFoundError):
            hotel_service.get_all_hotels()

    @patch('services.hotel_service.DB')
    def test_get_hotels(self, mocked_DB):
        hotel_service = HotelService()
        mocked_DB.return_value.get_items.return_value = [(1, 'h1', 2)]
        result = hotel_service.get_all_hotels()
        self.assertEqual(result[0].hid, 1)
        self.assertEqual(result[0].name, 'h1')
        self.assertEqual(result[0].rating, 2)

    @patch('services.hotel_service.DB')
    def test_get_rooms_available(self, mocked_DB):
        hotel_service = HotelService()
        mocked_DB.return_value.get_item.side_effect = [None, (1, 'h1', 4), (1, 'h2', 4)]
        mocked_DB.return_value.get_items.side_effect = [[(1, 'regular', 2000, 'available', 1)], None]
        with self.assertRaises(HotelNotExistError):
            hotel_service.get_available_rooms(2)
        result = hotel_service.get_available_rooms(1)
        self.assertEqual(result[0].room_id, 1)
        self.assertEqual(result[0].room_type, 'regular')
        self.assertEqual(result[0].price, 2000)
        self.assertEqual(result[0].status, 'available')
        self.assertEqual(result[0].hid, 1)

        with self.assertRaises(NoRoomsError):
            hotel_service.get_available_rooms(1)