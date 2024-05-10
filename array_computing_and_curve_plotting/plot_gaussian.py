"""
Defines a Gaussian function and provides a test function to evaluate it at sample positions.

__author__ = "Jackson"
"""

import numpy as np
import matplotlib.pyplot as plt


def gaussian(position):
    """
    Compute the value of the Gaussian function at a given position.

    Parameters:
        position (float or ndarray): The position(s) at which to evaluate the Gaussian function.

    Returns:
        float or ndarray: The value(s) of the Gaussian function at the specified position(s).
    """
    return 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * position ** 2)


def test_gaussian():
    """
    Test function to evaluate the Gaussian function at sample positions and print the results.
    """
    # Test with some sample positions
    test_positions = [-4, -2, 0, 2, 4]
    for pos in test_positions:
        print(f"g({pos}) = {gaussian(pos)}")


if __name__ == '__main__':
    # Fill the lists positions and gaussian_values with x and g(x) values
    positions = np.linspace(-4, 4, 41)
    gaussian_values = [gaussian(x) for x in positions]

    # Plot the Gaussian function
    plt.plot(positions, gaussian_values)
    plt.title('Gaussian Function')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.grid(True)
    plt.show()

    # Test the function
    print("\nTesting the function:")
    test_gaussian()
