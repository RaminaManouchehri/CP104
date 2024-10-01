"""
-------------------------------------------------------
Assignment 5, Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-16"
-------------------------------------------------------
"""
# Imports

# Constants


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, num + 1):
        product = product * i
    return product


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five minutes
    Use: calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute -  the number of calories burned per minute (float)
        minutes - the total number of minutes run (int)
    Returns:
        none
    ------------------------------------------------------
    """
    for i in range(5, minutes + 1, 5):
        calories = i * per_minute
        print(f'  {i:2}:  {calories:.1f}')
    return


def open_triangle(num_rows):
    """
    -------------------------------------------------------
    Takes an integer parameter and prints a triangle of # characters with an empty center
    Use: open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows -  the number of rows (int)
    Returns:
        none
    ------------------------------------------------------
    """
    for i in range(num_rows):
        print("#" + (" " * i) + "#")
    return


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("   ", end="")
    for i in range(start, stop + 1):
        print(f"{i:4d}", end=" ")
    print()
    print(f"  -------------------------")
    for j in range(start, stop + 1):
        for k in range(start, stop + 1):
            multiple = j * k
            if k == start:
                line = str(j) + "|"
            else:
                line = ""
            print(f"{line}", f'{multiple:4d}', end="")
        print()
    return


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total = total + start
        start = start + increment
    return total
