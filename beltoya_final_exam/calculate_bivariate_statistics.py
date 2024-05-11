import numpy as np


def calculate_bivariate_statistics(input_data):
    """
    Calculate statistical characteristics of a 2D data set.

    Parameters:
        input_data (ndarray): 2D array containing x-y data to be characterized.
            It should have the shape (2, M), where M is the number of data points.

    Returns:
        ndarray: An array containing the mean of y, standard deviation of y, minimum x-value,
            maximum x-value, minimum y-value, and maximum y-value, respectively.

    Raises:
        IndexError: If the input_data array has inappropriate dimensions (!=2 rows, or <=1 column).

             __author__ = Jackson
    """
    if input_data.shape[0] != 2 or input_data.shape[1] <= 1:
        raise IndexError("Data array has inappropriate dimensions")

    mean_y = np.mean(input_data[1])
    std_y = np.std(input_data[1])
    min_x = np.min(input_data[0])
    max_x = np.max(input_data[0])
    min_y = np.min(input_data[1])
    max_y = np.max(input_data[1])

    return np.array([mean_y, std_y, min_x, max_x, min_y, max_y])


if __name__ == "__main__":
    # Test the module
    x = np.linspace(-10, 10, 100)
    y = x ** 2
    data = np.vstack((x, y))

    statistics = calculate_bivariate_statistics(data)
    print(statistics)
