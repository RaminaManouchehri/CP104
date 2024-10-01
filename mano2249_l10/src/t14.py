"""
-------------------------------------------------------
Lab 10, Task 14
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
# Imports
from functions import file_copy_n
# Constants
print(f"Copying 'words.txt' to 'new_words.txt'")
n = int(input("Number of lines to copy: "))

fh_1 = open("words.txt", "r")
fh_2 = open("new_words.txt", "w")

file_copy_n(fh_1, fh_2, n)

fh_1.close()
fh_2.close()
