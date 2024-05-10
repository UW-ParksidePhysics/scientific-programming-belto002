"""
This module reads Hipparcos data from a file, calculates absolute magnitudes, and creates a Hertzsprung-Russell diagram.

__author__ = "Jackson"
"""

import numpy as np
import matplotlib.pyplot as plt


def read_hipparcos_data(filename):
    """
    Read Hipparcos data from a file and store it in a dictionary.

    Parameters:
        filename (str): The name of the file containing Hipparcos data.

    Returns:
        dict: A dictionary containing the Hipparcos data.

    Example:
        read_hipparcos_data('hipparcos_data.txt')
    """
    data = {}
    with open(filename, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            hip, name, _, _, apparent_mag, bv, distance_ly, _ = line.split()
            data[int(hip)] = {'name': name, 'apparent_magnitude': float(apparent_mag), 'blue_minus_visual': float(bv),
                              'distance_ly': float(distance_ly)}
    return data


def calculate_absolute_magnitude(apparent_magnitude, distance):
    """
    Calculate the absolute magnitude.

    Parameters:
        apparent_magnitude (float or ndarray): The apparent magnitude of the star or an array of apparent magnitudes.
        distance (float or ndarray): The distance to the star in light-years or an array of distances.

    Returns:
        float or ndarray: The absolute magnitude of the star or an array of absolute magnitudes.

    Example:
        calculate_absolute_magnitude(4.2, 10)
    """
    return apparent_magnitude - 5 * np.log10(distance / 10)


def label_brightest_stars(data, ax):
    """
    Label the brightest stars on the plot.

    Parameters:
        data (dict): Dictionary containing star data.
        ax (matplotlib.axes.Axes): Axes object to plot on.

    Returns:
        None.

    Example:
        label_brightest_stars(data, plt.gca())
    """
    brightest_stars = {
        32349: 'Sirius',
        30438: 'Canopus',
        71683: 'Rigil Kent',
        69673: 'Arcturus',
        91262: 'Vega'
    }
    for hip, name in brightest_stars.items():
        star_data = data[hip]
        ax.text(star_data['blue_minus_visual'], star_data['absolute_magnitude'], name, fontsize=8, ha='left',
                va='bottom')


def make_hertzsprung_russell_diagram(data):
    """
    Create a Hertzsprung-Russell diagram.

    Parameters:
        data (dict): Dictionary containing Hipparcos data.

    Returns:
        None.

    Example:
        make_hertzsprung_russell_diagram(hipparcos_data)
    """
    apparent_magnitudes = np.array([star['apparent_magnitude'] for star in data.values()])
    blue_minus_visual = np.array([star['blue_minus_visual'] for star in data.values()])
    distances_ly = np.array([star['distance_ly'] for star in data.values()])
    absolute_magnitudes = calculate_absolute_magnitude(apparent_magnitudes, distances_ly)
    luminosities = 10 ** ((4.77 - absolute_magnitudes) / 2.5)  # Using the Sun's absolute magnitude

    plt.figure(figsize=(10, 8))
    plt.scatter(blue_minus_visual, absolute_magnitudes, s=luminosities, c=absolute_magnitudes, cmap='plasma')
    plt.gca().invert_yaxis()  # Invert y-axis to match HR diagram convention
    plt.xlabel('Blue Minus Visual Index (B-V)')
    plt.ylabel('Absolute Magnitude')
    plt.title('Hertzsprung-Russell Diagram')
    plt.text(0.1, -5, 'Created by Jackson', fontsize=8, color='gray', ha='left', va='bottom')

    # Label brightest stars
    label_brightest_stars(data, plt.gca())

    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # Test case
    # Input: File containing Hipparcos data
    # Output: Hertzsprung-Russell diagram
    hipparcos_data = read_hipparcos_data('hipparcos_data.txt')
    make_hertzsprung_russell_diagram(hipparcos_data)
    plt.show()
