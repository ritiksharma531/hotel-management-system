import sqlite3
import hashlib

class Database:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if not hasattr(self,"connection"):
            self.connection=sqlite3.connect('hotel.db')
            self.connection.execute('PRAGMA foreign_keys = ON')

class getcursor:
    def __enter__(self):
        self.connection = Database().connection
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()


def initialize_db():
    cursor = Database().connection.cursor()
    cursor.executescript("""
    pragma foreign_keys = on;
    create table if not exists hotel(
        hid integer primary key autoincrement,
        name text not null unique,
        rating integer check(rating <=5 and rating >= 1) not null
    );
        create table if not exists room(
            room_id integer primary key autoincrement,
            room_type text not null,
            price integer not null,
            status text,
            hid integer,
            constraint fk_hid foreign key(hid) references hotel(hid)
    );
        create table if not exists user(
            uid integer primary key autoincrement,
            name text not null,
            mobile text unique
    );
        create table if not exists booking(
            bid integer primary key autoincrement,
            uid integer,
            room_id integer,
            booking_date date,
            check_in_date date,
            check_out_date date,
            status text,
            constraint fk_uid foreign key(uid) references user(uid),
            constraint fk_room foreign key(room_id) references room(room_id)
    );
        create table if not exists auth(
            uid integer primary key,
            password text,
            role text,
            constraint fk_uid foreign key(uid) references user(uid)
        );
    """)
    cursor.execute("insert or ignore into user values(1, 'ADMIN', 9165860333)")
    admin_password_hash = hashlib.sha256("Asdf1234!@".encode()).hexdigest()
    cursor.execute("insert or ignore into auth values(1, ?, 'admin')", (admin_password_hash,))