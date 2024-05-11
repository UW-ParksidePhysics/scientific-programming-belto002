import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import physical_constants, Bohr
from datetime import datetime
from equations_of_state import fit_eos  # Importing fit_eos function from equations_of_state module

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
    else:
        raise ValueError("Invalid conversion units")


# Function to plot data and fit curve
def plot_data_and_fit(x, y, fit_coeffs_, chem_symbol, sym_symbol, bulk_modulus, disp_graph):
    plt.plot(x, y, 'bo', label='Data')
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = np.polyval(fit_coeffs_, x_fit)
    plt.plot(x_fit, y_fit, 'k-', label='Fit Curve')
    plt.text(np.mean(x), np.mean(y), f'K0 = {bulk_modulus:.1f} GPa', fontsize=10, ha='center', va='bottom')
    plt.axvline(min(x_fit), color='black', linestyle='--')
    plt.text(min(x_fit), 0, f'V0 = {min(x_fit):.2f} Å³/atom', fontsize=8, ha='center')
    plt.text(min(x), min(y), f"Created by Jackson Beltoya {datetime.now().isoformat()}", fontsize=8, va='bottom')
    plt.title(f'(Birch-Murnaghan) Equation of State for {chem_symbol} in DFT (GGA-PBE)')
    plt.xlabel('V (Å³/atom)')
    plt.ylabel('E (eV/atom)')
    plt.legend()
    plt.grid(True)
    if disp_graph:
        plt.show()
    else:
        plt.savefig(f"Beltoya.{chem_symbol}.{sym_symbol}.GGA-PBE.Birch-MurnaghanEquationOfState.png")


# Function to generate the matrix
def generate_matrix(Ndim_, potential_coeff):
    matrix_ = np.diag(-2 * np.ones(Ndim_)) + np.diag(np.ones(Ndim_ - 1), 1) + np.diag(np.ones(Ndim_ - 1), -1)
    return matrix_ + potential_coeff * np.diag(np.linspace(-10, 10, Ndim_) ** 2)


# Function to calculate the lowest eigenvectors
def calculate_lowest_eigenvectors(matrix_, num_eigenvectors_):
    eigvals, eigvecs = np.linalg.eigh(matrix_)
    lowest_eigenvectors_ = eigvecs[:, :num_eigenvectors_]
    return lowest_eigenvectors_, eigvals[:num_eigenvectors_]


# Function to plot eigenvectors
def plot_eigenvectors(spacial_grid_points, eigvecs, eigvals, potential_name, show_plt):
    plt.figure(figsize=(8, 6))
    for i, (eigenvalue_, eigenvector_) in enumerate(zip(eigvals, eigvecs.T)):
        if eigenvector_[0] < 0:
            eigenvector_ *= -1
        plt.plot(spacial_grid_points, eigenvector_, label=f'ψ{i + 1}, E{i + 1} = {eigenvalue_:.3f} a.u.')
    plt.axhline(0, color='black', linestyle='-', linewidth=0.5)
    plt.xlabel('x [a.u.]')
    plt.ylabel('ψ(x)')
    plt.xlim(-10, 10)
    plt.ylim(-2 * np.max(np.abs(eigvecs)), 2 * np.max(np.abs(eigvecs)))
    plt.legend()
    plt.title(f"Select Wavefunctions for a {potential_name} Potential on a Grid of {len(spacial_grid_points)} Points")
    if show_plt:
        plt.show()
    else:
        for i, _ in enumerate(eigvecs.T, start=1):
            plt.savefig(f"Beltoya.{potential_name}.Eigenvector{i}.png")


if __name__ == '__main__':
    # Parameters
    file_name = "Sn.Fd-3m.GGA-PBE.volumes_energies.dat"
    display_graph = False

    # Parse file name
    chemical_symbol, symmetry_symbol, _ = parse_file_name(file_name)

    # Read data
    volumes, energies = read_two_columns_text(file_name)

    # Calculate bivariate statistics
    mean_volume, std_volume = calculate_bivariate_statistics(volumes)
    mean_energy, std_energy = calculate_bivariate_statistics(energies)

    # Fit a quadratic polynomial
    fit_coeffs = calculate_quadratic_fit(volumes, energies)

    # Pass the fit quadratic coefficients and the data to the fit_eos function (hypothetical)
    fit_eos(fit_coeffs, volumes, energies, chemical_symbol, symmetry_symbol)

    # Generate matrix
    Ndim = 100
    potential_strength = 0.1
    matrix = generate_matrix(Ndim, potential_strength)

    # Calculate lowest eigenvectors
    num_eigenvectors = 3
    eigenvectors, eigenvalues = calculate_lowest_eigenvectors(matrix, num_eigenvectors)

    # Plot eigenvectors
    grid_points = np.linspace(-10, 10, Ndim)
    plot_eigenvectors(grid_points, eigenvectors, eigenvalues, "Potential Name", display_graph)
