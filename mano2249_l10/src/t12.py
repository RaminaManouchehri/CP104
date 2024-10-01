"""
-------------------------------------------------------
Lab 10, Task 12
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
# Imports
from functions import find_shortest
# Constant
fh = open('words.txt', 'r')
word = find_shortest(fh)
fh.close()
print(f"file 'words.txt' open for reading")
print(f"{word}' is the first shortest word")
