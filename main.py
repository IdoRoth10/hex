import pygame
import numpy as np
from backend import Board
import settings
import sprite
pygame.init()


screen = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption('HEX')
screen.fill(settings.background_colour)
screen.blit(settings.hexBoard, (0, 0))
pygame.display.flip()
rect_list = list()


def get_hex_list():
    hex_matrix = []
    x = 5
    y = settings.y
    for row in range(11):
        for col in range(11):
            hexagon = sprite.Sprite(settings.img_height, settings.img_width)
            hexagon.x = settings.dx * (col+1) + x
            hexagon.y = y
            hex_matrix.append(hexagon)
        y += settings.dy
        x = settings.x * (row+1)

    return hex_matrix


def draw_hex(hex_matrix):
    global screen
    for hex in hex_matrix:
        hex.draw(screen)


"""
def drawBoard():
    global rect_list
    x = 5
    y = settings.y
    screen.fill((255, 255, 255))
    screen.blit(settings.hexBoard, (0, 0))
    for row in range(11):
        row_rect = list()
        for col in range(11):
            x += settings.dx
            row_rect.append(pygame.Rect(x, y, settings.WIDTH, settings.HEIGHT))
            screen.blit(settings.blue, row_rect[col])
        rect_list.append(row_rect)
        y += settings.dy
        x = settings.x_switc_col * (row+1)
    pygame.display.flip()
"""


def gameloop(board: Board):
    running = True
    hex_list = get_hex_list()
    while running:
        draw_hex(hex_list)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False


if __name__ == "__main__":
    board = Board()
    gameloop(board)
