import pygame
from hanoi import *
import sys

WIDTH = 500
HEIGHT = 400

RES = WIDTH, HEIGHT

MENU = 1
GAME = 2
OPTION = 3
CONTROL = 4


pygame.init()

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
pygame.display.set_caption("Menu")


def game():
    n_levels = 5
    base_width = 100//n_levels
    level_height = 150//n_levels
    space = WIDTH // 3

    hanoi = Hanoi(n_levels=n_levels, base_width=base_width, level_height=level_height, interval=0.10, space_per_level=space)
    if hanoi.hanoi_display() == 1:
        return MENU


def options():
    ...


def controls():
    ...


def menu():
    while True:
        screen.fill((50,50,100))
        text = pygame.font.Font("src/assets/font.ttf",
                                100).render("MENU", True, "#ffb500")
        rect = text.get_rect(center=(250, 100))
        text2 = pygame.font.Font(
            "src/assets/font.ttf", 20).render("Aperte A para comecar!", True, "#ffb500")
        rect2 = text.get_rect(center=(230, 250))
        text3 = pygame.font.Font(
            "src/assets/font.ttf", 20).render("Aperte O para opcoes", True, "#ffb500")
        rect3 = text.get_rect(center=(230, 300))
        text4 = pygame.font.Font(
            "src/assets/font.ttf", 20).render("Aperte Q para sair", True, "#ffb500")
        rect4 = text.get_rect(center=(230, 350))
        text5 = pygame.font.Font(
            "src/assets/font.ttf", 20).render("Aperte C para controles", True, "#ffb500")
        rect5 = text.get_rect(center=(230, 400))

        screen.blit(text, rect)
        screen.blit(text2, rect2)
        screen.blit(text3, rect3)
        screen.blit(text4, rect4)
        screen.blit(text5, rect5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game()
                elif event.key == pygame.K_o:
                    pass
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_c:
                    pass
        pygame.display.update()


def main():
    while True:
        if scene == MENU:
            scene = menu()
        elif scene == GAME:
            scene = game()
        elif scene == OPTION:
            scene = options()
        elif scene == CONTROL:
            scene == controls()


if __name__ == '__main__':
    menu()
