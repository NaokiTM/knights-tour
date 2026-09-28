
# CONTAINS FUNCTIONS: 
# resetChessBoard()
# nextmove()
# draw_board()
# game_auto()

import pygame
import sys
import random
import time

from colours import *

pygame.init()

# resets the chessboard after a game ()
def resetChessBoard(array):
    for row in array:
        for i in range(len(row)):
            row[i] = 0


def nextmove(chessBoard, chessBoardVisited, playerPos, SQUARES_ACROSS):
    smallest_value = 7
    smallest_value_position = None

    knight_moves = [
        (-2, -1), (-2, 1),
        (2, -1), (2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2)
    ]

    # Calculate number of outer moves
    for moveset in knight_moves:

        possible_moves_count = 0

        x1 = playerPos[0] + moveset[0]
        y1 = playerPos[1] + moveset[1]

        # Check that possible move is in bounds and unvisited
        if (
            0 <= x1 < SQUARES_ACROSS
            and 0 <= y1 < SQUARES_ACROSS
            and chessBoardVisited[x1][y1] != 1
        ):

            # Calculate outer moves
            for outer_moveset in knight_moves:

                x2 = x1 + outer_moveset[0]
                y2 = y1 + outer_moveset[1]

                if 0 <= x2 < SQUARES_ACROSS and 0 <= y2 < SQUARES_ACROSS:

                    if chessBoardVisited[x2][y2] == 0:
                        possible_moves_count += 1

            chessBoard[x1][y1] = possible_moves_count

    # Find move with smallest number of outer moves
    for moveset in knight_moves:

        x1 = playerPos[0] + moveset[0]
        y1 = playerPos[1] + moveset[1]

        if (
            0 <= x1 < SQUARES_ACROSS
            and 0 <= y1 < SQUARES_ACROSS
            and chessBoardVisited[x1][y1] != 1
        ):

            possible_move = chessBoard[x1][y1]

            if smallest_value >= possible_move:
                smallest_value = possible_move
                smallest_value_position = [x1, y1]

    # Update player position
    if smallest_value_position:

        playerPos = smallest_value_position
        chessBoardVisited[playerPos[0]][playerPos[1]] = 1

    return playerPos


def draw_board(screen, SQUARES_ACROSS, SQUARE_SIZE, chessBoard, chessBoardVisited, playerPos):
    font = pygame.font.Font(None, SQUARE_SIZE - 5)

    # Import and resize knight
    knight_image_big = pygame.image.load("./assets/knight.png")
    knight_image = pygame.transform.scale(
        knight_image_big,
        (SQUARE_SIZE, SQUARE_SIZE)
    )

    # Draw each square
    for x in range(SQUARES_ACROSS):
        for y in range(SQUARES_ACROSS):

            # Determine square colour
            if chessBoardVisited[x][y] == 1:
                color = VISITEDCOLOUR

            elif (x + y) % 2 == 0:
                color = LIGHT_WOOD

            else:
                color = DARK_WOOD

            # Draw square
            pygame.draw.rect(
                screen,
                color,
                (
                    x * SQUARE_SIZE,
                    y * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE
                )
            )

            # Draw knight
            if playerPos[0] == x and playerPos[1] == y:
                screen.blit(
                    knight_image,
                    (x * SQUARE_SIZE, y * SQUARE_SIZE)
                )

            # Draw number of possible moves
            if chessBoard[x][y] > 0:

                num = chessBoard[x][y]
                num_text = str(num)

                render_num = font.render(
                    num_text,
                    True,
                    BLACK
                )

                screen.blit(
                    render_num,
                    (
                        (x * SQUARE_SIZE) + SQUARE_SIZE / 2,
                        (y * SQUARE_SIZE) + SQUARE_SIZE / 2
                    )
                )

    pygame.display.flip()


def game_auto(SQUARES_ACROSS):
    PIXELS_ACROSS = SQUARES_ACROSS * 30
    SQUARE_SIZE = PIXELS_ACROSS // SQUARES_ACROSS

    # Random starting position
    startPosX = random.randint(0, SQUARES_ACROSS - 1)
    startPosY = random.randint(0, SQUARES_ACROSS - 1)

    playerPos = [startPosX, startPosY]

    # Create boards
    chessBoard = [
        [0 for y in range(SQUARES_ACROSS)]
        for x in range(SQUARES_ACROSS)
    ]

    chessBoardVisited = [
        [0 for y in range(SQUARES_ACROSS)]
        for x in range(SQUARES_ACROSS)
    ]

    # Create game window
    screen = pygame.display.set_mode(
        (PIXELS_ACROSS, PIXELS_ACROSS)
    )

    while True:
        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update player position
        playerPos = nextmove(
            chessBoard,
            chessBoardVisited,
            playerPos,
            SQUARES_ACROSS
        )

        # Draw board
        draw_board(
            screen,
            SQUARES_ACROSS,
            SQUARE_SIZE,
            chessBoard,
            chessBoardVisited,
            playerPos
        )

        # Check if tour is complete
        if all(all(row) for row in chessBoardVisited):

            print("Knight's tour completed!")
            break

        # Reset possible moves
        resetChessBoard(chessBoard)

        time.sleep(0.1)