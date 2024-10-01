"""
-------------------------------------------------------
Assignment 7, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""
# Imports
from functions import is_sorted
from functions import list_positives
# Constants
numbers = list_positives()
in_order, index = is_sorted(values)
print(f'{in_order}, {index}')
