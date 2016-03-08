
import pygame
import sys
from pygame.locals import *
from random import randint
import time


class App:

    def __init__(self, n=10, dt=0, dx=20):
        self.n = n
        self.dt = dt
        self.grid = [[False for i in range(0, 2 * n)] for j in range(0, 2 * n)]
        self.reset_grid()

        self._running = True
        self.w = self.h = dx
        self.size = 2 * n * self.w + 100, 2 * n * self.h
        self.screen = pygame.display.set_mode(self.size)

        self.blackSquare = pygame.Surface((self.w, self.w))
        self.blackSquare.fill((50,50,50))
        self.WhiteSquare = pygame.Surface((self.w, self.w))
        self.blackSquare.fill((220,220,220))

        self.results = []

    def reset_display(self):
        for i in range(0, 2 * self.n):
            for j in range(0, 2 * self.n):
                self.draw_square(i, j)

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

    def draw_square(self, i, j):
        self.screen.blit(
            self.blackSquare if self.grid[i][j] else self.WhiteSquare,
            self.blackSquare.get_rect().move([i * self.w, j * self.w])
        )

    def random_flip(self):
        i = randint(0, 2 * self.n-1)
        j = randint(0, 2 * self.n-1)
        self.grid[i][j] = not self.grid[i][j]
        self.draw_square(i, j)

    def on_execute(self):
        pygame.init()

        self.reset_display()
        clock = pygame.time.Clock()
        start = pygame.time.get_ticks()
        while self._running:
            clock.tick(self.dt)
            self.random_flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    break
                if event.type == pygame.KEYUP:
                    if event.key == K_SPACE:
                        self.results.append(pygame.time.get_ticks() - start)
                        self.reset_grid()
                        self.reset_display()
                        start = pygame.time.get_ticks()
                    elif event.key == K_q:
                        self._running = False
                        break
            pygame.display.flip()

        for result in self.results:
            print result

        pygame.quit()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
