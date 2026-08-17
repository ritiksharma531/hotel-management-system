from controllers.booking_controller import BookingController
from controllers.hotel_controller import HotelController
from controllers.room_controller import RoomController


def admin_menu(user):
    user_input = ''
    booking_controller = BookingController()
    hotel_controller = HotelController()
    room_controller = RoomController()
    while user_input != '5':
        print(f'Welcome Admin'.rjust(70))
        print('Choose Option')
        print('1. View all hotels')
        print('2. Add hotel')
        print('3. Add room')
        print('4. View all bookings')
        print('5. Logout')
        user_input = input('Enter you choice: ')

        if user_input == '1':
            hotel_controller.view_all_hotels()

        elif user_input == '2':
            hotel_controller.add_hotel()

        elif user_input == '3':
            room_controller.add_room()

        elif user_input == '4':
            booking_controller.view_all_bookings()

        elif user_input == '5':
            print('Bye')

        else:
            print('Invalid choice, try again...')