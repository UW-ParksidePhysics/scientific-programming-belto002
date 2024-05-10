"""
This module provides functions to calculate the sum of a series, estimate the error in the calculation,
and print tables of sums and errors for given x values and epsilon values.

__author__ = "Jackson"
"""


def sum_series(x_value, number_of_terms):
    """
    Calculate the sum of a series up to a given number of terms.

    Parameters:
        x_value (float): The value of x in the series.
        number_of_terms (int): The number of terms to sum in the series.

    Returns:
        float: The summation of the series.

    Example:
        sum_series(10, 3) will return the sum of the series with x_value=10 and 3 terms.
    """
    summation = 0
    for index in range(1, number_of_terms + 1):
        summation += (1.0 / index) * (x_value / (1.0 + x_value)) ** index
    return summation


def calculate_sum_and_error(x_value, number_of_terms):
    """
    Calculate the sum of a series and estimate the error in the calculation.

    Parameters:
        x_value (float): The value of x in the series.
        number_of_terms (int): The number of terms to sum in the series.

    Returns:
        tuple: A tuple containing the sum value, next term in the series, and exact error.

    Example:
        calculate_sum_and_error(10, 3) will return a tuple (sum_value, next_term, exact_error).
    """
    summation = 0
    for index in range(1, number_of_terms + 1):
        summation += (1.0 / index) * (x_value / (1.0 + x_value)) ** index
    sum_value = summation
    next_term = (1.0 / (number_of_terms + 1)) * (x_value / (1.0 + x_value)) ** (number_of_terms + 1)
    from math import log
    exact_error = log(1 + x_value) - sum_value
    return sum_value, next_term, exact_error


def print_sum_table(x_value):
    """
    Print a table of sums and errors for a given x value.

    Parameters:
        x_value (float): The value of x in the series.

    Returns:
        None.

    Example:
        print_sum_table(10) will print a table of sums and errors for x_value=10.
    """
    from math import log
    print('\nx=%g, ln(1+x)=%g' % (x_value, log(1 + x_value)))
    for number_of_terms in [1, 2, 10, 100, 500]:
        value, next_term, error = calculate_sum_and_error(x_value, number_of_terms)
        print('n=%-4d %-10g  (next term: %8.2e  '
              'error: %8.2e)' % (number_of_terms, value, next_term, error))


def calculate_sum_with_epsilon(x_value, epsilon=1.0E-6):
    """
    Calculate the sum of a series with a given epsilon value.

    Parameters:
        x_value (float): The value of x in the series.
        epsilon (float): The desired error tolerance.

    Returns:
        tuple: A tuple containing the summation value and number of terms used.

    Example:
        calculate_sum_with_epsilon(10, 1.0E-6) will return a tuple (summation, index).
    """
    x_value = float(x_value)
    index = 1
    term = (1.0 / index) * (x_value / (1 + x_value)) ** index
    summation = term
    while abs(term) > epsilon:
        index += 1
        term = (1.0 / index) * (x_value / (1 + x_value)) ** index
        summation += term
    return summation, index


def print_epsilon_table(x_value):
    """
    Print a table of epsilon values and exact errors for a given x value.

    Parameters:
        x_value (float): The value of x in the series.

    Returns:
        None.

    Example:
        print_epsilon_table(10) will print a table of epsilon values and exact errors for x_value=10.
    """
    from math import log
    for index in range(4, 14, 2):
        epsilon = 10 ** (-index)
        approximation, number_of_terms = calculate_sum_with_epsilon(x_value, epsilon=epsilon)
        exact = log(1 + x_value)
        exact_error = exact - approximation
        print('epsilon: %5.0e, exact error: %8.2e, n=%d' %
              (epsilon, exact_error, number_of_terms))


if __name__ == '__main__':
    # Test cases
    # Input: x values for calculating sums and errors
    # Output: Tables of sums and errors for different x values
    print_sum_table(10)
    print_sum_table(100)
    print_sum_table(1000)

    print('\n\n')

    # Input: x values for calculating epsilon tables
    # Output: Tables of epsilon values and exact errors for different x values
    print_epsilon_table(10)
