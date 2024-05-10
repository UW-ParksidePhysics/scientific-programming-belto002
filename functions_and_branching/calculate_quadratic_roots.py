"""
This module contains functions to calculate the roots of a quadratic equation and test cases for the functions.

__author__ = "Jackson"
"""

import numpy as np


def calculate_quadratic_roots(a, b, c):
    """
    Calculate the roots of a quadratic equation.

    Parameters:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple: A tuple containing the roots of the quadratic equation.

    Example:
        calculate_quadratic_roots(1, -2, -3)
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        # Real Part
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        # Complex Part
        real_part = -b / (2 * a)
        imaginary_part = np.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


def test_single_root():
    """
    Test for single real root.

    Returns:
        None.
    """
    a, b, c = 1, 2, 1
    computed_roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 + 2x + 1 = 0: x = -1.0 ; calculate_quadratic_roots(1, 2, 1) = {computed_roots}")


def test_roots_float():
    """
    Test for two real roots.

    Returns:
        None.
    """
    a, b, c = 1, -2, -3
    computed_roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 - 2x - 3 = 0: x = 3.0, -1.0 ; calculate_quadratic_roots(1, -2, -3) = {computed_roots}")


def test_roots_complex():
    """
    Test for complex roots.

    Returns:
        None.
    """
    a, b, c = 2, 2, -1
    computed_roots = calculate_quadratic_roots(a, b, c)
    print(f"x^2 + 0x + 1 = 0: x = 1j, -1j ; calculate_quadratic_roots(2, 2, -1) = {computed_roots}")


if __name__ == "__main__":
    test_single_root()
    test_roots_float()
    test_roots_complex()
