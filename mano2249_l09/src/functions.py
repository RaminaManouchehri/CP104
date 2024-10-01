"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    upper = 0
    lower = 0
    digit = 0
    length = len(password)
    for c in password:
        if c.isupper():
            upper = upper + 1
        if c.islower():
            lower = lower + 1
        if c.isdigit():
            digit = digit + 1
    if length < 8:
        print(f'not long enough')
    if digit == 0:
        print(f'no digits')
    if upper == 0:
        print(f'no upper case')
    if lower == 0:
        print(f'no lower case')
    return


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0
    vowels = "aeiouAEIOU"
    for c in s:
        if c in vowels:
            count = count + 1
    return count


def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """
    count = 0
    special_characters = "#@$%&!"
    for c in s:
        if c in special_characters:
            count = count + 1
    return count


def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out = ""
    for c in string:
        if c == ",":
            out = out + "."
        else:
            out = out + c
    return out


def total_digits(string):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in string.
    Use: total = total_digits(string)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in string (int)
    ------------------------------------------------------
    """
    total = 0
    for c in string:
        if c.isdigit():
            total = total + int(c)
    return total
