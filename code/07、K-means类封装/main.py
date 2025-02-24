import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt


def calculate_distance(x, y):
    distance = np.linalg.norm(x - y)
    return distance


class KMeans:
    def __init__(self, n_clusters=3):
        self.data = None
        self.n_clusters = n_clusters
        self.max_iter = None
        self.X = None
        self.Y = None

    def read_data(self, filename="./iris_data/iris.csv"):
        self.data = pd.read_csv(filename)
        self.X, self.Y = self.data.iloc[:, 1: -1], self.data.iloc[:, -1]
        self.X = self.X.values

    def get_clusters(self, clusters_center):
        distances = np.linalg.norm(self.X[:, np.newaxis] - clusters_center, axis=2)
        new_clusters = np.argmin(distances, axis=1)
        return new_clusters

    def classify(self):
        clusters_center = np.array(random.sample(self.X.tolist(), self.n_clusters))
        new_clusters = self.get_clusters(clusters_center)
        print(new_clusters)

    def test(self):
        print(self.X[:, np.newaxis])


if __name__ == '__main__':
    kmeans = KMeans()
    kmeans.read_data()
    # kmeans.test()
    kmeans.classify()
