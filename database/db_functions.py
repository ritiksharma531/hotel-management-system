import sqlite3

from database.db import getcursor


class DB:
    @staticmethod
    def get_item(query, *args):
        try:
            with getcursor() as cursor:
                cursor.execute(query, args)
                return cursor.fetchone()
        except sqlite3.Error as e:
            print(e)

    @staticmethod
    def get_items(query, *args):
        try:
            with getcursor() as cursor:
                cursor.execute(query, args)
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(e)

    @staticmethod
    def add_item(query, *args):
        try:
            with getcursor() as cursor:
                cursor.execute(query, args)
                return None

        except sqlite3.Error as e:
            print(e)

    @staticmethod
    def update_item(query, *args):
        try:
            with getcursor() as cursor:
                cursor.execute(query, args)
                return None

        except sqlite3.Error as e:
            print(e)
