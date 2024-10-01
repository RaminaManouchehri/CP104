"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import product_largest
# Constants
v1 = float(input("Please enter the first number: "))
v2 = float(input("Please enter the second number: "))
v3 = float(input("Please enter the third number: "))
product = product_largest(v1, v2, v3)
print(f"{product:.0f}")
