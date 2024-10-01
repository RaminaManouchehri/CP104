"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-10"
-------------------------------------------------------
"""
# Imports

# Program
date_entered = int(input("Enter a date in the format DDMMYYYY: "))
day = date_entered // 1000000
date_entered = date_entered % 1000000
month = date_entered // 10000
date_entered = date_entered % 10000
year = date_entered
# Output
print(f"")
print(f"The reformatted date: {year:d}/{month:0>2.0f}/{day:0>2.0f}")
