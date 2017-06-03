import pygame
import sys

__EXIT_SUCCESS = 0


def check_events(ship, elements):
    """Reacts to pygame events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(__EXIT_SUCCESS)
        elif hasattr(event, "key") and event.key == pygame.K_LEFT:
            ship.is_moving_left = event.type == pygame.KEYDOWN
        elif hasattr(event, "key") and event.key == pygame.K_RIGHT:
            ship.is_moving_right = event.type == pygame.KEYDOWN
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            elements.append(ship.fire())


def update_positions(elements):
    """Updates the position of all game elements"""
    # Loop through a copy of the list so items can be removed from the original
    for element in list(elements):
        element.update_position()

        if element.is_off_screen():
            elements.remove(element)


def refresh_screen(screen, background_color, elements):
    """Refreshes all the elements before repainting the screen"""
    screen.fill(background_color)

    for element in elements:
        element.draw()

    pygame.display.flip()
