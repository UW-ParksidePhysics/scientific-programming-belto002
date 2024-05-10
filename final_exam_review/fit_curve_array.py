import numpy as np


def fit_curve_array(coefficients, min_x, max_x, number_of_points=100):
    """
    Generate a fit curve using the provided quadratic polynomial coefficients.

    Parameters: coefficients (array_like): Quadratic polynomial coefficients, ordered from the highest degree to the
    lowest degree. The first coefficient represents the quadratic term, the second coefficient represents the linear
    term, and the third coefficient represents the constant term. min_x (float): Starting value for the x-values of
    the fit curve array. max_x (float): Ending value for the x-values of the fit curve array. number_of_points (int,
    optional): Number of points to generate for the fit curve. Default is 100.

    Returns:
        ndarray: An array of shape (2, N) containing the x-y data created by the coefficients of the fit function.
            The first row contains the x-values, and the second row contains the corresponding y-values.

    Raises:
        ArithmeticError: If max_x is less than min_x.
        IndexError: If number_of_points is less than or equal to 2.

             __author__ = Jackson
    """
    if max_x < min_x:
        raise ArithmeticError("maximum_x should be greater than minimum_x")
    if number_of_points <= 2:
        raise IndexError("number_of_points should be greater than 2")

    x_fit = np.linspace(min_x, max_x, number_of_points)
    y_fit = np.polyval(coefficients, x_fit)

    return np.array([x_fit, y_fit])


if __name__ == "__main__":
    # Test the module
    quadratic_coefficients = [0, 0, 1]
    minimum_x = -2
    maximum_x = 2
    fit_curve = fit_curve_array(quadratic_coefficients, minimum_x, maximum_x)
    print(fit_curve)
