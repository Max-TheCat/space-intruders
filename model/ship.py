import pygame

from model import bullet


class Ship:
    """A player controlled ship"""
    __SHIP_SCALE_FACTOR = 0.09
    __SHIP_SPEED = 0.5

    def __init__(self, screen):
        self.__screen = screen

        width, height = screen.get_size()

        width = int(width * self.__SHIP_SCALE_FACTOR)
        height = int(height * self.__SHIP_SCALE_FACTOR)

        self.__image = pygame.image.load("images/ship.png")
        self.__image = pygame.transform.scale(self.__image, (width, height))
        self.rect = self.__image.get_rect()

        # Position to bottom centered
        self.center = float(self.__screen.get_rect().centerx)
        self.rect.centerx = self.center
        self.rect.bottom = self.__screen.get_rect().bottom

        self.is_moving_left = False
        self.is_moving_right = False

    def fire(self):
        return bullet.Bullet(self.__screen, self.rect)

    def draw(self):
        """Draws the player's ship on the screen"""
        self.__screen.blit(self.__image, self.rect)

    def update_position(self):
        """Updates the ship position according to its state"""
        if self.is_moving_left and self.rect.left > self.__screen.get_rect().left:
            self.center -= self.__SHIP_SPEED

        if self.is_moving_right and self.rect.right < self.__screen.get_rect().right:
            self.center += self.__SHIP_SPEED

        self.rect.centerx = self.center

    def is_off_screen(self):
        return False
