"""
-------------------------------------------------------
Assignment 4, Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns a string representing the corresponding day of the week:
        "Monday" - day_number is 1
        "Tuesday" - day_number is 2
        "Wednesday" - day_number is 3
        "Thursday" - day_number is 4
        "Friday" - day_number is 5
        "Saturday" - day_number is 6
        "Sunday" - day_number is 7
    Returns "Error" if day_number is greater than seven.
    Use: weekday = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - number of the day of the week (int)
    Returns:
        weekday - name of the day of the week (str)
    ------------------------------------------------------
    """
    WEEK_DAY1 = "Monday"
    WEEK_DAY2 = "Tuesday"
    WEEK_DAY3 = "Wednesday"
    WEEK_DAY4 = "Thursday"
    WEEK_DAY5 = "Friday"
    WEEK_DAY6 = "Saturday"
    WEEK_DAY7 = "Sunday"
    INVALID_WEEKDAY = "Error"
    if day_number == 1:
        weekday = WEEK_DAY1
    elif day_number == 2:
        weekday = WEEK_DAY2
    elif day_number == 3:
        weekday = WEEK_DAY3
    elif day_number == 4:
        weekday = WEEK_DAY4
    elif day_number == 5:
        weekday = WEEK_DAY5
    elif day_number == 6:
        weekday = WEEK_DAY6
    elif day_number == 7:
        weekday = WEEK_DAY7
    else:
        weekday = INVALID_WEEKDAY
    return weekday


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    GOOD_AIR = "Good"
    MODERATE_AIR = "Moderate"
    SENSITIVE_AIR = "Unhealthy for Sensitive Groups"
    UNHEALTHY_AIR = "Unhealthy"
    VERY_UNHEALTHY_AIR = "Very Unhealthy"
    HAZARDOUS_AIR = "Hazardous"
    INVALID_AIR = "Error"
    if 0 <= aqi <= 50:
        level = GOOD_AIR
    elif 51 <= aqi <= 100:
        level = MODERATE_AIR
    elif 101 <= aqi <= 150:
        level = SENSITIVE_AIR
    elif 151 <= aqi <= 200:
        level = UNHEALTHY_AIR
    elif 201 <= aqi <= 300:
        level = VERY_UNHEALTHY_AIR
    elif aqi > 300:
        level = HAZARDOUS_AIR
    else:
        level = INVALID_AIR
    return level


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    if v1 > v2 and v1 > v2:
        if v2 > v3:
            product = v1 * v2
        else:
            product = v1 * v3
    elif v2 > v1 and v2 > v3:
        if v1 > v3:
            product = v2 * v1
        else:
            product = v2 * v3
    else:
        if v1 > v2:
            product = v3 * v1
        else:
            product = v3 * v2
    return product


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    RED_BLUE = "fushia"
    RED_GREEN = "yellow"
    GREEN_BLUE = "aqua"
    RED_RED = "red"
    BLUE_BLUE = "blue"
    GREEN_GREEN = "green"
    INVALID = "Error"
    if rgb1 == "red":
        if rgb2 == "blue":
            colour = RED_BLUE
        elif rgb2 == "green":
            colour = RED_GREEN
        elif rgb2 == "red":
            colour = RED_RED
        else:
            colour = INVALID
    elif rgb1 == "green":
        if rgb2 == "red":
            colour = RED_GREEN
        elif rgb2 == "blue":
            colour = GREEN_BLUE
        elif rgb2 == "green":
            colour = GREEN_GREEN
        else:
            colour = INVALID
    elif rgb1 == "blue":
        if rgb2 == "red":
            colour = RED_BLUE
        elif rgb2 == "green":
            colour = GREEN_BLUE
        elif rgb2 == "blue":
            colour = BLUE_BLUE
        else:
            colour = INVALID
    else:
        colour = INVALID
    return colour


def yee_ha(number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns one of the following strings:
    "Yee" if number is evenly divisible by 3
    "Ha" if number is evenly divisible by 7
    "Yee Ha" if number is evenly divisible by both 3 and 7
    "Nada" if number is none of the above
    Use: phrase = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - a number (int)
    Returns:
        phrase - the phrase depending on that number is entered (string)
    ------------------------------------------------------
    """
    THREE_DIVIDE = "Yee"
    SEVEN_DIVIDE = "Ha"
    BOTH_DIVIDE = "Yee Ha"
    NO_DIVIDE = "Nada"
    if number % 3 == 0:
        if number % 7 == 0:
            phrase = BOTH_DIVIDE
        else:
            phrase = THREE_DIVIDE
    elif number % 7 == 0:
        if number % 3 == 0:
            phrase = BOTH_DIVIDE
        else:
            phrase = SEVEN_DIVIDE
    else:
        phrase = NO_DIVIDE
    return phrase
