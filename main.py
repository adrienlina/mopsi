
import pygame
import sys
from pygame.locals import *
from random import randint

class App:

    def __init__(self, n=20, dt=0, dx=10):
        self.n = n
        self.dt = dt
        self.grid = [[False for i in range(0, 2 * n)] for j in range(0, 2 * n)]
        self.reset_grid()

        self.w = self.h = dx
        self.size = self.weight, self.height = 2 * n * self.w, 2 * n * self.h
        self.screen = pygame.display.set_mode(self.size)

        self.blackSquare = pygame.Surface((self.w, self.w))
        self.blackSquare.fill((50,50,50))
        self.WhiteSquare = pygame.Surface((self.w, self.w))
        self.blackSquare.fill((220,220,220))

    def reset_display(self):
        for i in range(0, 2 * self.n):
            for j in range(0, 2 * self.n):
                self.draw_square(i, j)
        self._running = True

    def reset_grid(self):
        for i in range(self.n // 2, 3 * self.n // 2):
            for j in range(self.n // 2, 3 * self.n // 2):
                print i,j
                self.grid[i][j] = True


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
        while self._running:
            clock.tick(self.dt)
            self.random_flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
