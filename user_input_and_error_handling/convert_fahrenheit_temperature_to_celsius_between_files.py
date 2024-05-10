"""
This module converts Fahrenheit temperatures to Celsius and writes the results to a file.

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
    # Read Fahrenheit temperatures from file
    fahrenheit_degrees = []
    with open('temperature_data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines[3:]:
            fahrenheit_degrees.append(float(line.split()[2]))

    # Convert Fahrenheit to Celsius
    celsius_degrees = [fahrenheit_to_celsius(f) for f in fahrenheit_degrees]

    # Write Fahrenheit and Celsius temperatures to a new file
    with open('converted_temperatures.txt', 'w') as outfile:
        outfile.write("Fahrenheit degrees\tCelsius degrees\n")
        for fahrenheit, celsius in zip(fahrenheit_degrees, celsius_degrees):
            outfile.write(f"{fahrenheit:.2f}\t\t\t{celsius:.2f}\n")
