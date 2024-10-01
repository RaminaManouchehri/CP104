"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-27"
-------------------------------------------------------
"""
# Imports

# Constants
total = 0

num = int(input("number: "))
for i in range(1, num + 1):
    if i % 2 != 0:
        total = total + i
print(total)
