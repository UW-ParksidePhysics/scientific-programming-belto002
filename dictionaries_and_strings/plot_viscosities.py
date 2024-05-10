"""This module parses viscosity data of gases from a file, calculates viscosity at different temperatures for
different gases, and plots the viscosity vs temperature for different gases.

__author__ = "Jackson"
"""

import matplotlib.pyplot as plt


def parse_viscosity_data(filename):
    """
    Parse viscosity data from a file and store it in a dictionary.

    Parameters:
        filename (str): The name of the file containing viscosity data.

    Returns:
        dict: A dictionary containing the viscosity data.

    Example:
        parse_viscosity_data('viscosity_of_gases.dat')
    """
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            name, c, t0, mu0 = line.split()
            data[name] = {'viscosity': float(c), 'reference_temperature': float(t0), 'reference_viscosity': float(mu0)}
    return data


def calculate_viscosity(temperature, gas, data):
    """
    Calculate the viscosity of a gas at a given temperature.

    Parameters:
        temperature (float): The temperature at which to calculate viscosity (in Kelvin).
        gas (str): The name of the gas.
        data (dict): A dictionary containing the viscosity data.

    Returns:
        float: The viscosity of the gas at the given temperature.

    Example:
        calculate_viscosity(300, 'air', viscosity_data)
    """
    c = data[gas]['viscosity']
    t0 = data[gas]['reference_temperature']
    mu0 = data[gas]['reference_viscosity']
    return mu0 * (t0 - c) / ((temperature + c) * (t0 / temperature) ** 1.5)


def plot_viscosity(temps, gases_list, data):
    """
    Plot viscosity vs temperature for different gases.

    Parameters:
        temps (list): A list of temperatures (in Kelvin).
        gases_list (list): A list of gas names.
        data (dict): A dictionary containing the viscosity data.

    Returns:
        None.

    Example:
        plot_viscosity([300, 310], ['air', 'carbon_dioxide'], viscosity_data)
    """
    for gas_name in gases_list:
        viscosities = [calculate_viscosity(temp, gas_name, data) for temp in temps]
        plt.plot(temps, viscosities, label=gas_name)

    plt.xlabel('Temperature (K)')
    plt.ylabel('Viscosity')
    plt.title('Viscosity vs Temperature for Different Gases')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # Test case
    # Input: File containing viscosity data
    # Output: Viscosity vs temperature plot for different gases
    viscosity_data = parse_viscosity_data('viscosity_of_gases.dat')
    temperatures = list(range(223, 324))
    gases = ['air', 'carbon_dioxide', 'hydrogen']
    plot_viscosity(temperatures, gases, viscosity_data)
