"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import pollution_level
# Constants
aqi = int(input("Please enter the Air Quality Index: "))
level = pollution_level(aqi)
print(f'{level}')
