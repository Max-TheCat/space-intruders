import pygame
from pygame.sprite import Sprite

from game_settings import Settings


class Bullet(Sprite):
    """Represents a bullet fired from the ship"""
    __BULLET_SPEED = 1
    __WIDTH = 3
    __HEIGHT = 15

    def __init__(self, screen, initial_position):
        super(Bullet, self).__init__()

        self.__screen = screen

        self.top = float(initial_position.top)

        self.rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.rect.centerx = initial_position.centerx
        self.rect.top = self.top
        self.color = Settings().bullet_color

    def draw(self):
        """Draws the bullet on the screen"""
        pygame.draw.rect(self.__screen, self.color, self.rect)

    def update_position(self):
        """Updates the bullet position"""
        self.top -= self.__BULLET_SPEED
        self.rect.top = self.top

    def is_off_screen(self):
        return self.rect.bottom <= 0
