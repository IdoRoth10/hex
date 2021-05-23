import pygame
import time
import numpy as np
from pygame import locals as py_loc
import sys
import os

from backend import Board
import settings
import sprite
pygame.init()

blue = pygame.image.load("media/blue.gif")
blue = pygame.transform.scale(blue, (35, 35))
red = pygame.image.load("media/red.gif")
red = pygame.transform.scale(red, (35, 35))
blue_confeti = pygame.image.load("media/blue_confeti.png")
blue_confeti = pygame.transform.scale(blue_confeti, (800, 600))

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
        row_matrix = list()
        for col in range(11):
            hexagon = sprite.Sprite(settings.img_height, settings.img_width)
            hexagon.x = settings.dx * (col+1) + x
            hexagon.y = y
            row_matrix.append(hexagon)
        hex_matrix.append(row_matrix)
        y += settings.dy
        x = settings.x_switc_col * (row+1)

    return hex_matrix


def draw_hex(hex_matrix):
    global screen
    for hex_row in hex_matrix:
        for hex in hex_row:
            hex.draw(screen)


def clicked_hexagon(x, y, hex_matrix, board: Board, count):
    for i in range(settings.size):
        for j in range(settings.size):
            if hex_matrix[i][j].rect.collidepoint(x, y) and board.get_value(i, j) == 0:
                board.set_value(i, j, (count % 2) + 1)
                hex_matrix[i][j].change_color(screen, (count % 2) + 1)
                print(board)
                return True
    return False



def gameloop(board: Board):
    running = True
    count = 0
    hex_list = get_hex_list()
    while running:
        draw_hex(hex_list)
        screen.blit(settings.text, (38, 22))
        #picture_turn(screen, count)
        if count % 2 == 0:
            screen.blit(blue, (160, 16))
        else:
            screen.blit(red, (160, 16))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                if clicked_hexagon(mouse_x, mouse_y, hex_list, board, count):
                    count += 1
                if board.chekWin(1):
                    print("P1 WON")
                    screen.blit(blue_confeti, (0, 0))


            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    board = Board()
    gameloop(board)
