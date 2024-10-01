"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""
# Imports

# Constants
from functions import feet_to_acres
square_footage = float(input("Square footage: "))
acres = feet_to_acres(square_footage)
print(f'')
print(f"{acres:.2f} acres is equivalent to {square_footage:,.2F} square feet")
