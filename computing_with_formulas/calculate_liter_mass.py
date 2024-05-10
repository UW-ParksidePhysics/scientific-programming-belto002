"""
This script calculates the mass of 1 liter of various substances in grams.

__author__ = "Jackson"
"""

if __name__ == "__main__":
    # Test case
    # Input: densities in g/cm^3
    # Expected output: Mass of 1 liter of each substance
    iron_density = 7.87  # g/cm^3
    air_density = 0.0012  # g/cm^3
    gasoline_density = 0.755  # g/cm^3
    ice_density = 0.917  # g/cm^3
    human_body_density = 1.010  # g/cm^3
    silver_density = 10.49  # g/cm^3
    platinum_density = 21.45  # g/cm^3

    # Calculate mass of 1 liter of substance in grams
    iron_mass = iron_density * 1000
    air_mass = air_density * 1000
    gasoline_mass = gasoline_density * 1000
    ice_mass = ice_density * 1000
    human_body_mass = human_body_density * 1000
    silver_mass = silver_density * 1000
    platinum_mass = platinum_density * 1000

    # Output mass
    print("Mass of 1 liter of iron:", iron_mass, "g")
    print("Mass of 1 liter of air:", air_mass, "g")
    print("Mass of 1 liter of gasoline:", gasoline_mass, "g")
    print("Mass of 1 liter of ice:", ice_mass, "g")
    print("Mass of 1 liter of human body:", human_body_mass, "g")
    print("Mass of 1 liter of silver:", silver_mass, "g")
    print("Mass of 1 liter of platinum:", platinum_mass, "g")
