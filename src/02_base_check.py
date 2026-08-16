import re

"""
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

- The string may contain integers, and uppercase or lowercase characters.
- The check should be case-insensitive.
- The base can be any number 2-36.
- A number is valid if every character is a valid digit in the given base.
- Example of valid digits for bases:
    - Base 2: 0-1
    - Base 8: 0-7
    - Base 10: 0-9
    - Base 16: 0-9 and A-F
    - Base 36: 0-9 and A-Z
"""

def is_valid_number(n: str, base: int):
    if base == 2:
        return bool(re.fullmatch('[01]+', n))
    elif base == 8:
        return bool(re.fullmatch('[0-7]+', n))
    elif base == 10:
        return bool(re.fullmatch('[0-9]+', n))
    elif base == 16:
        return bool(re.fullmatch('[0-9A-Fa-f]+', n))
    elif base == 17:
        return bool(re.fullmatch('[0-9A-Ga-g]+', n))
    elif base == 20:
        return bool(re.fullmatch('[0-9A-Ja-j]+', n))
    elif base == 36:
        return bool(re.fullmatch('[0-9A-Za-z]+', n))
    else: return False
