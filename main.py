import pygame
import sys
import random
import time
pygame.init()




def game(SQUARES_ACROSS):


  PIXELS_ACROSS = SQUARES_ACROSS * 16 #width and height in pixels, respectively
  SQUARE_SIZE = PIXELS_ACROSS // SQUARES_ACROSS #could use HEIGHT // SQUARES_ACROSS, if square board
  WHITE = pygame.Color("burlywood1")    #defines white macro
  BLACK = pygame.Color("chocolate4")    #define black as a macro 

  startPosX = random.randint(0, 7)                                  #initialises players position as a random place on board
  startPosY = random.randint(0, 7)
  playerPos = [startPosX, startPosY]


  chessBoard = [[0 for y in range(SQUARES_ACROSS)] for x in range(SQUARES_ACROSS)]

  screen = pygame.display.set_mode((PIXELS_ACROSS, PIXELS_ACROSS))
  pygame.display.set_caption("knights tour")
  
     
  def logic(chessBoard, playerPos):


    #gives coordinates of possible moves, and each one contains the number of moves available from that possible move.#
    knight_move_coords = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

        # playerPos[x1, y1] < 8: 
    for moveset in knight_move_coords: #runs through possible moves from playerPos
      possible_moves_count = 0;
      x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1] 
      if 0 <= x1 < SQUARES_ACROSS and 0 <= y1 < SQUARES_ACROSS:
        possible_move = [x1, y1] 


        for moveset in knight_move_coords: #counts outer moves from each possible move
          x2, y2 = possible_move[0] + moveset[0], possible_move[1] + moveset[1];  
          if 0 <= x2 < SQUARES_ACROSS and 0 <= y2 < SQUARES_ACROSS: 
            if x2 != playerPos[0] or y2 != playerPos[1]:
              possible_moves_count += 1  

          chessBoard[x1][y1] = possible_moves_count




     
  def draw_board(chessBoard, playerPos): 

    knight_image_big = pygame.image.load("knight.png") #import image of knight.png
    knight_image = pygame.transform.scale(knight_image_big, (SQUARE_SIZE, SQUARE_SIZE))
    font = pygame.font.Font(None, SQUARE_SIZE - 5)



    for x in range(SQUARES_ACROSS):          
        for y in range(SQUARES_ACROSS):         
            color = WHITE if (x + y) % 2 == 0 else BLACK       #white if even, black if odd
            pygame.draw.rect(
                screen,
                color,
                (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), #works cuz col and row start at 0
            )   #           x              y             width        




            
           #has the if statement to only print the knight where playerPos is.
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
    logic(chessBoard, playerPos)
    draw_board(chessBoard, playerPos) 











def game_auto(SQUARES_ACROSS):

  def resetChessBoard(array):
    for row in array:
      for i in range (len(row)):
        row[i] = 0

  PIXELS_ACROSS = SQUARES_ACROSS * 30 #width and height in pixels, respectively
  SQUARE_SIZE = PIXELS_ACROSS // SQUARES_ACROSS #could use HEIGHT // SQUARES_ACROSS, if square board

  startPosX = random.randint(0, 7)                #initialises players position as a random place on board
  startPosY = random.randint(0, 7)
  playerPos = [startPosX, startPosY]




  chessBoard = [[0 for y in range(SQUARES_ACROSS)] for x in range(SQUARES_ACROSS)]
  chessBoardVisited = [[0 for y in range(SQUARES_ACROSS)] for x in range(SQUARES_ACROSS)]


  screen = pygame.display.set_mode((PIXELS_ACROSS, PIXELS_ACROSS))
  pygame.display.set_caption("knights tour")


    






     
  def nextmove(chessBoard, playerPos):


    smallest_value = 7
    #smallest_value_position = [0,0]


    #gives coordinates of possible moves, and each one contains the number of moves available from that possible move.#
    knight_move_coords = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]


    #below function prints the numbers of possible moves on screen

    for moveset in knight_move_coords: #runs through possible moves from playerPos
      #possible_moves_count = 0;
      x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1] 
      if 0 <= x1 < SQUARES_ACROSS and 0 <= y1 < SQUARES_ACROSS:
        possible_move = [x1, y1] 
        possible_moves_count = 0;

        for moveset in knight_move_coords: #counts outer moves from each possible move
          x2, y2 = possible_move[0] + moveset[0], possible_move[1] + moveset[1];  
          if 0 <= x2 < SQUARES_ACROSS and 0 <= y2 < SQUARES_ACROSS: 
            if x2 != playerPos[0] or y2 != playerPos[1]:
              possible_moves_count += 1  

        chessBoard[x1][y1] = possible_moves_count #needs to be outside loop because it will keep changing the move count in ways you dont want because of the extra unneeded iterations



    #below finds the smallest of these possible moves and moves the players position to this square. 
          
          
    for moveset in knight_move_coords: #runs through possible moves from playerPos
      x1, y1 = playerPos[0] + moveset[0], playerPos[1] + moveset[1] 

      if 0 <= x1 < SQUARES_ACROSS and 0 <= y1 < SQUARES_ACROSS and chessBoardVisited[x1][y1] != 1: 

        possible_move = chessBoard[x1][y1]
          
        if smallest_value >= possible_move:
          smallest_value = possible_move
          smallest_value_position = [x1, y1]




    playerPos = smallest_value_position

    chessBoardVisited[playerPos[0]][playerPos[1]] = 1
    return playerPos
  

    












     
  def draw_board(playerPos): 
    font = pygame.font.Font(None, SQUARE_SIZE - 5)
    WHITE = pygame.Color("burlywood1")    #defines white macro
    BLACK = pygame.Color("chocolate4")    #define black as a macro 
    VISITEDCOLOUR = pygame.Color("aquamarine4")


    knight_image_big = pygame.image.load("knight.png") #import image of knight.png
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
                screen, color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), #works cuz col and row start at 0
            ) 

            
           #has the if statement to only print the knight where playerPos is.
            if playerPos[0] == x and playerPos[1] == y:
              screen.blit(knight_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))

            #draw number of possible moves onto screen
            if chessBoard[x][y] > 0:
              num = chessBoard[x][y]
              num_text = str(num)

              render_num = font.render(num_text, True, (0,0,0))
              screen.blit(render_num, ((x * SQUARE_SIZE) + SQUARE_SIZE / 2, (y * SQUARE_SIZE) + SQUARE_SIZE / 2))


    pygame.display.flip()







  has_run_once = False;


  while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:       
        pygame.quit()
        sys.exit() 
    draw_board(playerPos) 
    
    if (has_run_once == False):
      chessBoardVisited[startPosX][startPosY] = 1
      has_run_once = True

    playerPos = nextmove(chessBoard, playerPos)
    time.sleep(0)
    resetChessBoard(chessBoard)



  

def menu(SQUARES_ACROSS):
  import tkinter as tk
  from tkinter import simpledialog
  from tkinter import messagebox



  def option_message():
    message = simpledialog.askinteger("Input", "enter 1 to play game, 2 to see auto solve")

    if message == 1:
      game(SQUARES_ACROSS) 
    elif message == 2:
      game_auto(SQUARES_ACROSS)  
    else:
      messagebox.showwarning("Information", "please enter a valid integer")




  option_message()


#menu(8)
#game
game_auto(8)



