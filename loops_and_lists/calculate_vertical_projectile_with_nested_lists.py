"""
This module contains functions for working with time and position data.

__author__ = "Jackson"
"""

# separate lists of t and y values
times = [0.000, 0.177, 0.354, 0.531, 0.708, 0.885, 1.062, 1.239, 1.416]
positions = [0.000, 1.549, 2.656, 3.319, 3.541, 3.319, 2.656, 1.549, 0.000]

# store t and y in a nested list
times_positions = [times, positions]

# make a table with t and y values
print("t (s)\ty (m)")
for i in range(len(times)):
    print(f"{times_positions[0][i]:.3f}\t{times_positions[1][i]:.3f}")

# make a list of table rows
table_rows = list(zip(times_positions[0], times_positions[1]))

# Loop over the list and print t and y values
print("\nUsing table_rows list:")
print("t (s)\ty (m)")
for row in table_rows:
    print(f"{row[0]:.3f}\t{row[1]:.3f}")

if __name__ == "__main__":
    # Test case
    # Input: Lists of time and position values
    # Output: Printed tables showing time and position values
    pass
