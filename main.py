
import pygame
import sys
from pygame.locals import *
import math


class MixingApp:

    def __init__(self, n=15, dt=0, dx=15, precision=20):
        self.n = n
        self.m = 2 * n * 2 * n
        self.dt = dt
        self.grid = [[False for i in range(0, 2 * n)] for j in range(0, 2 * n)]

        pygame.init()

        plot_size = 600
        self.margin = 30
        self.epsilon = 3
        self.font = pygame.font.SysFont("arial", 15)

        self._running = True
        self.w = self.h = dx

        self.size = 2 * n * self.w + plot_size + 2 * self.margin, 2 * n * self.h

        self.screen = pygame.display.set_mode(self.size)

        self.blackSquare = pygame.Surface((self.w, self.w))
        self.blackSquare.fill((50,50,50))
        self.whiteSquare = pygame.Surface((self.w, self.w))
        self.whiteSquare.fill((220,220,220))

        self.other_rect = pygame.Rect(2 * n * self.w, 0, plot_size + 2 * self.margin, 2 * n * self.h)
        self.other_background = pygame.Surface(self.other_rect.size)
        self.other_background.fill((0,0,0))
        self.plot_rect = pygame.Rect(2 * n * self.w + self.margin, self.margin, plot_size, 2 * n * self.h - 2 * self.margin)
        self.plot_backgound = pygame.Surface(self.plot_rect.size)
        self.plot_backgound.fill((250,250,250))

        self.results = []
        self.precision = precision
        self.repartition = []

        self.reset_grid()

    def reset_display(self):
        for i in range(0, 2 * self.n):
            for j in range(0, 2 * self.n):
                self.draw_square(i, j)

        self.screen.blit(
            self.other_background,
            self.other_rect
        )
        self.screen.blit(
            self.plot_backgound,
            self.plot_rect
        )

        if self.results:
            left = self.plot_rect.left
            top = self.plot_rect.top
            width = self.plot_rect.width
            height = self.plot_rect.height

            nb_data = len(self.repartition)
            maximum = max(self.repartition)

            bar_size = width / nb_data

            for i in range(0, nb_data):
                self.draw_bar(
                    left + i * bar_size,
                    top + height,
                    bar_size,
                    self.repartition[i] * height / maximum,
                    (200,100,100)
                )
                self.screen.blit(
                    self.font.render(str(self.repartition[i]), 1, (255,255,255)),
                    (left + i * bar_size + self.epsilon, top + height - self.margin / 2 - self.epsilon)
                )
                self.screen.blit(
                    self.font.render(str(i * self.maximum / self.precision), 1, (255,255,255)),
                    (left + i * bar_size + self.epsilon, top + height + self.margin / 2 - self.epsilon)
                )

    def reset_grid(self):
        def is_middle(i, j):
            return (i >= self.n // 2 and
                    i < self.n * 3 // 2 and
                    j >= self.n // 2 and
                    j < self.n * 3 // 2)

        for i in range(0, 2 * self.n):
            for j in range(0, 2 * self.n):
                if is_middle(i, j):
                    self.grid[i][j] = True
                else:
                    self.grid[i][j] = False

        self.calculate_repartition()

    def calculate_repartition(self):
        if self.results:
            self.maximum = max(self.results)
            repartition = [0] * self.precision

            for result in self.results:
                repartition[(result * self.precision - 1) // self.maximum] += 1

            self.repartition = repartition
        else:
            self.repartition = []

    def draw_square(self, i, j):
        self.screen.blit(
            self.blackSquare if self.grid[i][j] else self.whiteSquare,
            self.blackSquare.get_rect().move([i * self.w, j * self.w])
        )

    def draw_bar(self, left, bottom, width, height, color):
        surface = pygame.Surface((width, height))
        surface.fill(color)
        rect = pygame.Rect(
            left,
            bottom - height,
            width,
            height
        )
        self.screen.blit(
            surface,
            rect
        )

    def random_action(self):
        pass

    def on_execute(self):
        self.reset_display()
        clock = pygame.time.Clock()
        counter = 0
        while self._running:
            clock.tick(self.dt)
            self.random_action()
            counter += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    break
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        self.results.append(counter)
                        counter = 0
                        self.reset_grid()
                        self.reset_display()
                    elif event.key == K_q:
                        self._running = False
                        break
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
