"""
This module converts temperature from Fahrenheit to Celsius.

__author__ = "Jackson"
"""


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
    # Test the function with user input
    fahrenheit_input = float(input("Enter the temperature in Fahrenheit: "))
    celsius_output = fahrenheit_to_celsius(fahrenheit_input)
    print(f"{fahrenheit_input}°F is equal to {celsius_output:.2f}°C.")
