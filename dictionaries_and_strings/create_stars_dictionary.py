"""
This module provides functions to convert a list of tuples containing star data into a dictionary
and print information about a specific star from the generated dictionary.

__author__ = "Jackson"
"""


def convert_list_of_tuples(nearby_data_star):
    """
    Convert a list of tuples containing star data into a dictionary.

    Parameters:
        nearby_data_star (list): A list of tuples containing star data in the format
                                 (name, distance, apparent_brightness, luminosity).

    Returns:
        dict: A dictionary where the star names are keys and the values are dictionaries
              containing the star's distance, apparent brightness, and luminosity.

    Example:
        nearby_star_data = [
            ('Alpha Centauri A', 4.3, 0.26, 1.56),
            ('Alpha Centauri B', 4.3, 0.077, 0.45)
        ]

        convert_list_of_tuples(nearby_star_data) will return:
        {'Alpha Centauri A': {'distance': 4.3, 'apparent_brightness': 0.26, 'luminosity': 1.56},
         'Alpha Centauri B': {'distance': 4.3, 'apparent_brightness': 0.077, 'luminosity': 0.45}}
    """
    star_data = {}
    for star in nearby_data_star:
        name, distance, apparent_brightness, luminosity = star
        star_data[name] = {'distance': distance, 'apparent_brightness': apparent_brightness,
                           'luminosity': luminosity
                           }
    return star_data


def print_star_information(star_data, star_name):
    """
    Print information about a specific star.

    Parameters:
        star_data (dict): A dictionary containing star information.
        star_name (str): The name of the star to retrieve information for.

    Returns:
        None. Prints the star information.

    Example:
        stars = {'Alpha Centauri A': {'distance': 4.3, 'apparent_brightness': 0.26, 'luminosity': 1.56},
                 'Alpha Centauri B': {'distance': 4.3, 'apparent_brightness': 0.077, 'luminosity': 0.45}}

        print_star_information(stars, 'Alpha Centauri A') will print:
        Star: Alpha Centauri A
        Distance (ly): 4.3
        Apparent_brightness (m): 0.26
        Luminosity (m): 1.56
    """
    if star_name in star_data:
        star = star_data[star_name]
        print(f"Star: {star_name}")
        print(f"Distance (ly): {star['distance']}")
        print(f"Apparent_brightness (m): {star['apparent_brightness']}")
        print(f"Luminosity (m): {star['luminosity']}")
    else:
        print(f"No information available for star {star_name}")


if __name__ == '__main__':
    # Test case
    # Input: nearby_star_data containing star data
    # Output: Information about the specified stars
    nearby_star_data = [
        ('Alpha Centauri A', 4.3, 0.26, 1.56),
        ('Alpha Centauri B', 4.3, 0.077, 0.45),
        ('Barnard\'s Star', 6.0, 0.00004, 0.0005)
    ]

    stars = convert_list_of_tuples(nearby_star_data)

    print_star_information(stars, 'Alpha Centauri A')
    print_star_information(stars, "Barnard's Star")
