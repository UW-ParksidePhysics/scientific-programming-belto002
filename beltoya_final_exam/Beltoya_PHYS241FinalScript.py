import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import physical_constants, Bohr
from datetime import datetime

from beltoya_final_exam.annotate_plot import annotate_plot

# Constants
bohr_to_angstrom = float(Bohr) * 1e10  # Convert Bohr constant to float
rydberg_to_ev = physical_constants['Rydberg constant times hc in eV'][0]
rydberg_per_cubic_bohr_to_gpa = physical_constants['Rydberg constant times hc in eV'][0] / bohr_to_angstrom ** 3 / 1e9


# Function to parse file name
def parse_file_name(file):
    parts = file.split('.')
    return parts[0], parts[1], parts[2]


# Function to read data from file
def read_two_columns_text(file):
    data = np.loadtxt(file)
    return data[:, 0], data[:, 1]


# Function to calculate bivariate statistics
def calculate_bivariate_statistics(data):
    return np.mean(data), np.std(data)


# Function to calculate quadratic fit
def calculate_quadratic_fit(x, y):
    return np.polyfit(x, y, 2)


# Function to convert units
def convert_units(value, from_unit, to_unit):
    if from_unit == 'bohr_per_atom' and to_unit == 'angstroms_per_atom':
        return value * bohr_to_angstrom
    elif from_unit == 'rydberg_per_atom' and to_unit == 'electron_volts_per_atom':
        return value * rydberg_to_ev
    elif from_unit == 'rydberg_per_cubic_bohr' and to_unit == 'gigapascals':
        return value * rydberg_per_cubic_bohr_to_gpa


# Function to plot data and fit curve
def plot_data_and_fit(x, y, fit_coeffs, chemical_symbol, symmetry_symbol, bulk_modulus, display_graph):
    # Plot data
    plt.plot(x, y, 'bo', label='Data')

    # Plot fit curve
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = np.polyval(fit_coeffs, x_fit)
    plt.plot(x_fit, y_fit, 'k-', label='Fit Curve')

    # Annotate graph
    plt.text(min(x), max(y), chemical_symbol, fontsize=12, va='top')
    plt.text(np.mean(x), np.mean(y), f'{symmetry_symbol}', fontsize=12, ha='center', va='bottom')
    plt.text(np.mean(x), np.mean(y), f'K0 = {bulk_modulus:.1f} GPa', fontsize=10, ha='center', va='bottom')
    plt.axvline(x_fit[np.argmin(y_fit)], color='black', linestyle='--')
    plt.text(x_fit[np.argmin(y_fit)], 0, f'V0 = {x_fit[np.argmin(y_fit)]:.2f} Å³/atom', fontsize=8, ha='center')
    plt.text(min(x), min(y), f"Created by Jackson Beltoya {datetime.now().isoformat()}", fontsize=8, va='bottom')
    plt.title(f'(Birch-Murnaghan) Equation of State for {chemical_symbol} in DFT (GGA-PBE)')
    plt.xlabel('V (Å³/atom)')
    plt.ylabel('E (eV/atom)')
    plt.legend()

    # Show or save plot based on display_graph flag
    plt.grid(True)
    if display_graph:
        plt.show()
    else:
        plt.savefig("Beltoya.Sn.Fd-3m.GGA-PBE.Birch-MurnaghanEquationOfState.png")


if __name__ == '__main__':
    # Parameters
    file_name = "Sn.Fd-3m.GGA-PBE.volumes_energies.dat"
    display_graph = False  # Set to True to display graph, False to save as PNG

    # Parse file name
    chemical_symbol, symmetry_symbol, _ = parse_file_name(file_name)

    # Read data
    volumes, energies = read_two_columns_text(file_name)

    # Calculate fit
    fit_coeffs = calculate_quadratic_fit(volumes, energies)

    # Convert units
    volumes_angstrom_per_atom = convert_units(np.ones_like(volumes), 'bohr_per_atom', 'angstroms_per_atom')
    energies_ev_per_atom = convert_units(np.ones_like(energies), 'rydberg_per_atom', 'electron_volts_per_atom')
    bulk_modulus_gpa = convert_units(fit_coeffs[0], 'rydberg_per_cubic_bohr', 'gigapascals')

    # Plot data and fit curve
    plot_data_and_fit(volumes, energies, fit_coeffs, chemical_symbol, symmetry_symbol, bulk_modulus_gpa, display_graph)


# Function to generate the matrix
def generate_matrix(Ndim, potential_strength):
    matrix = np.diag(-2 * np.ones(Ndim)) + np.diag(np.ones(Ndim - 1), 1) + np.diag(np.ones(Ndim - 1), -1)
    return matrix + potential_strength * np.diag(np.linspace(-10, 10, Ndim) ** 2)


# Function to calculate lowest eigenvectors
def calculate_lowest_eigenvectors(matrix_, num_eigenvectors_):
    eigenvalues_, eigenvectors_ = np.linalg.eigh(matrix_)
    lowest_eigenvectors_ = eigenvectors_[:, :num_eigenvectors_]
    return lowest_eigenvectors_, eigenvalues_[:num_eigenvectors_]


# Function to plot eigenvectors
def plot_eigenvectors(grid_points_, eigenvectors_, eigenvalues_, potential_name_, display_graph_):
    plt.figure(figsize=(8, 6))
    for i, (eigenvalue_, eigenvector_) in enumerate(zip(eigenvalues_, eigenvectors_.T)):
        if eigenvector_[0] < 0:
            eigenvector_ *= -1
        plt.plot(grid_points_, eigenvector_, label=f'ψ{i + 1}, E{i + 1} = {eigenvalue_:.3f} a.u.')

    plt.axhline(0, color='black', linestyle='-', linewidth=0.5)
    plt.xlabel('x [a.u.]')
    plt.ylabel('ψ(x)')
    plt.xlim(-10, 10)
    plt.ylim(-2 * np.max(np.abs(eigenvectors_)),
             2 * np.max(np.abs(eigenvectors_)))  # Removed extra closing parenthesis here
    plt.legend()
    plt.title(f"Select Wavefunctions for a {potential_name_} Potential on a Spatial Grid of {len(grid_points_)} Points")
    annotate_plot()

    if display_graph_:
        plt.show()
    else:
        plt.savefig(f"Beltoya.{potential_name_}.Eigenvectors.png")


if __name__ == '__main__':
    # Parameters
    Ndim_ = 100
    potential_strength_ = 0.1
    display_graph_ = False  # Set to True to display graph, False to save as PNG
    potential_name_ = "Harmonic"  # Name of the potential

    # Generate the matrix
    matrix_ = generate_matrix(Ndim_, potential_strength_)

    # Calculate lowest eigenvectors
    eigenvectors_, eigenvalues_ = calculate_lowest_eigenvectors(matrix_, 3)

    # Generate grid of spatial points
    grid_points_ = np.linspace(-10, 10, Ndim_)

    # Plot eigenvectors
    plot_eigenvectors(grid_points_, eigenvectors_, eigenvalues_, potential_name_, display_graph_)
