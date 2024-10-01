"""
-------------------------------------------------------
Lab 4, Task 15
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""
# Imports
from functions import time_split
initial_seconds = int(input("Enter the initial number of seconds: "))
# Output
days, hours, minutes, seconds = time_split(initial_seconds)
print(f'({days:d}, {hours:d}, {minutes:d}, {seconds:d})')
