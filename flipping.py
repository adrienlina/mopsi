from main import MixingApp
from random import randint

app = MixingApp(10, 0, 10, 20)

class FlippingApp(MixingApp):

    def __init__(self, *args):
        MixingApp.__init__(self, *args)

    def random_action(self):
        i = randint(0, 2 * self.n-1)
        j = randint(0, 2 * self.n-1)
        self.grid[i][j] = not self.grid[i][j]
        self.draw_square(i, j)

if __name__ == "__main__" :
    theApp = FlippingApp()
    theApp.on_execute()
