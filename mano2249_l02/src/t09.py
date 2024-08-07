"""
-------------------------------------------------------
[Lab 2, Task 9]
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-09-24"
-------------------------------------------------------
"""
# Imports

# Constants
PI = 3.14
# Program
diameter_base = float(input("Diameter of container base (cm): "))
height = float(input("Height of container (cm): "))
cost_materials = float(input("Cost of material ($/cm^2): "))
num_containers = int(input("Number of containers: "))
radius = diameter_base / 2
# Calculations
area_cylinder = (2 * PI * radius * height) + (PI * (radius ** 2))
one_cost = area_cylinder * cost_materials
all_cost = one_cost * num_containers
# Output
print("The total cost of one containers is $ ", one_cost)
print("The total cost of all containers is $ ", all_cost)
