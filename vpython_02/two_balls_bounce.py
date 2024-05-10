from vpython import sphere, vector, rate

wall_pos = 0
wall_width = 1

ball1 = sphere(pos=vector(-5, -5, 0), radius=0.5, color=vector(1, 0, 0), velocity=vector(1, 1, 0))
ball2 = sphere(pos=vector(-5, 5, 0), radius=0.5, color=vector(0, 0, 1), velocity=vector(1, -1, 0))

while True:
    rate(100)
    ball1.pos += ball1.velocity
    ball2.pos += ball2.velocity

    # Check collision with the wall for ball1
    if abs(ball1.pos.x - wall_pos) <= ball1.radius + wall_width / 2:
        ball1.velocity.x *= -1

    # Check collision with the wall for ball2
    if abs(ball2.pos.x - wall_pos) <= ball2.radius + wall_width / 2:
        ball2.velocity.x *= -1
