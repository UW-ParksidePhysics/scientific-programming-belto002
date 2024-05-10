"""
This script calculates the cooking time for eggs of different sizes and temperatures.

__author__ = "Jackson"
"""

import math

# Given constants
m_small = 47 / 1000  # kg
m_large = 67 / 1000  # kg
rho = 1.038  # g/cm^3 -> kg/L
c = 3.7  # J/g K -> kJ/kg K
k = 5.4 * 10 ** -3  # W/cm K -> kW/m K
T_w = 100  # C
T_y = 70  # C
T_0_fridge = 4  # C
T_0_room = 20  # C


def calculate_cook_time(mass, original_temp, t_minutes=None):
    """
    Calculate the cooking time for eggs of given mass and original temperature.

    Parameters:
        mass (float): Mass of the egg in kilograms.
        original_temp (int): Original temperature of the egg in Celsius.
        t_minutes (int): Optional parameter for returning the time in minutes. Default is None.

    Returns:
        tuple: A tuple containing the cooking time in seconds and minutes.

    """
    global T_0
    if original_temp == 4:
        T_0 = T_0_fridge
    elif original_temp == 20:
        T_0 = T_0_room

    t_seconds = ((mass ** (2 / 3)) * c * (rho ** (1 / 3))) / (
            k * (math.pi ** 2) * ((4 / 3) ** (2 / 3)) * math.log(0.76 * ((T_0 - T_w) / (T_y - T_w))))

    assert isinstance(t_minutes, object)
    return t_seconds, t_minutes


if __name__ == "__main__":
    # Test cases
    # Input: mass = m_large, original_temp = 4
    # Expected output: Large egg from fridge cook time = t_large_fridge_seconds s = t_large_fridge_minutes min
    t_large_fridge_seconds, t_large_fridge_minutes = calculate_cook_time(m_large, 4)
    print(f"Large egg from fridge cook time = {t_large_fridge_seconds:.1f} s = {t_large_fridge_minutes:.1f} min")

    # Input: mass = m_large, original_temp = 20
    # Expected output: Large egg from room temperature cook time = t_large_room_seconds s = t_large_room_minutes min
    t_large_room_seconds, t_large_room_minutes = calculate_cook_time(m_large, 20)
    print(f"Large egg from room temperature cook time = {t_large_room_seconds:.1f} s = {t_large_room_minutes:.1f} min")

    # Input: mass = m_small, original_temp = 4
    # Expected output: Small egg from fridge cook time = t_small_fridge_seconds s = t_small_fridge_minutes min
    t_small_fridge_seconds, t_small_fridge_minutes = calculate_cook_time(m_small, 4)
    print(f"Small egg from fridge cook time = {t_small_fridge_seconds:.1f} s = {t_small_fridge_minutes:.1f} min")

    # Input: mass = m_small, original_temp = 20
    # Expected output: Small egg from room temperature cook time = t_small_room_seconds s = t_small_room_minutes min
    t_small_room_seconds, t_small_room_minutes = calculate_cook_time(m_small, 20)
    print(f"Small egg from room temperature cook time = {t_small_room_seconds:.1f} s = {t_small_room_minutes:.1f} min")
