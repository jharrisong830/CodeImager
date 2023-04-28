""" NAME:   utilities.py
    AUTHOR: John Graham
    DATE:   04/27/23    """


from math import sqrt, ceil
from random import seed, randint



def color_randomizer(val: int) -> tuple:
    """assigns (pseudo) random values to red, green, and blue color values,
    given that the sum of these three values shall not exceed 'val'\n
    RETURNS:    tuple, of (R, B, G) values"""
    seed()
    red=randint(0, val)
    green=randint(0, val-red)
    blue=val-red-green
    return red, green, blue

def color_tuple(val: int, color: str) -> tuple:
    """returns the proper RGB-tuple encoding according to the provided
    'val' and 'color' format\n
    RETURNS:    tuple, of (R, B, G) values"""
    match color:
        case "r": return val, 0, 0
        case "g": return 0, val, 0
        case "b": return 0, 0, val
        case "all": return color_randomizer(val)

def get_dimensions(length: int) -> tuple:
    """calculates the dimensions of the resulting image, given the 'length'
    of bytes of the file\n
    RETURNS:    tuple, of (width, height) pixel dimensions"""
    closest_square=ceil(sqrt(length))
    return closest_square, closest_square