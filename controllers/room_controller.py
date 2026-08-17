from exceptions.exception import HotelNotExistError, RoomNotAvailableError, RoomNotBookedError, PaymentCancelledError
from services.room_service import RoomService
from services.validation import validate_input, is_valid_date


class RoomController:
    def __init__(self):
        self.room_service = RoomService()


    def book_room(self, user):
        try:
            room_id = int(validate_input('Enter room_id of room: ', lambda rid: rid.isdigit() and int(rid) >= 0,
                                         "rid must be non negative integer, try again"))
            check_out_date = validate_input('Enter check out date(DD-MM-YYYY): ', is_valid_date,
                                            "Enter correct date")
            self.room_service.book_room(room_id, user, check_out_date)
            print('Room Booked successfully, Feel free to check in anytime now...')
        except RoomNotAvailableError:
            print('Room is not available')
        except PaymentCancelledError:
            print('Payment cancelled')


    def cancel_room_booking(self, user):
        try:
            room_id = int(validate_input('Enter room_id of room: ', lambda rid: rid.isdigit() and int(rid) >= 0,
                                         "rid must be non negative integer, try again"))
            result = self.room_service.cancel_room_booking(room_id, user)
            print(result)
        except RoomNotBookedError:
            print('Room is not booked')


    def check_in(self, user):
        try:
            room_id = int(validate_input('Enter room_id of room: ', lambda rid: rid.isdigit() and int(rid) >= 0,
                                         "rid must be non negative integer, try again"))
            result = self.room_service.check_in_room(room_id, user)
            if result:
                print(result)
        except RoomNotBookedError:
            print('Room is not booked')

    def check_out(self, user):
        try:
            room_id = int(validate_input('Enter room_id of room: ', lambda rid: rid.isdigit() and int(rid) >= 0,
                                         "rid must be non negative integer, try again"))
            result = self.room_service.check_out_room(room_id, user)
            if result:
                print(result)
        except RoomNotBookedError:
            print('Room is not booked')


    def add_room(self):
        try:
            hid = int(validate_input('Enter hid of hotel: ', lambda hid: hid.isdigit() and int(hid) >= 0 and int(hid) < 100,"hid must be non negative integer, try again"))
            room_type = validate_input('Enter Type of room (regular or premium): ',lambda name: name.lower() == 'regular' or name.lower() == 'premium', "Room can be of two types regular or premium, try again")
            price = int(validate_input('Enter price of room: ', lambda hid: hid.isdigit() and int(hid) > 0, "Room price must be positive integer, try again"))
            status = 'available'
            self.room_service.add_room(room_type.lower(), price, status, hid)
            print('Room added successfully')
        except HotelNotExistError:
            print('Hotel not found')