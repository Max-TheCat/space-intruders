import pygame

from game_settings import Settings
from model import Ship
import controller.helper_functions as game_functions

APPLICATION_NAME = "Space Intruders"

game_settings = Settings()


def run_game():
    # Initialize display
    pygame.init()
    pygame.display.set_caption(APPLICATION_NAME)
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    ship = Ship(screen)

    elements = [ship]

    # Main game loop
    while True:
        game_functions.check_events(ship, elements)
        game_functions.update_positions(elements)
        game_functions.refresh_screen(screen, game_settings.background_color, elements)


run_game()
