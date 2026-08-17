from unittest import TestCase
from unittest.mock import patch

from controllers.hotel_controller import HotelController
from exceptions.exception import HotelNotExistError, NoRoomsError, NoHotelFoundError, HotelExistError


class Testing(TestCase):
    @patch('controllers.hotel_controller.HotelService')
    def test_view_all_hotels_success(self, mocked_HotelService):
        hotel_controller = HotelController()
        mocked_HotelService.return_value.get_all_hotels.return_value = [(1, 'Taj', 5)]
        hotel_controller.view_all_hotels()
        mocked_HotelService.return_value.get_all_hotels.assert_called_once()

    @patch('controllers.hotel_controller.HotelService')
    def test_view_all_hotels_none_found(self, mocked_HotelService):
        hotel_controller = HotelController()
        mocked_HotelService.return_value.get_all_hotels.side_effect = NoHotelFoundError
        hotel_controller.view_all_hotels()

    @patch('controllers.hotel_controller.HotelService')
    @patch('builtins.input', return_value='1')
    def test_get_available_rooms_success(self, mocked_input, mocked_HotelService):
        hotel_controller = HotelController()
        mocked_HotelService.return_value.get_available_rooms.return_value = [(1, 'regular', 2000, 'available', 1)]
        hotel_controller.get_available_rooms()
        mocked_HotelService.return_value.get_available_rooms.assert_called_once_with(1)

    @patch('controllers.hotel_controller.HotelService')
    @patch('builtins.input', return_value='1')
    def test_get_available_rooms_hotel_not_exist(self, mocked_input, mocked_HotelService):
        hotel_controller = HotelController()
        mocked_HotelService.return_value.get_available_rooms.side_effect = HotelNotExistError
        hotel_controller.get_available_rooms()

    @patch('controllers.hotel_controller.HotelService')
    @patch('builtins.input', return_value='1')
    def test_get_available_rooms_no_rooms(self, mocked_input, mocked_HotelService):
        hotel_controller = HotelController()
        mocked_HotelService.return_value.get_available_rooms.side_effect = NoRoomsError
        hotel_controller.get_available_rooms()

    @patch('controllers.hotel_controller.HotelService')
    @patch('builtins.input', side_effect=['Taj Palace', '5'])
    def test_add_hotel_success(self, mocked_input, mocked_HotelService):
        hotel_controller = HotelController()
        hotel_controller.add_hotel()
        mocked_HotelService.return_value.add_hotel.assert_called_once_with('Taj Palace', 5)

    @patch('controllers.hotel_controller.HotelService')
    @patch('builtins.input', side_effect=['Taj Palace', '5'])
    def test_add_hotel_already_exists(self, mocked_input, mocked_HotelService):
        hotel_controller = HotelController()
        mocked_HotelService.return_value.add_hotel.side_effect = HotelExistError
        hotel_controller.add_hotel()