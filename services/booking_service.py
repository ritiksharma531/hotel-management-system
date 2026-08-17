from database import queries
from database.db_functions import DB
from exceptions.exception import NoBookingFound
from models.booking import Booking


class BookingService:
    def __init__(self):
        self.DB = DB

    def get_my_bookings(self, user):
        try:
            all_bookings = self.DB.get_items(queries.GET_MY_BOOKINGS, user.uid)
            if not all_bookings:
                raise NoBookingFound
            bookings = []
            for booking in all_bookings:
                bookings.append(Booking(*booking))
            return bookings
        except NoBookingFound:
            raise

    def get_all_bookings(self):
        try:
            all_bookings = self.DB.get_items(queries.GET_BOOKINGS)
            if not all_bookings:
                raise NoBookingFound
            bookings = []
            for booking in all_bookings:
                bookings.append(Booking(*booking))
            return bookings
        except NoBookingFound:
            raise