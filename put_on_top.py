from main import MixingApp
from random import randint

app = MixingApp(10, 0, 10, 20)

class PutOnTopApp(MixingApp):

    def __init__(self, *args):
        MixingApp.__init__(self, *args)

    def random_action(self):
        N = 2 * self.n-1
        i = randint(0, N)
        j = randint(0, N)
        while i > 0 or j >= 0:
            x, y = self.before(i, j, N)
            if self.grid[i][j] != self.grid[x][y]:
                self.grid[i][j], self.grid[x][y] = self.grid[x][y], self.grid[i][j]
                self.draw_square(i, j)
                self.draw_square(x, y)
            i, j = x, y

    def before(self, i, j, N):
        if i == 0:
            return (N, j-1)
        else:
            return (i-1, j)


if __name__ == "__main__" :
    theApp = PutOnTopApp()
    theApp.on_execute()
