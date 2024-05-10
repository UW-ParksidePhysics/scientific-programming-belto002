"""
Defines a Gaussian function and computes its values over a range of positions.

__author__ = "Jackson"
"""

import numpy as np


def gaussian(position):
    """
    Compute the value of the Gaussian function at a given position.

    Parameters:
        position (float): The position at which to evaluate the Gaussian function.

    Returns:
        float: The value of the Gaussian function at the specified position.
    """
    return 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * position ** 2)


if __name__ == '__main__':
    # Create empty arrays
    x_values = []
    y_values = []

    # Compute values using a for loop
    positions = np.linspace(-4, 4, 41)
    for pos in positions:
        x_values.append(pos)
        y_values.append(gaussian(pos))

    # Print the arrays
    print("x_values:", x_values)
    print("y_values:", y_values)
