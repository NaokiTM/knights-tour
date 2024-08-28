import pygame
import sys
import random
import time
pygame.init()

def game_auto(SQUARES_ACROSS):

  def resetChessBoard(array):    
    for row in array:
      for i in range (len(row)):
        row[i] = 0

  PIXELS_ACROSS = SQUARES_ACROSS * 30
  SQUARE_SIZE = PIXELS_ACROSS // SQUARES_ACROSS 

  startPosX = random.randint(0, SQUARES_ACROSS -1)                
  startPosY = random.randint(0, SQUARES_ACROSS -1)
  playerPos = [startPosX, startPosY]


  chessBoard = [[0 for y in range(SQUARES_ACROSS)] for x in range(SQUARES_ACROSS)]
  chessBoardVisited = [[0 for y in range(SQUARES_ACROSS)] for x in range(SQUARES_ACROSS)]


  screen = pygame.display.set_mode((PIXELS_ACROSS, PIXELS_ACROSS))
  pygame.display.set_caption("knights tour")

     
  def nextmove(chessBoard, playerPos):
    smallest_value = 7
    smallest_value_position = None
    knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]  #move patterns of the knight

    #calculates and stores possible moves 
    for moveset in knight_moves: 
      possible_moves_count = 0;
      x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1] 
      if 0 <= x1 < SQUARES_ACROSS and 0 <= y1 < SQUARES_ACROSS:
        possible_move = [x1, y1]     

        for moveset in knight_moves: #counts outer moves from each possible_move
          x2, y2 = possible_move[0] + moveset[0], possible_move[1] + moveset[1];  
          if 0 <= x2 < SQUARES_ACROSS and 0 <= y2 < SQUARES_ACROSS: 
            if x2 != playerPos[0] or y2 != playerPos[1]:
              possible_moves_count += 1
        chessBoard[x1][y1] = possible_moves_count

    #finds the smallest move and moves the player to this square. 
    for moveset in knight_moves:
      x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1] 

      if 0 <= x1 < SQUARES_ACROSS and 0 <= y1 < SQUARES_ACROSS and chessBoardVisited[x1][y1] != 1: 

        possible_move = chessBoard[x1][y1]

        if smallest_value >= possible_move:  
          smallest_value = possible_move  
          smallest_value_position = [x1, y1]

    if smallest_value_position:
        playerPos = smallest_value_position
        chessBoardVisited[playerPos[0]][playerPos[1]] = 1

    return playerPos
  
     
  def draw_board(playerPos): 
    font = pygame.font.Font(None, SQUARE_SIZE - 5)
    WHITE = pygame.Color("burlywood1")   
    BLACK = pygame.Color("chocolate4")  
    VISITEDCOLOUR = pygame.Color("aquamarine4")

    #imports and resizes knight image to fit square
    knight_image_big = pygame.image.load("knight.png")
    knight_image = pygame.transform.scale(knight_image_big, (SQUARE_SIZE, SQUARE_SIZE))

    for x in range(SQUARES_ACROSS):          
        for y in range(SQUARES_ACROSS):         
            
            if chessBoardVisited[x][y] == 1: 
              color = VISITEDCOLOUR 
            elif (x + y) % 2 == 0:
              color = WHITE
            else:
              color = BLACK

            pygame.draw.rect(
                screen, color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            ) 

            if playerPos[0] == x and playerPos[1] == y:
              screen.blit(knight_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))

            #draw number of possible moves onto screen
            if chessBoard[x][y] > 0:
              num = chessBoard[x][y]
              num_text = str(num)

              render_num = font.render(num_text, True, (0,0,0))
              screen.blit(render_num, ((x * SQUARE_SIZE) + SQUARE_SIZE / 2, (y * SQUARE_SIZE) + SQUARE_SIZE / 2))


    pygame.display.flip()


  while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:       
        pygame.quit()
        sys.exit() 

    playerPos = nextmove(chessBoard, playerPos)
    draw_board(playerPos) 

    if all(all(row) for row in chessBoardVisited):  # If all squares visited
      print("Knight's tour completed!")
      break

    resetChessBoard(chessBoard)    #removing this removes numbers displaying
game_auto(8)