import pygame, sys
from piece import *

playerColor = int(input("Enter 0 for white, 1 for black: "))

pygame.init()

LENGTH = 720
BLOCK_LENGTH = LENGTH / 8

screen = pygame.display.set_mode((LENGTH, LENGTH))
pygame.display.set_caption("Chess 2.0")
screen.fill([220,211,176])

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 1:
            screen.fill([65,125,20], pygame.Rect(j * BLOCK_LENGTH, i * BLOCK_LENGTH, BLOCK_LENGTH, BLOCK_LENGTH))

pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()