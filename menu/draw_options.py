import pygame
from colours import *
pygame.init()

screen = pygame.display.set_mode((400, 300))
BOARD_SIZES = [6, 8, 10, 12]

def draw_options(selected_size):
    left_button = pygame.Rect(80, 100, 40, 45)
    right_button = pygame.Rect(280, 100, 40, 45)

    while True:
        screen.fill(LIGHT_GREY)

        font = pygame.font.Font(None, 50)

        text = font.render("Options", True, WHITE)
        screen.blit(text, (140, 50))

        back_button = pygame.Rect(120, 200, 160, 45)
        pygame.draw.rect(screen, DARK_GREY, back_button)

        # no. of squares cycler
        pygame.draw.rect(screen, DARK_GREY, left_button)
        pygame.draw.rect(screen, DARK_GREY, right_button)

        left_text = font.render("<", True, WHITE)
        right_text = font.render(">", True, WHITE)

        # left button text 
        screen.blit(left_text, left_text.get_rect(center=left_button.center))

        # display board sizes 
        size_text = font.render(str(selected_size) + " x " + str(selected_size), True, WHITE)
        size_rect = size_text.get_rect(center=(200, 122))
        screen.blit(size_text, size_rect)

        # right button text 
        screen.blit(right_text, right_text.get_rect(center=right_button.center))

        # back button
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
                    # also returns selected size 
                    return selected_size
                if left_button.collidepoint(event.pos):
                    index = BOARD_SIZES.index(selected_size)
                    selected_size = BOARD_SIZES[(index - 1) % len(BOARD_SIZES)]

                if right_button.collidepoint(event.pos):
                    index = BOARD_SIZES.index(selected_size)
                    selected_size = BOARD_SIZES[(index + 1) % len(BOARD_SIZES)]

        pygame.display.flip()