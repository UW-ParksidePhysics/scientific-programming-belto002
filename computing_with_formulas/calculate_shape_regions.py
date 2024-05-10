"""
This script calculates the areas of a parallelogram, square, and circle, as well as the volume of a cone.

__author__ = "Jackson"
"""

from math import pi

if __name__ == "__main__":
    # Test case
    # Input: height, base, radius
    # Expected output: Area of parallelogram, square, and circle; volume of cone

    # Given dimensions
    height = 5.0  # cm
    base = 2.0    # cm
    radius = 1.5  # cm

    # Calculate areas and volume
    parallelogram_area = height * base
    square_area = base ** 2
    circle_area = pi * radius ** 2
    cone_volume = (1. / 3) * pi * radius ** 2 * height

    # Output results
    print(f'The area of a parallelogram of height {height} and base {base} cm is {parallelogram_area:3.2f} cm^2')
    print(f'The area of a square of base {base} cm is {square_area:3.2f} cm^2')
    print(f'The area of a circle of radius {radius} cm is {circle_area:3.2f} cm^2')
    print(f'The volume of a cone of radius {radius} cm and height {height} cm is {cone_volume:3.2f} cm^3')
