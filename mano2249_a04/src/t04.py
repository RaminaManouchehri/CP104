"""
-------------------------------------------------------
Assignment 4, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import rgb_mix

rgb1 = input("Please enter the first primary colour: ")
rgb2 = input("Please enter the second primary colour: ")

colour = rgb_mix(rgb1, rgb2)
print(f'{colour}')
