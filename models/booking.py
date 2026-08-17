class Booking:
    def __init__(self, bid, uid, room_id, booking_date, check_in_date, check_out_date, status):
        self.bid = bid
        self.uid = uid
        self.room_id = room_id
        self.booking_date = booking_date
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = status


    def __str__(self):
        return f'''{self.bid:<10}{self.uid:<35}{self.room_id:<20}{self.booking_date:<20}{str(self.check_in_date):<20}{str(self.check_out_date):<20}{self.status:<20}'''