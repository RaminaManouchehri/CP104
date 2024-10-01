"""
-------------------------------------------------------
Lab 10, Task 8
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
# Imports
from functions import append_increment
# Constants
fh = open('numbers.txt', 'r+')
num = append_increment(fh)
fh.close()
print(f"file 'numbers.txt' open for reading and writing")
print(f"{num} is appended")
