import math

drag_coefficient = 0.2  # unitless
air_density = 1.2  # kg/m^3
radius = 11 / 100  # m
cross_area = math.pi * radius ** 2  # m^2
ball_mass = 0.43  # kg
gravitational_acceleration = 9.81  # m/s^2

# Convert velocities from km/h to m/s
v_hard_kick = 120 * 1000 / 3600  # m/s
v_soft_kick = 10 * 1000 / 3600  # m/s

# Calculating drag force and gravity force for hard kick
drag_force_hard_kick = 0.5 * drag_coefficient * air_density * cross_area * v_hard_kick ** 2  # N
gravitational_force_hard_kick = ball_mass * gravitational_acceleration  # N

# Calculating drag force and gravity force for soft kick
drag_force_soft_kick = 0.5 * drag_coefficient * air_density * cross_area * v_soft_kick ** 2  # N
gravitational_force_soft_kick = ball_mass * gravitational_acceleration  # N

# Ratio of drag force to gravity force for hard kick and soft kick
drag_gravity_ratio_hard_kick = drag_force_hard_kick / gravitational_force_hard_kick
drag_gravity_ratio_soft_kick = drag_force_soft_kick / gravitational_force_soft_kick

print(f"For a hard kick at {v_hard_kick:.2f} m/s:")
print(f"Drag Force: {drag_force_hard_kick:.1f} N")
print(f"Gravity Force: {gravitational_force_hard_kick:.1f} N")
print(f"Ratio of Drag Force to Gravity Force: {drag_gravity_ratio_hard_kick:.2f}")

print(f"\nFor a soft kick at {v_soft_kick:.2f} m/s:")
print(f"Drag Force: {drag_force_soft_kick:.1f} N")
print(f"Gravity Force: {gravitational_force_soft_kick:.1f} N")
print(f"Ratio of Drag Force to Gravity Force: {drag_gravity_ratio_soft_kick:.2f}")
