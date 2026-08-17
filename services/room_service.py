from datetime import date, datetime

import logger
from database import queries
from database.db_functions import DB
from exceptions.exception import HotelNotExistError, RoomNotAvailableError, RoomNotBookedError, PaymentCancelledError
from models.booking import Booking
from models.room import Room


class RoomService:
    def __init__(self):
        self.DB = DB
        self.logger = logger.get_logger(__name__)
        self.special_dates = [(26, 1), (15, 8), (2, 10), (25, 12)]

    def discount(self):
        today = date.today()
        if (today.day, today.month) in self.special_dates:
            return 20
        if today.isoweekday() in (6,7):
            return 10
        return 0

    def add_room(self, room_type, price, status, hid):
        try:
            if not self.DB.get_item(queries.GET_HOTEL, hid):
                self.logger.info(f"Tried to add room, but hotel doesn't exists")
                raise HotelNotExistError

            self.DB.add_item(queries.ADD_ROOM, room_type, price, status, hid)
            self.logger.info(f"\'{room_type}\'room added successfully in hotel with hid {hid}")
            return None
        except HotelNotExistError:
            raise


    def book_room(self, room_id, user, check_out_date):
        try:
            room_details = self.DB.get_item(queries.GET_AVAILABLE_ROOM, room_id)
            if not room_details:
                self.logger.info(f"{user.name} tried to book room but not available")
                raise RoomNotAvailableError
            room = Room(*room_details)
            discount = self.discount()
            if discount:
                print(f'You got discount of {discount}%')
            total_price = room.price*(datetime.strptime(check_out_date, '%d-%m-%Y').date() - date.today()).days
            if total_price == 0:
                total_price = room.price
            discounted_price = total_price - (total_price * discount / 100)
            print(f'Total price is {discounted_price}')
            res = input('Enter y to pay: ')
            if res.lower() != 'y':
                self.logger.info(f"{user.name} cancelled the payment")
                raise PaymentCancelledError
            self.DB.add_item(queries.BOOK_ROOM, room.room_id)
            self.DB.add_item(queries.ADD_BOOKING, user.uid, room.room_id, date.today(), check_out_date, 'booked')
            self.logger.info(f"{user.name} booked room with room_id {room_id}")

        except (RoomNotAvailableError, PaymentCancelledError):
            raise

    def check_in_room(self, room_id, user):
        try:
            booking_details = self.DB.get_item(queries.GET_BOOKING, user.uid, room_id)
            if not booking_details:
                self.logger.info(f"{user.name} tried to check in but room not booked")
                raise RoomNotBookedError

            booking = Booking(*booking_details)
            if booking.status == 'checked_in':
                self.logger.info(f"{user.name} tried to check in after checking in")
                return 'You already checked in'
            if booking.status in ('cancelled', 'completed'):
                self.logger.info(f"{user.name} tried to check in after booking has been completed")
                raise RoomNotBookedError

            if booking.status == 'booked':
                self.DB.update_item(queries.CHECK_IN, date.today(), user.uid, room_id)
                self.logger.info(f"{user.name} checked in {room_id}")
                return 'Successfully checked in'
        except RoomNotBookedError:
            raise


    def check_out_room(self, room_id, user):
        try:
            booking_details = self.DB.get_item(queries.GET_BOOKING, user.uid, room_id)
            if not booking_details:
                self.logger.info(f"{user.name} tried to check out but no booking found")
                raise RoomNotBookedError

            booking = Booking(*booking_details)
            if booking.status in ('completed', 'cancelled'):
                self.logger.info(f"{user.name} tried to check out but no booking found")
                raise RoomNotBookedError

            if booking.status == 'booked':
                self.logger.info(f"{user.name} tried to check out but never checked in")
                return "Can't check out, you never checked in"

            if booking.status == 'checked_in':
                self.DB.update_item(queries.CHECK_OUT_BOOKING, date.today(), user.uid, room_id)
                self.DB.update_item(queries.UPDATE_ROOM_COMPLETED, room_id)

            self.logger.info(f"{user.name} checked out room {room_id}")
            return 'Successfully checked out'
        except RoomNotBookedError:
            raise


    def cancel_room_booking(self, room_id, user):
        try:
            booking_details = self.DB.get_item(queries.GET_BOOKING, user.uid, room_id)
            if not booking_details:
                self.logger.info(f"{user.name} tried to cancel booking but no booking found")
                raise RoomNotBookedError
            booking = Booking(*booking_details)
            if booking.status == 'completed':
                self.logger.info(f"{user.name} tried to cancel booking but no booking found")
                raise RoomNotBookedError
            self.DB.update_item(queries.CANCEL_BOOKING, user.uid, room_id)
            self.DB.update_item(queries.UPDATE_ROOM_COMPLETED, room_id)
            self.logger.info(f"{user.name} cancelled booking for room {room_id}")
            return 'Booking successfully cancelled'

        except RoomNotBookedError:
            raise