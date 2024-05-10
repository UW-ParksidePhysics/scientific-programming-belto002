import numpy as np


def calculate_quadratic_fit(input_data):
    """
    Fit a quadratic polynomial to a two-row NumPy array of x-y data using NumPy's polynomial class polyfit() method.

    Parameters:
        input_data (ndarray): Array of shape (2, M) where M is the number of data points.
            The first row contains the x-values and the second row contains the corresponding y-values.

    Returns:
        ndarray: Quadratic polynomial coefficients, ordered from the highest degree to the lowest degree.
            The first coefficient represents the quadratic term, the second coefficient represents the linear term,
            and the third coefficient represents the constant term.

    Raises:
        IndexError: If the input_data array has inappropriate dimensions, i.e., != 2 rows.

     __author__ = Jackson
    """
    if input_data.shape[0] != 2:
        raise IndexError("Data array has inappropriate dimensions")

    coefficients = np.polyfit(input_data[0], input_data[1], 2)
    return coefficients


if __name__ == "__main__":
    # Test the module
    data = np.array([np.linspace(-1, 1), np.linspace(-1, 1) ** 2])
    quadratic_coefficients = calculate_quadratic_fit(data)
    print(quadratic_coefficients)
