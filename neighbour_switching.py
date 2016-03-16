from main import MixingApp
from random import randint

app = MixingApp(10, 0, 10, 20)

class NeighbourSwitchingApp(MixingApp):

    def __init__(self, *args):
        MixingApp.__init__(self, *args)

    def random_action(self):
        N = 2 * self.n-1
        position = randint(0, N * N - 1)
        i = position % N
        j = position // N
        if i == N -1:
            x = 0
            y = j + 1
        else:
            x = i + 1 % N
            y = j
        self.grid[i][j], self.grid[x][y] = self.grid[x][y], self.grid[i][j]
        self.draw_square(i, j)
        self.draw_square(x, y)

if __name__ == "__main__" :
    theApp = NeighbourSwitchingApp()
    theApp.on_execute()
