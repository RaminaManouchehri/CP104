"""
-------------------------------------------------------
Lab 5, Task 12
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import pay_raise
# Constants
status = input("Enter status, Full Time (F) or Part Time (P): ")
years = int(input("Enter number of years employed: "))
salary = float(input("Enter current salary: "))
new_salary = pay_raise(status, years, salary)
print(f"{new_salary:.2f}")
