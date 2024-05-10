"""
This script calculates the displacement of an object using the formula s = ut + (1/2)at^2.

__author__ = "Jackson"
"""

# Given values
initial_velocity = 3  # m/s
time = 1  # s
acceleration = 2  # m/s^2

# Calculate displacement
displacement = initial_velocity * time + 0.5 * acceleration * time ** 2

# Print the result
print(f's(t = {time:.0f} s) = {displacement:.1f} m')

if __name__ == "__main__":
    # Test case: Input initial_velocity = 3 m/s, time = 1 s, acceleration = 2 m/s^2
    # Expected output: s(t = 1 s) = 4.5 m
    pass
