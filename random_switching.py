from main import MixingApp
from random import randint

app = MixingApp(10, 0, 10, 20)

class RandomSwitchingApp(MixingApp):

    def __init__(self, *args):
        MixingApp.__init__(self, *args)

    def random_action(self):
        i = randint(0, 2 * self.n-1)
        j = randint(0, 2 * self.n-1)
        x = randint(0, 2 * self.n-1)
        y = randint(0, 2 * self.n-1)
        self.grid[i][j], self.grid[x][y] = self.grid[x][y], self.grid[i][j]
        self.draw_square(i, j)
        self.draw_square(x, y)

if __name__ == "__main__" :
    theApp = RandomSwitchingApp()
    theApp.on_execute()
