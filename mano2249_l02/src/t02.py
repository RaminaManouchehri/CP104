"""
-------------------------------------------------------
[Lab 2, Task 2]
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-09-24"
-------------------------------------------------------
"""
# Imports

# Constants
WATER_FREEZING = 32
# Calculations
fahrenheit = int(input("Temperature (F): "))
celcius = int((fahrenheit - WATER_FREEZING) * (5 / 9))
# Output
print("Temperature (c): ", celcius)
