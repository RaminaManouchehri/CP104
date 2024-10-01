"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-21"
-------------------------------------------------------
"""
# Imports

# Constants


def list_factors(num):
    """
    -------------------------------------------------------
    Returns a list of the factors that make up that number 
    excepting the number itself
    Use: list_factor = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - an integer greater than 0
    Returns:
        list_factors
    ------------------------------------------------------
    """
    factor = 0
    list_factor = []
    while factor < num:
        factor = factor + 1
        if (num % factor) == 0 and (factor != num):
            list_factor.append(factor)
    return list_factor


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    num = 1
    numbers = []
    while num != 0:
        num = int(input("Enter a positive number: "))
        if num > 0:
            numbers.append(num)
    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []
    for i in range(len(values)):
        if values[i] == target:
            locations.append(i)
    return locations


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in minuend[:]:
        if i in subtrahend:
            minuend.remove(i)
    return


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    indexs = []
    order = values[:]
    order.sort()
    for i in range(len(values)):
        for j in range(len(order)):
            if values[i] == order[j]:
                in_order = True
            else:
                in_order = False
                indexs.append(i)
    if in_order:
        index = -1
    else:
        index = indexs[0]
        index = index + 1
    return in_order, index
