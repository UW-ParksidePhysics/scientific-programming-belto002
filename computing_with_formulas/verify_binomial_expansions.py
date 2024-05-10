"""
This script performs verification of algebraic expressions.

__author__ = "Jackson"
"""

if __name__ == "__main__":
    # Test cases
    # Input: a = 3, b = 5
    # Expected output: "(a+b)**2 = a**2 + 2*a*b + b**2 is True"
    #                  "(a-b)**2 = a**2 - 2*a*b + b**2 is True"

    # Define values of a and b
    a = 3
    b = 5

    # Verify (a+b)**2 = a**2 + 2*a*b + b**2
    left = (a + b) ** 2
    right = a ** 2 + 2 * a * b + b ** 2
    print("(a+b)**2 = a**2 + 2*a*b + b**2 is", left == right)

    # Verify (a-b)**2 = a**2 - 2*a*b + b**2
    left = (a - b) ** 2
    right = a ** 2 - 2 * a * b + b ** 2
    print("(a-b)**2 = a**2 - 2*a*b + b**2 is", left == right)
