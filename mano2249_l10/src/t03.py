"""
-------------------------------------------------------
Lab 10, Task 3
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
# Imports
from functions import customer_best
# Constants

fh = open('customers.txt', 'r')

result = customer_best(fh)
print(f'Find customer with largest balance: ')
print(result)
fh.close()
