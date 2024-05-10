"""
Demo of convert_temperature module:

>>> celsius_to_fahrenheit(0)
32.0
>>> fahrenheit_to_celsius(32)
0.0
>>> celsius_to_kelvin(0)
273.15
>>> kelvin_to_celsius(273.15)
0.0
>>> fahrenheit_to_kelvin(32)
273.15
>>> kelvin_to_fahrenheit(273.15)
32.0

"""

__author__ = "Jackson"


def celsius_to_fahrenheit(celsius_temperature):
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
        celsius_temperature (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius_temperature * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit_temperature):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit_temperature (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit_temperature - 32) * 5 / 9


def celsius_to_kelvin(celsius_temperature):
    """
    Convert temperature from Celsius to Kelvin.

    Parameters:
        celsius_temperature (float): Temperature in Celsius.

    Returns:
        float: Temperature in Kelvin.
    """
    return celsius_temperature + 273.15


def kelvin_to_celsius(kelvin_temperature):
    """
    Convert temperature from Kelvin to Celsius.

    Parameters:
        kelvin_temperature (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Celsius.
    """
    return kelvin_temperature - 273.15


def fahrenheit_to_kelvin(fahrenheit_temperature):
    """
    Convert temperature from Fahrenheit to Kelvin.

    Parameters:
        fahrenheit_temperature (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Kelvin.
    """
    return (fahrenheit_temperature - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(kelvin_temperature):
    """
    Convert temperature from Kelvin to Fahrenheit.

    Parameters:
        kelvin_temperature (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (kelvin_temperature - 273.15) * 9 / 5 + 32


def test_conversion():
    """
    Test conversion functions.
    """
    tests = [
        (0, celsius_to_fahrenheit, fahrenheit_to_celsius),
        (0, celsius_to_kelvin, kelvin_to_celsius),
        (32, fahrenheit_to_kelvin, kelvin_to_fahrenheit)
    ]

    for value, conv_func1, conv_func2 in tests:
        result1 = conv_func1(value)
        result2 = conv_func2(result1)
        assert abs(result2 - value) < 0.001


def user_interface(temp, temp_scale):
    """
    Convert temperature between scales.

    Parameters:
        temp (str): Temperature value.
        temp_scale (str): Temperature scale ('C' for Celsius, 'F' for Fahrenheit, 'K' for Kelvin).

    Returns:
        str: Converted temperature in Fahrenheit, Celsius, and Kelvin.
    """
    temp = float(temp)  # Convert string to float
    temp_scale = temp_scale.lower()
    if temp_scale == 'c':
        celsius = temp
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif temp_scale == 'f':
        fahrenheit = temp
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif temp_scale == 'k':
        kelvin = temp
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        raise ValueError("Invalid temperature scale. Use 'C', 'F', or 'K'.")
    return f"{fahrenheit:.2f} F  {celsius:.2f} C  {kelvin:.2f} K"


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import sys

    if len(sys.argv) != 3:
        print("Usage: python convert_temperature.py <temperature> <scale>")
        sys.exit(1)

    temperature, temperature_scale = sys.argv[1], sys.argv[2]
    print(user_interface(temperature, temperature_scale))
