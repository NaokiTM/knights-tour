import pygame
from colours import *
pygame.init()

screen = pygame.display.set_mode((400, 300))

def draw_options():

    while True:
        screen.fill(LIGHT_GREY)

        font = pygame.font.Font(None, 50)

        text = font.render("Options", True, WHITE)
        screen.blit(text, (140, 50))

        back_button = pygame.Rect(120, 200, 160, 45)
        pygame.draw.rect(screen, DARK_GREY, back_button)

        button_text = font.render("Back", True, WHITE)
        button_rect = button_text.get_rect(center=back_button.center)
        screen.blit(button_text, button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    # returns and falls back to the draw_menu function. this prevents stack overflow. 
                    return

        pygame.display.flip()