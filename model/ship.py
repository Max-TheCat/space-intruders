import pygame


class Ship:
    """A player controlled ship"""
    __SHIP_SCALE_FACTOR = 0.09

    def __init__(self, screen):
        self.__screen = screen

        width, height = screen.get_size()

        width = int(width * self.__SHIP_SCALE_FACTOR)
        height = int(height * self.__SHIP_SCALE_FACTOR)

        self.__image = pygame.image.load("images/ship.png")
        self.__image = pygame.transform.scale(self.__image, (width, height))
        self.rect = self.__image.get_rect()

        # Position to bottom centered
        self.rect.centerx = self.__screen.get_rect().centerx
        self.rect.bottom = self.__screen.get_rect().bottom

        self.is_moving_left = False
        self.is_moving_right = False

    def blit(self):
        """Draws the player's ship on the screen"""
        self.__screen.blit(self.__image, self.rect)

    def update_position(self):
        """Updates the ship position according to its state"""
        if self.is_moving_left and self.rect.left > self.__screen.get_rect().left:
            self.rect.left -= 1

        if self.is_moving_right and self.rect.right < self.__screen.get_rect().right:
            self.rect.right += 1
