"""
This module converts Fahrenheit temperatures to Celsius based on user input from the command line.

__author__ = "Jackson"
"""

import sys


def fahrenheit_to_celsius(fahrenheit_temp):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit_temp (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    celsius_temp = (fahrenheit_temp - 32) * 5 / 9
    return celsius_temp


if __name__ == '__main__':
    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <temperature_in_fahrenheit>")
        sys.exit(1)

    # Read Fahrenheit temperature from Command Line.
    fahrenheit_input = float(sys.argv[1])

    # Convert Fahrenheit to Celsius
    celsius_output = fahrenheit_to_celsius(fahrenheit_input)

    # Print the results
    print(f"{fahrenheit_input}°F is equal to {celsius_output:.2f}°C.")
