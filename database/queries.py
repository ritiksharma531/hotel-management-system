IS_HOTEL_EXIST = 'SELECT * FROM hotel WHERE name = ?'
GET_HOTEL = 'SELECT * FROM hotel WHERE hid = ?'
ADD_HOTEL = 'INSERT INTO hotel(name, rating) VALUES(?, ?)'
GET_ROOMS = 'SELECT * FROM room WHERE hid = ? AND status = ?'
GET_USER = 'SELECT * FROM user WHERE mobile = ?'
ADD_USER = 'INSERT INTO user(name, mobile) VALUES(?, ?)'
ADD_AUTH = 'INSERT INTO auth(uid, password, role) VALUES(?, ?, ?)'
GET_PASS = 'SELECT password, role FROM auth WHERE uid = ?'
GET_HOTELS = 'SELECT * FROM hotel'
ADD_ROOM = 'INSERT INTO room(room_type, price, status, hid) VALUES(?, ?, ?, ?)'
GET_AVAILABLE_ROOM = "SELECT * FROM room WHERE room_id = ? AND status = 'available'"
BOOK_ROOM = "UPDATE room SET status = 'booked' WHERE room_id = ?"
ADD_BOOKING = 'INSERT INTO booking(uid, room_id, booking_date, check_out_date, status) VALUES(?, ?, ?, ?, ?)'
CHECK_IN = "UPDATE booking SET check_in_date = ?, status = 'checked_in' WHERE uid = ? AND room_id = ?"
CHECK_OUT_BOOKING = "UPDATE booking SET check_out_date = ?, status = 'completed' WHERE uid = ? AND room_id = ?"
UPDATE_ROOM_COMPLETED = "UPDATE room SET status = 'available' WHERE room_id = ? AND status = 'booked'"
GET_BOOKING = "SELECT * FROM booking WHERE uid = ? AND room_id = ? AND (status = 'booked' OR status = 'checked_in')"
CANCEL_BOOKING = "UPDATE booking SET status = 'cancelled' WHERE uid = ? AND room_id = ?"
GET_MY_BOOKINGS = 'SELECT * FROM booking WHERE uid = ?'
GET_BOOKINGS = 'SELECT * FROM booking'