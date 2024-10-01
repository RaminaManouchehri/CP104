"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-12-20"
-------------------------------------------------------
"""
# Imports
import string
import random


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.choice(string.ascii_lowercase))
        matrix.append(row)
    return matrix


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    print('  ', end='')
    for i in range(len(matrix[0])):
        print('    ', end='')
        print(i, end='')
    print('')
    for i in range(len(matrix)):
        print('', i, end='')
        for j in range(len(matrix[i])):
            print('    ', end='')
            print(matrix[i][j], end='')
        print('')
    return


def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    matrix = []
    for i in range(len(word_list)):
        row = []
        for j in range(len(word_list[0])):
            row.append(word_list[i][j])  # add value to row
        matrix.append(row)
    return matrix


def find_word_horizontal(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
    Use: rows = find_word_horizontal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        rows - a list of row indexes (list of int)
    ------------------------------------------------------
    """
    rows = []
    word2 = ''
    for i in range(len(matrix)):
        word2 = ''
        for j in range(len(matrix[0])):
            word2 = word2 + matrix[i][j]
        if word2 == word:
            rows.append(i)
    return rows


def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of *)
        matrix2 - the second matrix (2D list of *)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    score = 0
    if (len(matrix1)) == len(matrix2):
        for i in range(len(matrix1)):
            word1 = ''
            word2 = ''
            if (len(matrix1[i])) == (len(matrix2[i])):
                for j in range(len(matrix1[0])):
                    word1 = word1 + str(matrix1[i][j])
                    word2 = word2 + str(matrix2[i][j])
                if word1 != word2:
                    score = score + 1
            else:
                score = 1
    else:
        score = 1

    if score == 0:
        equal = True
    else:
        equal = False

    return equal
