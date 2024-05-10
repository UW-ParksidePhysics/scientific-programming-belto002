"""
Defines a Gaussian function and computes its values over a range of positions.

__author__ = "Jackson"
"""

import numpy as np


def gaussian(position):
    """
    Compute the value of the Gaussian function at a given position.

    Parameters:
        position (float or ndarray): The position(s) at which to evaluate the Gaussian function.

    Returns:
        float or ndarray: The value(s) of the Gaussian function at the specified position(s).
    """
    return 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * position ** 2)


if __name__ == '__main__':
    # Create x values using linspace
    x_values = np.linspace(-4, 4, 41)

    # Evaluate g(x) for the array argument
    y_values = gaussian(x_values)

    # Print the arrays
    print("x_values:", x_values)
    print("y_values:", y_values)
