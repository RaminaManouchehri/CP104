"""
-------------------------------------------------------
Lab 6, Task 15
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-08"
-------------------------------------------------------
"""
# Imports
from functions import statistics
# Constants
n = int(input("Enter number of values to process: "))
minimum, maximum, total, average = statistics(n)
print("")
print(f'({minimum:.2f}, {maximum:.2f}, {total:.2f}, {average:.2f})')
