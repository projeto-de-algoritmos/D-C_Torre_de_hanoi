import time
import pygame
import sys

MENU = 1


class Hanoi:
    def __init__(self, n_levels, base_width, level_height, interval, space_per_level):
        self.n_levels = n_levels
        self.base_width = base_width
        self.level_height = level_height
        self.interval = interval
        self.space_per_level = space_per_level

    def __hanoi(self, levels, start, target, n):
        if n == 1:
            levels[target].append(levels[start].pop())
            yield levels
        else:
            aux = 3 - start - target
            for i in self.__hanoi(levels, start, aux, n-1):
                yield i
            for i in self.__hanoi(levels, start, target, 1):
                yield i
            for i in self.__hanoi(levels, aux, target, n-1):
                yield i

    def __pyramid(self, levels, start_x, start_y, level_height, screen):
        for i, levelwidth in enumerate(levels):
            pygame.draw.rect(screen, (238-levelwidth, 100-levelwidth, 123-levelwidth), (start_x + (
                self.space_per_level - levelwidth)/2, start_y - level_height * i, levelwidth, level_height))

    def hanoi_display(self):
        levels = [
            [i * self.base_width for i in reversed(range(1, self.n_levels+1))], [], []]
        positions = self.__hanoi(levels, 0, 2, self.n_levels)

        pygame.init()
        screen = pygame.display.set_mode((500, 400))
        pygame.display.set_caption('Torre de Hanoi')

        while True:
            for position in positions:
                screen.fill((50, 50, 100))
                text = pygame.font.Font("src/assets/font.ttf",
                                        32).render("Torre de Hanoi", True, (238, 100, 123))
                rect = text.get_rect(center=(250, 65))
                text2 = pygame.font.Font("src/assets/font.ttf",
                                        15).render("Aperte B para retornar", True, (238, 100, 123))
                rect2 = text.get_rect(center=(310, 110))

                screen.blit(text, rect)
                screen.blit(text2, rect2)
                for i, pile in enumerate(position):
                    self.__pyramid(pile, 10 + self.space_per_level *
                                   i, 300, self.level_height, screen)
                pygame.display.update()
                time.sleep(self.interval)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        return MENU
