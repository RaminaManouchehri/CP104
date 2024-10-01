"""
-------------------------------------------------------
Lab 7, Task 9
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-04"
-------------------------------------------------------
"""
# Imports
from functions import get_int
# Constants
low = int(input("Enter lowest value: "))
high = int(input("Enter highest value: "))
print("")
value = get_int(low, high)
print("")
print(f'{value}')
