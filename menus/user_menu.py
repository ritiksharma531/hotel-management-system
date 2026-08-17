from controllers.booking_controller import BookingController
from controllers.hotel_controller import HotelController
from controllers.room_controller import RoomController


def user_menu(user):
    user_input = ''
    booking_controller = BookingController()
    hotel_controller = HotelController()
    room_controller = RoomController()
    while user_input != '8':
        print(f'Welcome {user.name}'.rjust(70))
        print('Choose Option')
        print('1. View Hotels')
        print('2. Get available rooms')
        print('3. Book Room')
        print('4. View my bookings')
        print('5. Cancel booking')
        print('6. Check in')
        print('7. Check out')
        print('8. Logout')
        user_input = input('Enter you choice: ')

        if user_input == '1':
            hotel_controller.view_all_hotels()

        elif user_input == '2':
            hotel_controller.get_available_rooms()

        elif user_input == '3':
            room_controller.book_room(user)

        elif user_input == '4':
            booking_controller.view_my_bookings(user)

        elif user_input == '5':
            room_controller.cancel_room_booking(user)

        elif user_input == '6':
            room_controller.check_in(user)

        elif user_input == '7':
            room_controller.check_out(user)

        elif user_input == '8':
            print('Bye!!')

        else:
            print('Invalid choice, try again')