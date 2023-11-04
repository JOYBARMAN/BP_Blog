"""Some utils function of core app"""

import re


def is_valid_bd_phone_num(phone):
    # Define a regular expression pattern for a valid Bangladeshi phone number
    pattern = r"^\+?(88)?01[3-9]\d{8}$"

    # Use the re.match() function to check if the phone number matches the pattern
    return bool(re.match(pattern, phone))
