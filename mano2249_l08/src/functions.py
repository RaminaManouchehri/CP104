"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-08"
-------------------------------------------------------
"""
# Imports


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    weekdays = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]
    name = weekdays[d - 1]

    return name


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = values[0]
    largest = values[0]
    total = values[0]
    for i in range(1, len(values)):
        if values[i] < smallest:
            smallest = values[i]
        if values[i] > largest:
            largest = values[i]
        total = total + values[i]
    average = total / len(values)
    return smallest, largest, total, average


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    positives = 0
    negatives = 0
    zeroes = 0
    evens = 0
    odds = 0
    for number in values:
        if number > 0:
            positives = positives + 1
        elif number < 0:
            negatives = negatives + 1
        else:
            zeroes = zeroes + 1

        if number % 2 == 0:
            evens = evens + 1
        else:
            odds = odds + 1
    return negatives, positives, zeroes, evens, odds


def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: target = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - source1 ⋅ source2 [source1 dot product source2] (float)
    -------------------------------------------------------
    """
    target = 0
    for i in range(len(source1)):
        target = target + (source1[i] * source2[i])
    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    for number in source1:
        if (number not in source2) and (number not in target):
            target.append(number)
    for number in source2:
        if (number not in source1) and (number not in target):
            target.append(number)
    return target
