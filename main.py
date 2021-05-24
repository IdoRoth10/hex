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
                return True
    return False


def press_enter_to_clean_screan(board : Board):
    pass


def clean_board():
    hex_list = get_hex_list()
    board = Board()
    return hex_list, board



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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    print(1)
                    hex_list = get_hex_list()
                    board = Board()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                if clicked_hexagon(mouse_x, mouse_y, hex_list, board, count):
                    count += 1
                    pygame.display.flip()
                if board.chekWin(1):
                    time.sleep(1)
                    screen.blit(settings.blue_winner, (220, -60))
                    pygame.display.flip()
                    time.sleep(5)
                    screen.fill(settings.background_colour)
                    hex_list, board = clean_board()
                    screen.blit(settings.hexBoard, (0, 0))



                if board.chekWin(2):
                    time.sleep(1)
                    screen.blit(settings.red_winner, (220, -60))
                    pygame.display.flip()
                    time.sleep(5)
                    screen.fill(settings.background_colour)
                    hex_list, board = clean_board()
                    screen.blit(settings.hexBoard, (0, 0))


            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    board = Board()
    gameloop(board)
