"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""
# Imports
from functions import mow_lawn
# Constants
width = float(input("Width (m): "))
length = float(input("Length (m): "))
speed = float(input("Speed (m^2/minute): "))
time = mow_lawn(width, length, speed)
print(f'')
print(f'Mowing the lawn takes {time:.0f} minutes')
