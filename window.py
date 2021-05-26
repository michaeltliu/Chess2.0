import pygame, sys
from game import *
from piece import *

playerColor = int(input("Enter 1 for white, -1 for black: "))

pygame.init()

LENGTH = 720
BLOCK_LENGTH = LENGTH // 8

screen = pygame.display.set_mode((LENGTH, LENGTH))
pygame.display.set_caption("Chess 2.0")
screen.fill([220,211,176])

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 1:
            screen.fill([65,125,20], pygame.Rect(j * BLOCK_LENGTH, i * BLOCK_LENGTH, BLOCK_LENGTH, BLOCK_LENGTH))

pieceTypes = ["pawn", "bishop", "knight", "rook", "queen", "king"]
pieceImages = dict()
for i in range(2):
    for j in pieceTypes:
        if i == 0:
            pathname = "w"
        else:
            pathname = "b"

        pathname += j
        img = pygame.image.load("img/{}.png".format(pathname))
        img = pygame.transform.smoothscale(img, (BLOCK_LENGTH, BLOCK_LENGTH))
        pieceImages[pathname] = img

game = Game(playerColor)

for piece in game.pieces.values():
    pieceSpec = ""
    if piece.color == 1:
        pieceSpec += "w"
    elif piece.color == -1:
        pieceSpec += "b"

    if type(piece) == Pawn:
        pieceSpec += "pawn"
    elif type(piece) == Bishop:
        pieceSpec += "bishop"
    elif type(piece) == Knight:
        pieceSpec += "knight"
    elif type(piece) == Rook:
        pieceSpec += "rook"
    elif type(piece) == Queen:
        pieceSpec += "queen"
    elif type(piece) == King:
        pieceSpec += "king"

    x = piece.loc % 8
    y = piece.loc // 8
    screen.blit(pieceImages[pieceSpec], (x * BLOCK_LENGTH, y * BLOCK_LENGTH))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.mouse.get_pos()