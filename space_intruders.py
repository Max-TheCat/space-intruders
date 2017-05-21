import sys
import pygame

from game_settings import Settings

EXIT_SUCCESS = 0
APPLICATION_NAME = "Space Intruders"

game_settings = Settings()


def run_game():
    # Initialize display
    pygame.init()
    pygame.display.set_caption(APPLICATION_NAME)
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(EXIT_SUCCESS)

        screen.fill(game_settings.background_color)
        pygame.display.flip()

run_game()
