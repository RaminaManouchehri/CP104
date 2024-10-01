"""
-------------------------------------------------------
Lab 10, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-11-26"
-------------------------------------------------------
"""
# Imports
from functions import customer_append
# Constants
fh = open('customers.txt', 'a')
customer_append(fh,  ['35612', 'David', 'Brown', '237.56', '2008-10-10'])
fields = ['35612', 'David', 'Brown', '237.56', '2008-10-10']
fh.close()
print(fields)
print('data appended to file')
