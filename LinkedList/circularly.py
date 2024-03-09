# Circular Music Visualizer:
# A circular linked list could be used to create a visualizer for music,
# where each node represents a frequency band or sound effect. The list
# could loop continuously, creating a dynamic visual display that reacts to the music.

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CIRCLE_RADIUS = 100
NUM_BANDS = 10
BAND_WIDTH = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circular Music Visualizer")


# Create a circular linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Generate random frequency bands
frequency_bands = [Node(random.randint(0, 255)) for _ in range(NUM_BANDS)]
for i in range(NUM_BANDS - 1):
    frequency_bands[i].next = frequency_bands[i + 1]
frequency_bands[NUM_BANDS - 1].next = frequency_bands[0]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the circular visualizer
    angle = 0
    band = frequency_bands[0]
    for _ in range(NUM_BANDS):
        color = (band.value, band.value, band.value)
        pygame.draw.arc(
            screen,
            color,
            (
                SCREEN_WIDTH // 2 - CIRCLE_RADIUS,
                SCREEN_HEIGHT // 2 - CIRCLE_RADIUS,
                CIRCLE_RADIUS * 2,
                CIRCLE_RADIUS * 2,
            ),
            angle,
            angle + (360 / NUM_BANDS),
            BAND_WIDTH,
        )
        angle += 360 / NUM_BANDS
        band = band.next

    # Update the display
    pygame.display.flip()

pygame.quit()
