import sys
import pygame

EXIT_SUCCESS = 0
APPLICATION_NAME = "Space Intruders"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = (230, 230, 230)


def run_game():
    # Initialize display
    pygame.init()
    pygame.display.set_caption(APPLICATION_NAME)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(EXIT_SUCCESS)

        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()


run_game()
