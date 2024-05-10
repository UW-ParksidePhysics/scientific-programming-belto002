"""
This module contains functions to convert temperatures between Celsius and Fahrenheit.

__author__ = "Jackson"
"""


def convert_celsius_to_fahrenheit(celsius_temperature):
    """Convert temperature from Celsius to Fahrenheit."""
    return (9. / 5.) * celsius_temperature + 32


def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    """Convert temperature from Fahrenheit to Celsius."""
    return (5. / 9.) * (fahrenheit_temperature - 32)


def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
    """Convert temperature from Fahrenheit to Celsius."""
    return (5. / 9.) * (fahrenheit_temperature - 32)


def verify_temperature_conversions():
    """Verify temperature conversions."""
    celsius_temperatures = [0, 21, 100]

    print('T_C\tT_C(T_F(T_C))')

    for celsius_temperature in celsius_temperatures:
        converted_fahrenheit = convert_celsius_to_fahrenheit(celsius_temperature)
        converted_celsius = convert_fahrenheit_temperature_to_celsius(converted_fahrenheit)
        print(f'{celsius_temperature}\t\t{converted_celsius:.0f}')


if __name__ == "__main__":
    verify_temperature_conversions()
