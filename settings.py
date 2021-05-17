import pygame

width = 800
height = 600
WIDTH = 60
HEIGHT = 60
background_colour = (255, 255, 255)
x = 30
y = 78
x_switc_col = 23
dx = 45
dy = 45
img_width = 35
img_height = 35

hexBoard = pygame.image.load('media/HexBoard.png')
hexBoard = pygame.transform.scale(hexBoard, (width, height))
