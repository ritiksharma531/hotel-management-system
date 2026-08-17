class HotelNotExistError(Exception):
    pass

class HotelExistError(Exception):
    pass

class RoomNotAvailableError(Exception):
    pass

class RoomNotBookedError(Exception):
    pass

class UserExistsError(Exception):
    pass

class UserNotExistError(Exception):
    pass

class IncorrectPasswordError(Exception):
    pass

class NoRoomsError(Exception):
    pass

class NoBookingFound(Exception):
    pass

class PaymentCancelledError(Exception):
    pass

class NoHotelFoundError(Exception):
    pass