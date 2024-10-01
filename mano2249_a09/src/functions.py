"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""
# Imports

# Constants


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 1
    line = fh.readline()
    print(line, end='')
    while i < linecount:
        i = i + 1
        line = fh.readline()
        print(line, end='')
    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    numbers = []
    line = fh.readline()
    while line != "":
        num = line.strip().split(',')
        for i in range(len(num)):
            if num[i].isdigit():
                numbers.append(int(num[i]))
        line = fh.readline()
    return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    line = fh.readline()
    while line != "":
        line1 = line.strip()
        for i in range(len(line1)):
            if line1[i] == " ":
                wcount += 1
            if line1[i].isalpha():
                if line1[i].isupper():
                    ucount += 1
                else:
                    lcount += 1
            if line1[i].isdigit():
                dcount += 1
        line = fh.readline()
    return ucount, lcount, dcount, wcount


def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    num = -1
    line = fh_in.readline()
    while line != "":
        num += 1
        write1 = "[" + str(num) + "]" + " " + line
        fh_out.write(write1)
        line = fh_in.readline()
    return


def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    lines = 1
    result = students.readline().strip().split(',')
    result2 = result
    l_id = result2[2]
    h_id = result[2]
    avg = int(result[3])
    line = students.readline()
    while line != '':
        lines = lines + 1
        num = line.strip().split(',')
        num2 = num
        avg = avg + int(num[3])
        if float(num[3]) > float(result[3]):
            result = num
            h_id = num[2]
        if float(num2[3]) < float(result2[3]):
            result2 = num2
            l_id = num2[2]
        line = students.readline()
    avg = avg / lines
    l_id = str(l_id)
    h_id = str(h_id)
    return l_id, h_id, avg
