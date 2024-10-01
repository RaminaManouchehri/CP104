"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    new_string = ''
    for c in range(len(string)):
        letter = string[c]
        if c != 0:
            if letter.isupper():
                new_string = new_string + ' ' + letter.lower()
            else:
                new_string = new_string + letter
        else:
            new_string = new_string + letter
    return new_string


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    length = len(string) - 1
    if (string.endswith('s')) or (string.endswith('sh')) or (string.endswith('ch')):
        string = string + 'ies'
    elif (string.endswith('y')) and (string.endswith('ay') is False) and (string.endswith('oy') is False):
        string = string[0: length:]
        string = string + 'ies'
    else:
        string = string + 's'
    plural = string
    return plural


def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    common = ''
    i = (len(string1)) - 1
    j = (len(string2)) - 1
    end = True
    while end is True:
        if string1[i] == string2[j]:
            common = common + string1[i]
        else:
            end = False
        i = i - 1
        j = j - 1
    common = common[::-1]
    return common


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    length = len(isbn)
    for i in range(len(isbn)):
        char = isbn[i]
        if (char.isdigit()) or (char == '-'):
            digit_dash = True
        else:
            digit_dash = False
        if (isbn[i] == '-'):
            if isbn[i + 1].isdigit():
                count = True
            else:
                count = False
    if isbn[length - 2] == "-":
        last_digit = True
    else:
        last_digit = False
    if isbn.startswith("978") or isbn.startswith("979"):
        start = True
    if (count) and (digit_dash) and (last_digit) and (start) and (length == 17):
        valid = True
    else:
        valid = False
    return valid


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    no = 0
    for i in range(len(word_list)):
        word = word_list[i]
        length = len(word) - 1
        letter = word[length]
        if i != (len(word_list) - 1):
            word2 = word_list[i + 1]
            if word2[0] != letter:
                no = no + 1
    if no != 0:
        word_chain = False
    else:
        word_chain = True
    return word_chain
