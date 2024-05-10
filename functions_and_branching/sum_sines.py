"""
This module contains functions for computing piecewise constant functions and sinusoidal sums.

__author__ = "Jackson"
"""

import numpy as np


def piecewise_function(t, period):
    """Compute the piecewise constant function f(t).

    Parameters:
        t (float): The time parameter.
        period (float): The period of the function.

    Returns:
        int: The value of the piecewise constant function at time t.
    """
    t_half = period / 2
    if 0 <= t < t_half:
        return 1
    elif t == t_half:
        return 0
    else:
        return -1


def sinusoidal_sum(t, number_of_functions, period):
    """Compute the value of the sinusoidal sum S(t;n).

    Parameters:
        t (float): The time parameter.
        number_of_functions (int): The number of sinusoidal functions to sum.
        period (float): The period of the sinusoidal functions.

    Returns:
        float: The value of the sinusoidal sum at time t.
    """
    result = 0
    for i in range(1, number_of_functions + 1):
        result += (1 / (2 * i - 1)) * np.sin((2 * (2 * i - 1) * np.pi * t) / period)
    return 4 / np.pi * result


def compute_error(t, number_of_functions, period):
    """Compute the error f(t) - S(t;n) for a given time and number of functions.

    Parameters:
        t (float): The time parameter.
        number_of_functions (int): The number of sinusoidal functions to sum.
        period (float): The period of the sinusoidal functions.

    Returns:
        float: The error between the piecewise function and the sinusoidal sum at time t.
    """
    return piecewise_function(t, period) - sinusoidal_sum(t, number_of_functions, period)


def print_error_table(period_value, alpha_values, number_of_functions):
    """Print table showing error with n and t.

    Parameters:
        period_value (float): The period value.
        alpha_values (list): List of alpha values.
        number_of_functions (list): List of number of functions.
    """
    print("Error Table:")
    print("n\talpha\tT/2\tError")
    for n in number_of_functions:
        for alpha in alpha_values:
            t = alpha * period_value
            t_half = period_value / 2
            error = compute_error(t, n, period_value)
            print(f"{n}\t{alpha}\t{t_half}\t{error:.6f}")


if __name__ == "__main__":
    p = 2 * np.pi  # T = 2pi
    alphas = [0.01, 0.25, 0.49]
    num_functions = [1, 3, 5, 10, 30, 100]
    print_error_table(p, alphas, num_functions)
