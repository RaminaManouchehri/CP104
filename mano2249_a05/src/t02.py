"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-04"
-------------------------------------------------------
"""
# Imports
from functions import calories_burned

per_minute = float(input("Enter calories burnt per minute: "))
minutes = int(input("Enter total number of minutes run: "))
calories_burned(per_minute, minutes)
