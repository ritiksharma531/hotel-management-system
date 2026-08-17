import getpass
import re
from datetime import datetime, date


def validate_input(prompt, validator, error_msg):
    while True:
        user_input = input(prompt).strip()
        if validator(user_input):
            return user_input
        print(error_msg)


def is_valid_date(input_date, fmt = '%d-%m-%Y'):
    try:
        given_date = datetime.strptime(input_date, fmt).date()
        return given_date >= date.today()
    except ValueError:
        return False


def validate_password(prompt, validator, error_msg):
    while True:
        user_input = getpass.getpass(prompt, echo_char='*').strip()
        if validator(user_input):
            return user_input
        print(error_msg)

def password_regex(pswd):
    if len(pswd) < 8 or len(pswd) > 30:
        return False
    if not re.search(r'[A-Z]', pswd):
        return False
    if not re.search(r'[a-z]', pswd):
        return False
    if not re.search(r'[0-9]', pswd):
        return False
    if not re.search(r'[!@#$%^&*]', pswd):
        return False
    return True