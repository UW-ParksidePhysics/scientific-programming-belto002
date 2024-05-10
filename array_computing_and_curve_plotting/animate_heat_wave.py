"""
Simulate temperature variations over depth and time.

This script simulates temperature variations over depth and time using a mathematical model
that incorporates both annual and diurnal oscillations. It visualizes the temperature profile
over a 24-hour period at different depths.

__author__ = "Jackson"
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
k = 1e-6  # Thermal diffusivity (m^2/s)
A1 = 15  # Amplitude of annual variations (Celsius)
A2 = 7  # Amplitude of diurnal variations (Celsius)
P1 = 365  # Period of annual oscillations (days)
P2 = 24  # Period of daily (diurnal) oscillations (hours)
t_delta = P2 / 10  # Time resolution (hours)

# Calculate other parameters
omega1 = 2 * np.pi / P1
omega2 = 2 * np.pi / P2
a1 = np.sqrt(omega1 / (2 * k))
a2 = np.sqrt(omega2 / (2 * k))


# Define temperature function
def temperature(z, t):
    annual_variation = A1 * np.exp(-a1 * z) * np.sin(omega1 * t - a1 * z)
    diurnal_variation = A2 * np.exp(-a2 * z) * np.sin(omega2 * t - a2 * z)
    return annual_variation + diurnal_variation


# Set up plot
fig, ax = plt.subplots()
ax.set_xlim(0, 24)
ax.set_ylim(0, 20)
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Depth (m)')
line, = ax.plot([], [], lw=2)

# Initialize lines
lines = [ax.plot([], [], lw=2)[0] for _ in range(2)]


# Initialization function
def init():
    for temp_line in lines:
        temp_line.set_data([], [])
    return lines


# Animation function
def animate(t):
    # Depth values
    z_values = np.linspace(0, 20, 100)

    # Calculate temperature at each depth
    temperatures = [temperature(z, t) for z in z_values]

    # Update plot
    lines[0].set_data(np.arange(0, 24, t_delta), temperatures)
    lines[1].set_data(np.arange(0, 24, t_delta), z_values)
    return lines


# Create animation
anim = FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, 24, t_delta), interval=100, blit=True)

# Show plot
plt.show()

# Test block
if __name__ == '__main__':
    # Run some tests or output additional information here
    pass
