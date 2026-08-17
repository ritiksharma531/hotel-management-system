class Room:
    def __init__(self, room_id, room_type, room_price, status, hid):
        self.room_id = room_id
        self.room_type = room_type
        self.price = room_price
        self.status = status
        self.hid = hid

    def __str__(self):
        return f'''{self.room_id:<10}{self.room_type:<35}{self.price:<20}{self.status:<20}{self.hid:<20}'''