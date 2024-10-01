"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""
# Imports

# Constants
from functions import date_extract
date_number = int(input("Enter a date in the format MMDDYYYY: "))
year, month, day = date_extract(date_number)
print(f"")
print(f"The reformatted date: {year:d}/{month:0>2.0f}/{day:0>2.0f}")
