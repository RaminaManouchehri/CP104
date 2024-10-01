"""
-------------------------------------------------------
Assignment 3, Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""
# Imports
from random import randint

# Constants
FEET_ACRES = 43560


def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = square_footage / FEET_ACRES
    return acres


def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    time = width * length / speed
    return time


def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    month = date_number // 1000000
    date_number = date_number % 1000000
    day = date_number // 10000
    date_number = date_number % 10000
    year = date_number
    return year, month, day


def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:                                                                            
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    numerator = num1 * num2
    denominator = denom1 * denom2
    product = (num1 / denom1) * (num2 / denom2)
    return numerator, denominator, product


def math_quiz():
    """
    -------------------------------------------------------
    Creates a simple math quiz by displaying two random integers between 0 and 999 that are to be added
    Use: math_quiz()
    -------------------------------------------------------
    Parameters: none
    Returns: none
    ------------------------------------------------------
    """
    number1 = randint(0, 999)
    number2 = randint(0, 999)
    expected = int(number1 + number2)

    print(f'   {number1:>3}')
    print(f'   {number2:>3}')
    print(f'')
    answer = input("Your answer: ")
    print(f'')
    print(f'Your answer: {answer:>5}')
    print(f'Expected:    {expected:>5}')
    return
