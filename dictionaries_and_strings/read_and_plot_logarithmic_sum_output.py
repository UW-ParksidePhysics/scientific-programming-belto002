"""This module parses the output of a logarithmic sum computation from a file and plots the tolerance and
approximation error against the maximum index.

__author__ = "Jackson"
"""


def parse_sum_output(output_path):
    """
    Parse the output of a logarithmic sum computation from a file.

    Parameters:
        output_path (str): The path to the output file.

    Returns:
        tuple: A tuple containing lists of tolerances, errors, and maximum indices.

    Example:
        parse_sum_output('logarithmic_sum.out')
    """
    epsilons = []
    err_values = []
    max_indices = []

    with open(output_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'epsilon' in line:
                parts = line.split(',')
                tolerance = float(parts[0].split(':')[1].strip())
                error = float(parts[1].split(':')[1].strip())
                index = int(parts[2].split(':')[1].strip())
                epsilons.append(tolerance)
                err_values.append(error)
                max_indices.append(index)

    return epsilons, err_values, max_indices


def plot_logarithmic_sum_error():
    """
    Plot the tolerance and approximation error against the maximum index.

    Returns:
        None.

    Example:
        plot_logarithmic_sum_error()
    """
    import matplotlib.pyplot as plt

    plt.figure()
    plt.semilogy(maximum_indices, tolerances, label='Tolerance (epsilon)')
    plt.semilogy(maximum_indices, errors, label='Approximation Error (delta)')
    plt.xlabel('Maximum Index (n)')
    plt.ylabel('Value')
    plt.title('Logarithmic Sum Error')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Test case
    # Input: Path to the output file
    # Output: Plot of tolerance and approximation error against maximum index
    file_path = 'logarithmic_sum.out'
    tolerances, errors, maximum_indices = parse_sum_output(file_path)
    plot_logarithmic_sum_error()
