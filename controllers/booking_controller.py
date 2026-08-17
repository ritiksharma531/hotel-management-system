from exceptions.exception import NoBookingFound
from services.booking_service import BookingService
from services.print_service import print_bookings


class BookingController:
    def __init__(self):
        self.booking_service = BookingService()


    def view_my_bookings(self, user):
        try:
            all_bookings = self.booking_service.get_my_bookings(user)
            print_bookings(all_bookings)
        except NoBookingFound:
            print('No bookings found')


    def view_all_bookings(self):
        try:
            all_bookings = self.booking_service.get_all_bookings()
            print_bookings(all_bookings)
        except NoBookingFound:
            print('No bookings found')