"""
This module parses a file containing constants and returns them as a dictionary.

__author__ = "Jackson"
"""


def parse_constants_file(file_path):
    """
    Parse a file containing constants and return them as a dictionary.

    Parameters:
        file_path (str): The path to the file containing constants.

    Returns:
        dict: A dictionary containing the parsed constants.

    Example:
        Suppose constants.txt contains the following lines:
        speed_of_light 299792458 m/s
        gravitational_constant 6.67430e-11 m^3/kg/s^2

        parse_constants_file('constants.txt') will return:
        {'speed_of_light': {'value': 299792458.0}, 'gravitational_constant': {'value': 6.6743e-11}}
    """
    constants = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, value, dimension = line.strip().split()
            constants[name] = dict(value=float(value))
    return constants


if __name__ == '__main__':
    # Test case
    # Input: constants.txt file containing constants and their values
    # Output: Dictionary containing the parsed constants
    constants_dict = parse_constants_file('constants.txt')
    print(constants_dict)
