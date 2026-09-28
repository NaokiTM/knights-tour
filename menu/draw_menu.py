import pygame
from colours import *
pygame.init()
from menu.draw_options import draw_options
from game import game_auto

screen = pygame.display.set_mode((400, 300))

def draw_menu():
    font = pygame.font.Font(None, 50)

    # define menu rect
    menu = pygame.Rect(0, 0, 400, 300)
    menu.center = screen.get_rect().center

    # define button rect
    start_button = pygame.Rect(0, 0, 160, 45)
    start_button.center = (menu.centerx, menu.centery + 50)

    #define option button rect
    option_button = pygame.Rect(0, 0, 160, 45)
    option_button.center = (menu.centerx, menu.centery + 100)


    while True:
        screen.fill(LIGHT_GREY)
        pygame.draw.rect(screen, DARK_GREY, menu)

        # render text
        font = pygame.font.Font(None, 50)
        text = font.render("Knight's Tour", True, WHITE)
        screen.blit(text, (100, 100))

        # option button
        pygame.draw.rect(screen, (100, 100, 100), option_button)
        button_text = font.render("Options", True, WHITE)
        button_text_rect = button_text.get_rect(center=option_button.center)
        screen.blit(button_text, button_text_rect)

        # start Button
        pygame.draw.rect(screen, (100, 100, 100), start_button)
        button_text = font.render("Start", True, WHITE)
        button_text_rect = button_text.get_rect(center=start_button.center)
        screen.blit(button_text, button_text_rect)

        # handle menu input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              return

            if event.type == pygame.MOUSEBUTTONDOWN:
              if start_button.collidepoint(event.pos):
                  game_auto(8)
                  return
              if option_button.collidepoint(event.pos):
                  draw_options()

        pygame.display.flip()