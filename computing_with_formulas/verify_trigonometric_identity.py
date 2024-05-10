"""
This script calculates the value of sin^2(angle) + cos^2(angle) to verify it equals 1.

__author__ = "Jackson"
"""

import math

if __name__ == "__main__":
    # Test case
    # Input: angle = pi/4
    # Expected output: "sin^2(pi/4) + cos^2(pi/4) = 1.000"

    # Define angle in radians
    angle = math.pi / 4

    # Calculate the value of sin^2(angle) + cos^2(angle)
    unit_value = math.sin(angle) ** 2 + math.cos(angle) ** 2

    # Print the result
    print(f'sin^2({angle:.3f}) + cos^2({angle:.3f}) = {unit_value:.3f}')
