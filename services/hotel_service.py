import logger
from database import queries
from database.db_functions import DB
from exceptions.exception import HotelExistError, HotelNotExistError, NoRoomsError, NoHotelFoundError
from models.hotel import Hotel
from models.room import Room


class HotelService:
    def __init__(self):
        self.DB = DB
        self.logger = logger.get_logger(__name__)

    def get_all_hotels(self):
        try:
            result = self.DB.get_items(queries.GET_HOTELS)
            if not result:
                raise NoHotelFoundError
            hotels = []
            for hotel in result:
                hotels.append(Hotel(*hotel))
            return hotels

        except NoHotelFoundError:
            raise

    def add_hotel(self, name, rating):
        try:
            if self.DB.get_item(queries.IS_HOTEL_EXIST, name):
                self.logger.info(f"Tried to add hotel  {name}, but already exists")
                raise HotelExistError
            self.DB.add_item(queries.ADD_HOTEL, name, rating)
            self.logger.info(f"Hotel {name} added successfully")
            return None
        except HotelExistError:
            raise

    def get_available_rooms(self, hid):
        try:
            if not self.DB.get_item(queries.GET_HOTEL, hid):
                raise HotelNotExistError

            rooms_list = self.DB.get_items(queries.GET_ROOMS, hid, 'available')
            if not rooms_list:
                raise NoRoomsError
            rooms = []
            for room in rooms_list:
                rooms.append(Room(*room))
            return rooms
        except HotelNotExistError:
            raise
        except NoRoomsError:
            raise