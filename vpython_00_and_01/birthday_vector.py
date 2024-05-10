"""
Visualization of a 3D vector.

__author__ = "Jackson"
"""

import matplotlib.pyplot as plt
import numpy as np


def visualize_3d_vector(a, b, c):
    """
    Visualize a 3D vector with given components.

    Parameters:
        a (float): x-component of the vector.
        b (float): y-component of the vector.
        c (float): z-component of the vector.

    Returns:
        None
    """
    # Define the figure and the 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the vector
    r = np.array([a, b, c])

    # Draw the vector
    ax.quiver(0, 0, 0, *r, color='navy')  # Using navy color for the vector

    # Label the axes
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Set lower case axis labels
    ax.xaxis.label.set_size(10)
    ax.yaxis.label.set_size(10)
    ax.zaxis.label.set_size(10)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    # Test case
    # Input: x-component: 6, y-component: 24, z-component: 2
    # Output: 3D vector visualization
    visualize_3d_vector(6, 24, 2)
