import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_fmt='o', fit_fmt='', **kwargs):
    """
    Plot the given data along with the fitted curve.

    Parameters:
        data (ndarray): Array containing the x-y data points to be plotted.
            It should have the shape (2, M), where the first row contains the x-values and
            the second row contains the corresponding y-values.
        fit_curve (ndarray): Array containing the x-y data points of the fitted curve.
            It should have the shape (2, N), where the first row contains the x-values and
            the second row contains the corresponding y-values.
        data_fmt (str, optional): Formatting specification for the style of the scatter plot data points.
            Default is 'o' (circle). See matplotlib.pyplot.plot for specifications.
        fit_fmt (str, optional): Formatting specification for the curve of the fit function.
            Default is '' (empty string). See matplotlib.pyplot.plot for specifications.
        **kwargs: Additional keyword arguments to be passed to matplotlib.pyplot.plot.

    Returns:
        list: A list of Line2D objects representing the plotted data.

    Example:
        import numpy as np
        test_data = np.array([[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
        test_fit_curve = np.array([np.linspace(-2, 2), np.linspace(-2, 2) ** 2])
        combined_plot = plot_data_with_fit(test_data, test_fit_curve, data_fmt='x', fit_fmt='--')
        plt.legend()
        plt.show()

             __author__ = Jackson
    """
    scatter_plot = plt.plot(data[0], data[1], data_fmt, label='Data', **kwargs)
    fit_plot = plt.plot(fit_curve[0], fit_curve[1], fit_fmt, label='Fit', **kwargs)

    return scatter_plot + fit_plot


if __name__ == "__main__":
    # Test the module
    import numpy as np

    test_data = np.array([[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
    test_fit_curve = np.array([np.linspace(-2, 2), np.linspace(-2, 2) ** 2])

    combined_plot = plot_data_with_fit(test_data, test_fit_curve, data_fmt='x', fit_fmt='--')
    plt.legend()
    plt.show()
