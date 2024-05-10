"""
This module contains functions to calculate velocity and acceleration using finite difference approximations.

__author__ = "Jackson"
"""


def calculate_velocity_and_acceleration(positions, index, time_step=1e-6):
    """
    Calculate velocity and acceleration using finite difference approximations.

    Parameters:
        positions (list): A list of positions at different time points.
        index (int): The index for which to calculate velocity and acceleration.
        time_step (float, optional): The time step between each position. Default is 1e-6.

    Returns:
        tuple: A tuple containing velocity and acceleration.

    Example:
        calculate_velocity_and_acceleration([0, 5, 15, 22], 1, 0.5)
    """
    # Extract positions and times for the current, previous, and next points
    x_i_minus_1 = positions[index - 1]
    x_i = positions[index]
    x_i_plus_1 = positions[index + 1]

    t_i_minus_1 = index - 1
    t_i = index
    t_i_plus_1 = index + 1

    # Calculate velocity using finite difference approximation
    v_i = (x_i_plus_1 - x_i_minus_1) / (t_i_plus_1 - t_i_minus_1)

    # Calculate acceleration using finite difference approximation
    a_i = (2 / (t_i_plus_1 - t_i_minus_1)) * (
            (x_i_plus_1 - x_i) / (t_i_plus_1 - t_i + time_step) - (x_i - x_i_minus_1) / (t_i - t_i_minus_1 + time_step))

    return v_i, a_i


def test_kinematics():
    """
    Test function for kinematics calculations.

    Returns:
        None.
    """
    # Define positions and time step
    positions = [0, 5, 15, 22]
    time_step = 0.5

    # Print input parameters
    print("Input:")
    print(f"Positions: {positions}")
    print(f"Time step: {time_step}")

    print("\nResults:")
    # Iterate over positions to calculate velocity and acceleration
    for i in range(1, len(positions) - 1):
        v_i, a_i = calculate_velocity_and_acceleration(positions, i, time_step)
        # Print velocity and acceleration at each index
        print(f"At index {i}:")
        print(f"Velocity: {v_i}")
        print(f"Acceleration: {a_i}")
        print()


if __name__ == "__main__":
    test_kinematics()
