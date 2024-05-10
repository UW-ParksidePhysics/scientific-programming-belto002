from vpython import sphere, vector, rate, color

# Define properties of balls
ball1_pos = vector(-5, 0, 0)
ball1_velocity = vector(1, 1, 1)
ball2_pos = vector(5, 0, 0)
ball2_velocity = vector(-1, -1, -1)

# Create balls
ball1 = sphere(pos=ball1_pos, radius=0.5, color=color.red)
ball2 = sphere(pos=ball2_pos, radius=0.5, color=color.blue)

# Define trails for balls
trail1 = sphere(pos=ball1_pos, radius=0.1, color=color.red, make_trail=True, retain=100)
trail2 = sphere(pos=ball2_pos, radius=0.1, color=color.blue, make_trail=True, retain=100)

# Animation loop
while True:
    rate(100)

    # Update positions of balls
    ball1.pos += ball1_velocity
    ball2.pos += ball2_velocity

    # Update positions of trails
    trail1.pos = ball1.pos
    trail2.pos = ball2.pos
