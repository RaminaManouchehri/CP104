"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""
# Imports
from functions import file_stats
# Constants
fh = open("addresses.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()
print(ucount, lcount, dcount, wcount)
