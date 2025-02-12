import numpy as np
import matplotlib.pyplot as plt


class Moon:
    def __init__(self, r, w, d):
        self.r = r
        self.w = w
        self.d = d

    def moon(self, num):
        r1 = self.r - self.w / 2
        r2 = self.r + self.w / 2

        x1 = np.random.uniform(-r2, r2, num // 2)
        x2 = np.random.uniform(-r2, r2, num // 2)

        y1 = np.array([])
        for x in x1:
            low = 0 if abs(x) > r1 else np.sqrt(np.square(r1) - np.square(x))
            high = np.sqrt(np.square(r2) - np.square(x))
            y1 = np.append(y1, np.random.uniform(low, high))

        y2 = np.array([])
        for x in x2:
            low = 0 if abs(x) > r1 else np.sqrt(np.square(r1) - np.square(x))
            high = np.sqrt(np.square(r2) - np.square(x))
            low = -low - self.d
            high = -high - self.d
            y2 = np.append(y2, np.random.uniform(low, high))
        x2 += self.r

        # plt.title(f'r={self.r}, w={self.w}, d={self.d}')
        # plt.plot(x1, y1, 'ro')
        # plt.plot(x2, y2, 'bo')
        # plt.show()

        res1 = np.array([[x, y] for x, y in zip(x1, y1)])
        res2 = np.array([[x, y] for x, y in zip(x2, y2)])
        return res1, res2


if __name__ == "__main__":
    m = Moon(4, 2, 1)
    m.moon(800)
