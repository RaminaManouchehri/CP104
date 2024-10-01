"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""
# Imports
from functions import file_head
fh = open("functions.py", "r", encoding="utf-8")
file_head(fh, 5)
fh.close()
