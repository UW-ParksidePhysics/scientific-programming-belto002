"""
Simulate projectile motion on Earth, Mars, and the Moon.

__author__ = "Jackson"
"""

from vpython import box, sphere, vector, color, label, rate, points

# Constants
g_earth = -9.8
g_mars = -3.7
g_moon = -1.6

# Create fields and labels
earth_field = box(pos=vector(0, 0, 0), size=vector(20, 20, 0.1), color=color.green)
mars_field = box(pos=vector(-25, 0, 0), size=vector(20, 20, 0.1), color=color.red)
moon_field = box(pos=vector(25, 0, 0), size=vector(20, 20, 0.1), color=color.gray(0.5))

earth_label = label(pos=vector(0, -10, 0), text="EARTH", color=color.green)
mars_label = label(pos=vector(-25, -10, 0), text="MARS", color=color.red)
moon_label = label(pos=vector(25, -10, 0), text="MOON", color=color.gray(0.5))


# Function to simulate projectile motion
def projectile_motion(g, ball_color):
    """
        Simulate projectile motion given gravitational acceleration and ball color.

        Parameters:
            g (float): Gravitational acceleration.
            ball_color (color): Color of the projectile.

        Returns:
            None
        """
    start_pos = vector(-9, -9, 0)
    end_pos = vector(9, 9, 0)

    # Create ball and trail
    ball = sphere(pos=start_pos, radius=0.5, color=ball_color, make_trail=True, retain=100)
    trail = points(color=ball_color)

    # Simulation loop
    while ball.pos.y < end_pos.y:
        rate(100)
        ball.velocity += vector(0, 0, g)
        ball.pos += ball.velocity
        trail.append(pos=ball.pos)


# Run simulation for Earth
projectile_motion(g_earth, color.blue)

# Pause simulation
rate(1)

# Run simulation for Mars
projectile_motion(g_mars, color.pink)

# Pause simulation
rate(1)

# Run simulation for Moon
projectile_motion(g_moon, color.white)

if __name__ == "__main__":
    # Test case
    # Input: Gravitational acceleration of Earth, Mars, and the Moon, and respective ball colors
    # Output: Visualization of projectile motion on Earth, Mars, and the Moon
    projectile_motion(g_earth, color.blue)
    rate(1)
    projectile_motion(g_mars, color.pink)
    rate(1)
    projectile_motion(g_moon, color.white)
