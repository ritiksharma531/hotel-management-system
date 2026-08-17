from exceptions.exception import HotelNotExistError, HotelExistError, NoRoomsError, NoHotelFoundError
from services.hotel_service import HotelService
from services.print_service import print_hotels, print_rooms
from services.validation import validate_input


class HotelController:
    def __init__(self):
        self.hotel_service = HotelService()

    def view_all_hotels(self):
        try:
            hotels = self.hotel_service.get_all_hotels()
            print_hotels(hotels)
        except NoHotelFoundError:
            print('No hotels found')

    def get_available_rooms(self):
        try:
            hid = int(validate_input('Enter hid of hotel: ', lambda hid: hid.isdigit() and int(hid) >= 0 and int(hid) < 100, "hid must be non negative integer, try again"))
            rooms = self.hotel_service.get_available_rooms(hid)
            print_rooms(rooms)
        except HotelNotExistError:
            print('Hotel not found')
        except NoRoomsError:
            print('No rooms found')


    def add_hotel(self):
        try:
            name = validate_input('Enter Name of the Hotel: ', lambda name: len(name) >= 2 and len(name) < 35, "Name must be between 2 and 35 characters, try again")
            rating = int(validate_input('Enter rating for this hotel: ', lambda rating: rating.isdigit() and int(rating) >= 1 and int(rating) <= 5, "Rating must be in ranger 1 - 5 , try again"))
            self.hotel_service.add_hotel(name, rating)
            print('Hotel added successfully')

        except HotelExistError:
            print('Hotel already exists')