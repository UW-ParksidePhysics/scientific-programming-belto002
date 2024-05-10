"""
This module calculates the position of an object in vertical motion over time and prints a table of the results.

__author__ = "Jackson"
"""


def y(t, v0, g):
    """
    Calculate the position of an object in vertical motion at time t.

    Parameters:
        t (float): Time elapsed since the start of motion (in seconds).
        v0 (float): Initial velocity of the object (in meters per second).
        g (float): Acceleration due to gravity (in meters per second squared).

    Returns:
        float: The position of the object at time t (in meters).
    """
    return v0 * t - 0.5 * g * t ** 2


def print_table(n, v0, g):
    """
    Print a table of object positions over time using both for and while loops.

    Parameters:
        n (int): Number of intervals for time calculation.
        v0 (float): Initial velocity of the object (in meters per second).
        g (float): Acceleration due to gravity (in meters per second squared).

    Returns:
        None
    """
    interval = 2 * v0 / g
    step = interval / n

    # print a table header
    print("t\t|\ty(t)")
    print("------------------")

    # for loop
    print("Using a for loop:")
    for i in range(n + 1):
        t = i * step
        print(f"{t:.2f}\t|\t{y(t, v0, g):.2f}")

    print("\n")

    # while loop
    print("Using a while loop:")
    t = 0
    while t <= interval:
        print(f"{t:.2f}\t|\t{y(t, v0, g):.2f}")
        t += step


if __name__ == "__main__":
    # Test case
    # Input: Number of intervals (n), initial velocity (v0), acceleration due to gravity (g)
    # Output: Table of object positions over time
    print_table(10, 20, 9.8)
