import os
import sys
import pygame
from pygame.locals import *


grid = [[' ' for i in range(0, 3)] for j in range(0, 3)]
winner = None
draw = None

def initboard(ttt):
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    pygame.draw.line(background, (0,0,0), (100, 0), (100, 300), 2)
    pygame.draw.line(background, (0,0,0), (200, 0), (200, 300), 2)

    pygame.draw.line(background, (0,0,0), (0, 100), (300, 100), 2)
    pygame.draw.line(background, (0,0,0), (0, 200), (300, 200), 2)
    return background


def drawStatus(board, player, winner):
    if(winner is None):
        message = player + "'s turn"
    elif(winner == "Draw"):
        message = "Draw"
    else:
        message = winner + " won!"

    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))

    board.fill((250, 250, 250), (0,300,300,350))
    board.blit(text, (10, 300))

def showBoard(ttt, board, player, winner):
    drawStatus(board, player, winner)
    ttt.blit(board, (0,0))
    pygame.display.flip()


def drawState(board, state):
    for row in range(3):
        for col in range(3):
            drawMove(board, row, col, state[row][col])


def drawMove(board, boardRow, boardCol, Piece):
    #print(state)
    centreX = ((boardCol)*100) + 50
    centreY = ((boardRow)*100) + 50

    if(Piece == 'O'):
        pygame.draw.circle(board, (0,0,0), (centreX, centreY), 44,2)
    elif(Piece == 'X'):
        pygame.draw.line(board, (0,0,0), (centreX - 22, centreY - 22), (centreX + 22, centreY + 22), 2)
        pygame.draw.line(board, (0,0,0), (centreX + 22, centreY - 22), (centreX - 22, centreY + 22), 2)
    grid[boardRow][boardCol] = Piece
    #print(state)




def gameWon(board, state):
    global winner, draw
    for row in range(0, 3):
        if((state[row][0]==state[row][1]==state[row][2]) and state[row][0] is not ' '):
            winner = state[row][0]
            pygame.draw.line(board, (250, 0, 0), (0, (row+1)*100-50), (300, (row+1)*100 -50), 2)
            return state[row][0]

    for col in range(0, 3):
        if ((state[0][col] == state[1][col] == state[2][col]) and (state[0][col] is not ' ')):
            winner = state[0][col]
            pygame.draw.line (board, (250,0,0), ((col + 1)* 100 - 50, 0),((col + 1)* 100 - 50, 300), 2)
            return state[0][col]

    if (state[0][0] == state[1][1] == state[2][2]) and (state[0][0] is not ' '):
        # game won diagonally left to right
        winner = state[0][0]
        pygame.draw.line (board, (250,0,0), (50, 50), (250, 250), 2)
        return state[1][1]

    if (state[0][2] == state[1][1] == state[2][0]) and (state[0][2] is not ' '):
        # game won diagonally right to left
        winner = state[0][2]
        pygame.draw.line (board, (250,0,0), (250, 50), (50, 250), 2)
        return state[1][1]
    return None


    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] is None:
                draw_flag = 1
    if draw_flag is 0:
        winner = "Draw"

    


#state = [[None, None, 'O'], [None, None, None], [None, None, 'X']]
def gameResult(state, player):
    pygame.init()
    #xo = player
    ttt = pygame.display.set_mode((300, 325))
    pygame.display.set_caption('Test Game')

    board = initboard(ttt)
    drawState(board, state)
    winner = gameWon(board, state)
    showBoard(ttt, board, player, winner)
    #print(2)
    # for event in pygame.event.get():
    #     if (event.type is pygame.QUIT or winner is not ' '):
    #         print(1)
    #         running = 0
    #     drawState(board, state)
    #     #gameWon(board, state)
    #     print(1)
    #     showBoard(ttt, board)

#gameResult(state)