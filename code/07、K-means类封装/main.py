import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt


def calculate_distance(x, y):
    distance = np.linalg.norm(x - y)
    return distance


class KMeans:
    def __init__(self):
        self.data = None
        self.n_clusters = None
        self.max_iter = None

    def read_data(self, filename="./iris_data/iris.csv"):
        self.data = pd.read_csv(filename)

    def classify(self):
        X, Y = self.data.iloc[:, 1:-1], self.data.iloc[:, -1]
        clusters_center = X.sample(n=self.n_clusters).to_numpy()
        print(clusters_center)


if __name__ == '__main__':
    kmeans = KMeans()
    kmeans.n_clusters = 3
    kmeans.read_data()
    kmeans.classify()
