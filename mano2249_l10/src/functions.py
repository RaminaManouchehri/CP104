"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
# Imports

# Constants


def customer_best(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    result = fh.readline().strip().split(',')
    line = fh.readline()
    while line != "":
        num = line.strip().split(',')
        if float(num[3]) > float(result[3]):
            result = num
        line = fh.readline()
    return result


def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    record_string = (
        f'\n{fields[0]},{fields[1]},{fields[2]},{fields[3]},{fields[4]}')
    fh.write(record_string)
    return


def append_increment(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of the fh. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    line = fh.readline()
    while line != '':
        num = int(line.strip())
        line = fh.readline()
    num = num + 1
    fh.write(f'\n{num}')
    return num


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    word = fh.readline().strip()
    size = len(word)
    line = fh.readline()
    while line != '':
        line = line.strip()
        size2 = len(line)
        if size2 < size:
            word = line
            size = size2
        line = fh.readline()
    return word


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    line = fh_1.readline()
    i = 0
    while line != "" and i < n:
        fh_2.write(line)
        i = i + 1
        line = fh_1.readline()
    return
