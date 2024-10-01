"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-05"
-------------------------------------------------------
"""
# Imports
from functions import range_total
# Constants
start = int(input("Start: "))
increment = int(input("Increment: "))
count = int(input("Count: "))
total = range_total(start, increment, count)
print(f'{total}')
