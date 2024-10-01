"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-04"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 1
    guess = int(input("Guess: "))
    while guess != number:
        if guess > number:
            print(f"Too high, try again.")
        else:
            print(f"Too low, try again.")

        count = count + 1
        guess = int(input("Guess: "))
    print(f"Congratulations - good guess!")
    print(f"You made {count} guesses.")
    return count


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    num = 1
    final = 0
    while final < target:
        final = final + num * num
        num = num + 1
    if target <= 0:
        final = 1
    return final


def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """
    negatives = 0
    zeroes = 0
    positives = 0
    entered = float(input("First value: "))
    while entered != -999:
        if entered > 0:
            positives = positives + 1
        elif entered < 0:
            negatives = negatives + 1
        else:
            zeroes = zeroes + 1
        entered = float(input("Next value: "))
    return negatives, zeroes, positives


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    data = "Y"
    day = 1
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0
    while data == "Y":
        print(f"For Day {day}")
        print("")
        day = day + 1
        breakfast = float(input("How much was breakfast? $"))
        b_total = b_total + breakfast
        lunch = float(input("How much was lunch? $"))
        l_total = l_total + lunch
        supper = float(input("How much was supper? $"))
        s_total = s_total + supper
        total = breakfast + lunch + supper
        print(f"Your total for the day was ${total:.2f}")
        print("")
        data = input("Were you away another day (Y/N)? ")
        print("")
    a_total = b_total + l_total + s_total
    return b_total, l_total, s_total, a_total


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f"Enter a value between {low} and high {high}: "))
    while value < low or value > high:
        if value > high:
            print("Value entered is too high")
        else:
            print("Value entered is too low")
        value = int(input(f"Enter a value between {low} and high {high}: "))
    return value
