import pygame
from hanoi import *
import sys

WIDTH = 500
HEIGHT = 400

RES = WIDTH, HEIGHT

MENU = 1
GAME = 2
ABOUT = 3
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

    hanoi = Hanoi(n_levels=n_levels, base_width=base_width, level_height=level_height, interval=0.35, space_per_level=space)
    if hanoi.hanoi_display() == 1:
        return MENU


def about():
    while True:

        screen = pygame.display.set_mode((800, 600))
        screen.fill((50,50,100))
        text = pygame.font.Font("src/assets/font.ttf", 42).render("Torre de Hanoi", True, (238, 100, 123))
        rect = text.get_rect(center=(400,150))
        text2 = pygame.font.Font("src/assets/font.ttf", 18).render("A Torre de Hanoi é um jogo muito famoso", True, (238, 100, 123))
        rect2 = text.get_rect(center=(350, 230))
        text3 = pygame.font.Font("src/assets/font.ttf", 18).render("famoso ele consiste em três bases com", True, (238, 100, 123))
        rect3 = text.get_rect(center=(350, 280))
        text4 = pygame.font.Font("src/assets/font.ttf", 18).render("5 discos na esquerda e o objetivo é", True, (238, 100, 123))
        rect4 = text.get_rect(center=(350, 330))
        text5 = pygame.font.Font("src/assets/font.ttf", 18).render("passar todos os discos para direita ", True, (238, 100, 123))
        rect5 = text.get_rect(center=(350, 380))
        text6 = pygame.font.Font("src/assets/font.ttf", 18).render("em ordem crescente de diâmetro.", True, (238, 100, 123))
        rect6 = text.get_rect(center=(350, 430))
        text7 = pygame.font.Font("src/assets/font.ttf", 18).render("Nosso algoritmo é um resolvedor", True, (238, 100, 123))
        rect7 = text.get_rect(center=(350, 480))
        text8 = pygame.font.Font("src/assets/font.ttf", 18).render("da Torre de Hanoi em alguns passos.", True, (238, 100, 123))
        rect8 = text.get_rect(center=(350, 530))

        screen.blit(text, rect)
        screen.blit(text2, rect2)
        screen.blit(text3, rect3)
        screen.blit(text4, rect4)
        screen.blit(text5, rect5)
        screen.blit(text6, rect6)
        screen.blit(text7, rect7)
        screen.blit(text8, rect8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return MENU
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        pygame.display.flip()

def menu():
    while True:
        
        screen = pygame.display.set_mode((500, 400))
        screen.fill((50,50,100))
        text = pygame.font.Font("src/assets/font.ttf",
                                100).render("MENU", True, (238, 100, 123))
        rect = text.get_rect(center=(250, 100))
        text2 = pygame.font.Font(
            "src/assets/font.ttf", 20).render("Aperte A para comecar!", True, (238, 100, 123))
        rect2 = text.get_rect(center=(230, 250))
        text3 = pygame.font.Font(
            "src/assets/font.ttf", 20).render("Aperte O para sobre", True, (238, 100, 123))
        rect3 = text.get_rect(center=(230, 300))
        text4 = pygame.font.Font(
            "src/assets/font.ttf", 20).render("Aperte Q para sair", True, (238, 100, 123))
        rect4 = text.get_rect(center=(230, 350))

        screen.blit(text, rect)
        screen.blit(text2, rect2)
        screen.blit(text3, rect3)
        screen.blit(text4, rect4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game()
                elif event.key == pygame.K_o:
                    about()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def main():
    while True:
        if scene == MENU:
            scene = menu()
        elif scene == GAME:
            scene = game()
        elif scene == ABOUT:
            scene = about()


if __name__ == '__main__':
    menu()
