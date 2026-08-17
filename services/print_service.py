def print_hotels(all_hotels):
    if not all_hotels:
        print('No Hotels found')
    else:
        print(f"{'ID':<10}{'Name':<35}{'Rating':<20}")
        for hotel in all_hotels:
            print(hotel)


def print_rooms(all_rooms):
    if not all_rooms:
        print('No Rooms found')
    else:
        print(f"{'RoomID':<10}{'Type':<35}{'Price':<20}{'Status':<20}{'HotelID':<20}")
        for room in all_rooms:
            print(room)

def print_bookings(all_bookings):
    if not all_bookings:
        print('No Bookings found')
    else:
        print(f"{'Bid':<10}{'User_id':<35}{'Room_id':<20}{'Booking date':<20}{'Check in Date':<20}{'Check out Date':<20}{'Status':<20}")
        for booking in all_bookings:
            print(booking)