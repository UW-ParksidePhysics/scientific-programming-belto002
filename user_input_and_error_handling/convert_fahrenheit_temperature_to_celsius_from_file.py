"""
This module converts Fahrenheit temperatures to Celsius based on a temperature read from a file.

__author__ = "Jackson"
"""


def fahrenheit_to_celsius(fahrenheit_degree):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit_degree (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    celsius_temp = (fahrenheit_degree - 32) * 5 / 9
    return celsius_temp


if __name__ == '__main__':
    # Read Fahrenheit temperature from file
    with open('temperature_data.txt', 'r') as file:
        lines = file.readlines()
        fahrenheit_temp = float(lines[3].split()[2])

    # Convert Fahrenheit to Celsius
    celsius_output = fahrenheit_to_celsius(fahrenheit_temp)

    # Print the result
    print(f"{fahrenheit_temp}°F is equal to {celsius_output:.2f}°C.")
