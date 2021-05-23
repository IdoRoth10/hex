import pygame
pygame.font.init()

width = 800
height = 600
WIDTH = 60
HEIGHT = 60
background_colour = (255, 255, 255)
x = 30
y = 72
x_switc_col = 23.5
dx = 45
dy = 42
img_width = 35
img_height = 35
size = 11

font = pygame.font.Font('freesansbold.ttf', 24)
text = font.render('TURN OF:', True, (0, 0, 0))

hexBoard = pygame.image.load('media/HexBoard.png')
hexBoard = pygame.transform.scale(hexBoard, (width, height))
