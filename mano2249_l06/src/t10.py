"""
-------------------------------------------------------
Lab 6, Task 10
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-26"
-------------------------------------------------------
"""
# Imports
from functions import treadmill
# Constants
burnt_per_minute = float(input("Enter calories burnt per minute: "))
start = int(input("Enter start time in minutes: "))
end = int(input("Enter end time in minutes: "))
inc = int(input("Enter increment in minutes: "))
treadmill(burnt_per_minute, start, end, inc)
