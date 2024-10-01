"""
-------------------------------------------------------
[Lab 3, Task 6]
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-09-27"
-------------------------------------------------------
"""
# Imports

# Constants

# Program
cost = float(input("Enter a Cost: $"))
quantity = int(input("Enter quantity: "))
total = cost * quantity
print(
    f'Given a cost of ${cost:.2f} and a quantity of {quantity:d} the total is ${total:.2f}')
