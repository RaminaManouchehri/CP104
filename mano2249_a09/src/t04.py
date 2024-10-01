"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""
# Imports
from functions import number_lines
# Constants
fh_in = open("wilde.txt", "r", encoding="utf-8")
fh_out = open("wilde_numbered.txt", "w", encoding="utf-8")
number_lines(fh_in, fh_out)
fh_in.close()
fh_out.close()
