"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import day_of_week

day_number = int(input("Please enter number of the day of the week: "))
weekday = day_of_week(day_number)
print(f'{weekday}')
