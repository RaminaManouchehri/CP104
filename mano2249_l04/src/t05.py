"""
-------------------------------------------------------
Lab 4, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-05"
-------------------------------------------------------
"""
# Imports
from functions import right_triangle
adjacent = float(input("Enter adjacent side: "))
opposite = float(input("Enter opposite side: "))
# Constants
hyp, circ, area = right_triangle(adjacent, opposite)
print(f"({hyp:.1f}, {circ:.1f}, {area:.1f})")
