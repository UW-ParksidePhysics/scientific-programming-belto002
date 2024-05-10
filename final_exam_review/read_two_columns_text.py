import numpy as np


def read_two_columns_text(input_filename):
    """
    Read data from a text file containing two columns.

    This function reads data from a text file containing two columns and returns it as a NumPy array.

    Parameters:
        input_filename (str): The name of the text file to be read.

    Returns:
        ndarray: A NumPy array containing the data read from the text file.
            The array has the shape (2, M), where M is the number of data points.
            The first row contains the x-values, and the second row contains the corresponding y-values.

    Raises:
        OSError: If the file specified by input_filename cannot be found or accessed.

    Example:
        test_filename = "volumes_energies.dat"
        loaded_data = read_two_columns_text(test_filename)
        print(f'{loaded_data=}, shape={loaded_data.shape}')

             __author__ = Jackson
    """
    try:
        file_data = np.loadtxt(input_filename).T
        return file_data
    except OSError as e:
        raise e


if __name__ == "__main__":
    # Test the module
    test_filename = "volumes_energies.dat"
    loaded_data = read_two_columns_text(test_filename)
    print(f'{loaded_data=}, shape={loaded_data.shape}')
