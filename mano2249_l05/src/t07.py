"""
-------------------------------------------------------
Lab 5, Task 7
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import get_pay
# Constants
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))
net_payment = get_pay(hourly_rate, hours_worked)
print(f'{net_payment:.2f}')
