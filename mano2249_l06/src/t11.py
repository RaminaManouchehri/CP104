"""
-------------------------------------------------------
Lab 6, Task 11
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-26"
-------------------------------------------------------
"""
# Imports
from functions import retirement
# Constants
age = int(input("Enter worker's current age: "))
salary = float(input("Enter worker's current salary: "))
increase = float(input("Enter percent increase in salary per year: "))
retirement(age, salary, increase)
