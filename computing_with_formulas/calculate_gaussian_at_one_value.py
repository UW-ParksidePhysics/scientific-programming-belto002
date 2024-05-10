"""
This script calculates the value of the Gaussian function for a given mean, standard deviation, and input value.

__author__ = "Jackson"
"""

import math

if __name__ == "__main__":
    # Test case
    # Input: m = 0, s = 2, x = 1
    # Expected output: Gaussian Value at x = 1 : <calculated value>
    m = 0
    s = 2
    x = 1

    gaussian_value = 1 / (math.sqrt(2 * math.pi) * s) * math.exp(-0.5 * ((x - m) / s) ** 2)

    print("Mean:", m)
    print("Standard Deviation:", s)
    print("Input Value:", x)
    print("Gaussian Value at x =", x, ":", gaussian_value)
