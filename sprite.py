import pygame


class Sprite:
    def __init__(self, img_width, img_height, color=0, pos=0):
        """
                    0 repesnt empty
                    1 repesnt blue
                    2 repesnt red
        """
        self.image = pygame.image.load("media/white.gif").convert_alpha()
        self.image = pygame.transform.scale(self.image, (img_width, img_height))
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        self.color = color
        self.pos = pos

    def draw(self, screen):
        self.rect.move_ip(self.x, self.y)
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_color(self, screen, color):
        if color == 0:
            self.image = pygame.image.load("media/white.gif").convert_alpha()
        elif color == 1:
            self.image = pygame.image.load("media/blue.gif").convert_alpha()
        elif color == 2:
            self.image = pygame.image.load("media/red.gif").convert_alpha()

        self.image = pygame.transform.scale(self.image, (35, 35))
        screen.blit(self.image, (self.rect.x, self.rect.y))