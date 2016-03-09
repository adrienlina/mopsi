import numpy as np
import matplotlib.pyplot as plt



class ResultBarPlot:

    def __init__(self, precision=10):
        self.results = [123,234,345,345,234,345,123,234,345,345]
        self.precision = precision

    def plot(self):
        repartition, axis = self.calculate_repartition()

        fig, axes = plt.subplots()
        axes.bar(np.arange(len(repartition)), repartition, 1)
        axes.bar(np.arange(len(repartition)), [0.00000001]*len(repartition), 1)
        axes.set_xticklabels(axis)

        plt.show()

    def calculate_repartition(self):
        maximum = max(self.results)
        print(maximum)
        repartition = [0] * self.precision

        for result in self.results:
            repartition[result * self.precision // maximum - 1] += 1

        axis = [i * maximum / 5 for i in range(0, 6)]

        return repartition, axis

    def add_value(self, value):
        self.results.append(value)

if __name__ == "__main__" :
    barplot = ResultBarPlot()
    barplot.plot()
