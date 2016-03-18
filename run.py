from constant_switching import ConstantSwitchingApp
from random_switching import RandomSwitchingApp
from neighbour_switching import NeighbourSwitchingApp
from flipping import FlippingApp
from put_on_top import PutOnTopApp

apps = [
 [1, "Star graph transpositions", ConstantSwitchingApp],
 [2, "Linear graph transpositions", NeighbourSwitchingApp],
 [3, "Complete graph transpositions", RandomSwitchingApp],
 [4, "Random flipping", FlippingApp],
 [5, "Random put-on-top cycle", PutOnTopApp]
]
__name__ = "Mixing"

while True:
    for x, y, z in apps:
        print(x, y)
    x = int(raw_input())
    app = apps[x-1][2]()
    app.on_execute()
