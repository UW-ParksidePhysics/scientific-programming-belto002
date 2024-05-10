"""
Defines a function to calculate projectile motion trajectories and plots them based on command-line arguments.

__author__ = "Jackson"
"""

import sys
import numpy as np
import matplotlib.pyplot as plt


def calculate_y(v0, g, t_range):
    """
    Calculate the height of a projectile at various time points.

    Parameters:
        v0 (float): Initial velocity of the projectile.
        g (float): Acceleration due to gravity.
        t_range (ndarray): Array of time points.

    Returns:
        ndarray: Array of height values corresponding to the given time points.
    """
    return v0 * t_range - 0.5 * g * t_range ** 2


def main():
    """
    Main function to parse command-line arguments and plot projectile motion trajectories.
    """
    # Check if correct number of arguments is provided
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <gravity> <initial_velocity1> <initial_velocity2> ...")
        sys.exit(1)

    # Parse command-line arguments
    g = float(sys.argv[1])
    v0_values = list(map(float, sys.argv[2:]))

    # Calculate time range for each curve
    max_time = max([2 * v0 / g for v0 in v0_values])
    t_range = np.linspace(0, max_time, 100)

    # Plot each curve
    plt.figure(figsize=(8, 6))
    for v0 in v0_values:
        y_values = calculate_y(v0, g, t_range)
        plt.plot(t_range, y_values, label=f"v0 = {v0}")

    # Add labels, title, and legend
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.title("Projectile Motion Curves")
    plt.legend()
    plt.grid(True)

    # Show plot
    plt.show()


if __name__ == "__main__":
    main()
