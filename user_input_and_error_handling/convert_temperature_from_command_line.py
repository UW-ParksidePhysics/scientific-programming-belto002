"""
Convert Fahrenheit temperature to Celsius.

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
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python script_name.py <temperature_in_fahrenheit>")

        fahrenheit_input = float(sys.argv[1])

        celsius_output = fahrenheit_to_celsius(fahrenheit_input)

        print(f"{fahrenheit_input}°F is equal to {celsius_output:.2f}°C.")

    except ValueError as ve:
        print(ve)
        sys.exit(1)
