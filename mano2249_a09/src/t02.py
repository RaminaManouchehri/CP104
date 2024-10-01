"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""
# Imports
from functions import file_integers
# Constants
fh = open("numbers.txt", "r", encoding="utf-8")
numbers = file_integers(fh)
print(numbers)
fh.close()
