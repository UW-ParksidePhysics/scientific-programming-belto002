"""
Birthday Space Station simulation.

__author__ = "Jackson"
"""

import pygame
from pygame.locals import *
import numpy as np


def simulate_space_station(my_birthdate, partner_birthdate):
    """
    Simulate a rotating space station with two balls and rotating rings.

    Parameters:
        my_birthdate (int): Day of birth for the user.
        partner_birthdate (int): Day of birth for the partner.

    Returns:
        None
    """
    # Set up pygame
    pygame.init()

    # Pick the value closest to 1 as rotation period
    rotation_period = 1 / ((my_birthdate + partner_birthdate) / 2)

    # Set up the display
    width, height = 800, 600
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Birthday Space Station")

    # Colors
    background_color = (255, 255, 255)  # White
    ball_color = (255, 0, 0)  # Red
    ring_color = (0, 0, 255)  # Blue (changed from green)

    # Main loop
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Clear the screen
        display.fill(background_color)

        # Draw balls
        pygame.draw.circle(display, ball_color, (400, 300), 20)

        # Draw rotating rings
        for angle in np.arange(0, 2 * np.pi, np.pi / 10):
            x = int(400 + 100 * np.cos(angle))
            y = int(300 + 100 * np.sin(angle))
            pygame.draw.circle(display, ring_color, (x, y), 10)

        # Update the display
        pygame.display.update()

        # Rotate the space station
        # Rotate at a period equal to rotation_period
        pygame.time.wait(int(rotation_period * 1000))
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    # Test case
    # Input: User's birthdate: 6, Partner's birthdate: 24
    # Output: Simulated rotating space station
    simulate_space_station(6, 24)
