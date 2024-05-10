import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import physical_constants
from datetime import datetime
import read_two_columns_text
import calculate_bivariate_statistics
import calculate_quadratic_fit
import fit_curve_array
import plot_data_with_fit
import calculate_lowest_eigenvectors
import annotate_plot

# Test read_two_columns_text module
filename = "volumes_energies.dat"
data = read_two_columns_text.read_two_columns_text(filename)
print(f'{data=}, shape={data.shape}')

# Test calculate_bivariate_statistics module
statistics = calculate_bivariate_statistics.calculate_bivariate_statistics(data)
print(f'{statistics=}')

# Test calculate_quadratic_fit module
quadratic_coefficients = calculate_quadratic_fit.calculate_quadratic_fit(data)
print(f'{quadratic_coefficients=}')

# Test fit_curve_array module
fit_curve = fit_curve_array.fit_curve_array(quadratic_coefficients, -2, 2)
print(f'{fit_curve=}')

# Test plot_data_with_fit module
plt.figure()
data = [[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]]
fit_curve = [np.linspace(-2, 2), np.linspace(-2, 2)**2]
plot_data_with_fit.plot_data_with_fit(data, fit_curve, data_format='x', fit_format='--')
plt.show()

# Test calculate_lowest_eigenvectors module
square_matrix = np.array([[2, -1], [-1, 2]])
eigenvalues, eigenvectors = calculate_lowest_eigenvectors.calculate_lowest_eigenvectors(square_matrix)
print(f'{eigenvalues=}')
print(f'{eigenvectors=}')

# Test annotate_plot module
annotations = {'Text': {'position': np.array([0.1, 0.1]), 'alignment': ['left', 'bottom'], 'fontsize': 12}}
annotate_plot.annotate_plot(annotations)

plt.show()