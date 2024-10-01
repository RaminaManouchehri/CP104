"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2022-10-10"
-------------------------------------------------------
"""
# Imports

# Constants
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
concrete_cost = float(input("Cost of concrete ($/m^3): "))
brick_cost = float(input("Cost of bricks ($/m^2): "))

concrete_needed = foundation_length * foundation_width * foundation_height
concrete_total_cost = concrete_needed * concrete_cost
bricks_needed = ((wall_height * foundation_length) * 2) + \
    ((wall_height * foundation_width) * 2)
bricks_total_cost = bricks_needed * brick_cost
total_cost = concrete_total_cost + bricks_total_cost
print("")
print(f"Concrete needed for foundation (m^3): {concrete_needed:.2f}")
print(f"Cost of concrete: ${concrete_total_cost:,.2f}")
print(f"Bricks needed for walls (m^2): {bricks_needed:.2f}")
print(f"Cost of bricks: ${bricks_total_cost:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
