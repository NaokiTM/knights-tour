import pygame
import sys
import random
import time
pygame.init()

def game_auto(SQUARES_ACROSS):

  #every square in the chessboard array is iteratively reset to not store possible moves from the previous turn
  def resetChessBoard(array):    
    for row in array:
      for i in range (len(row)):
        row[i] = 0

  #each square is 30 pixels across 
  PIXELS_ACROSS = SQUARES_ACROSS * 30
  SQUARE_SIZE = PIXELS_ACROSS // SQUARES_ACROSS 

  #randomly determines starting position for the player
  startPosX = random.randint(0, SQUARES_ACROSS -1)                
  startPosY = random.randint(0, SQUARES_ACROSS -1)
  playerPos = [startPosX, startPosY]

  #chessBoard array stores all possible moves for the player (resets every turn)
  #chessBoardVisited stores 0 if not visited, 1 if visited, for all squares
  chessBoard = [[0 for y in range(SQUARES_ACROSS)] for x in range(SQUARES_ACROSS)]
  chessBoardVisited = [[0 for y in range(SQUARES_ACROSS)] for x in range(SQUARES_ACROSS)]

  # creates a new pygame display defined as a square that has dimensions matching the size of the chessboard
  screen = pygame.display.set_mode((PIXELS_ACROSS, PIXELS_ACROSS))

  
  def nextmove(chessBoard, playerPos):
    smallest_value = 7
    smallest_value_position = None
    knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]  #move patterns of the knight (L shape)

    # this loop calculates and stores the number of possible outer moves there are from the possible move
    for moveset in knight_moves:
        possible_moves_count = 0
        x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1]

        # doesnt count moves that are out of bounds or visited
        if 0 <= x1 < SQUARES_ACROSS and 0 <= y1 < SQUARES_ACROSS and chessBoardVisited[x1][y1] != 1:
            
            # adds 1 to the value of possible moves when a valid outer move is found 
            for outer_moveset in knight_moves: 
                x2, y2 = x1 + outer_moveset[0], y1 + outer_moveset[1]
                if 0 <= x2 < SQUARES_ACROSS and 0 <= y2 < SQUARES_ACROSS:
                    if chessBoardVisited[x2][y2] == 0: # checks if any of the outermost possible moves have been marked as visited, in which case they are not counted
                        possible_moves_count += 1
            
            #chessboard array is updated with numbers of outer possible moves for each possible move
            chessBoard[x1][y1] = possible_moves_count


    # this loop calculates move with the least outer possible moves, and updates player position to it
    for moveset in knight_moves: 
      # x1 and y1 are loop variables that hold the x and y coordinates of each of the possible moves from the player position
      x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1] 
      if 0 <= x1 < SQUARES_ACROSS and 0 <= y1 < SQUARES_ACROSS and chessBoardVisited[x1][y1] != 1: 
        possible_move = chessBoard[x1][y1]

        # finds smallest possible move 
        if smallest_value >= possible_move:   
          smallest_value = possible_move  
          smallest_value_position = [x1, y1]

    #player position set to smallest possible move, new player position marked as visited
    if smallest_value_position:
        playerPos = smallest_value_position
        chessBoardVisited[playerPos[0]][playerPos[1]] = 1  

    return playerPos
  
     
  def draw_board(playerPos): 
    #defines colours and fonts
    font = pygame.font.Font(None, SQUARE_SIZE - 5)
    WHITE = pygame.Color("burlywood1")   
    BLACK = pygame.Color("chocolate4")  
    VISITEDCOLOUR = pygame.Color("aquamarine4")

    #imports and resizes knight image to fit square
    knight_image_big = pygame.image.load("knight.png")
    knight_image = pygame.transform.scale(knight_image_big, (SQUARE_SIZE, SQUARE_SIZE))

    #loops for each square on the board
    for x in range(SQUARES_ACROSS):          
        for y in range(SQUARES_ACROSS):         
            
            #determines colour of square depending on visited status
            if chessBoardVisited[x][y] == 1: 
              color = VISITEDCOLOUR 
            elif (x + y) % 2 == 0:
              color = WHITE
            else:
              color = BLACK

            #draws each square on to the board, starting from the top left corner
            pygame.draw.rect(
                screen, color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            ) 

            #draws knight image onto board
            if playerPos[0] == x and playerPos[1] == y:
              screen.blit(knight_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))

            #draw number of possible moves onto board
            if chessBoard[x][y] > 0:
              num = chessBoard[x][y]
              num_text = str(num)

              render_num = font.render(num_text, True, (0,0,0))

              #prints the number of moves specified in the chessboard array (num), and blits the number in the center of the corresponding square
              screen.blit(render_num, ((x * SQUARE_SIZE) + SQUARE_SIZE / 2, (y * SQUARE_SIZE) + SQUARE_SIZE / 2))


    pygame.display.flip()


  #main game loop
  while True: 
    #pygame.quit handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:       
        pygame.quit()
        sys.exit() 

    #updates player position each turn, and updates(draws) board accordingly
    playerPos = nextmove(chessBoard, playerPos)
    draw_board(playerPos) 

    #exits main game loop when all squares visited
    if all(all(row) for row in chessBoardVisited):
      print("Knight's tour completed!")
      break

    #resets possible moves in the chessboard array, to be recalculated from the new player position
    resetChessBoard(chessBoard)
    time.sleep(0.1)

game_auto(8)