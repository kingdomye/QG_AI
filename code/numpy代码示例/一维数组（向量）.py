import numpy as np

vector = np.array([128, 128, 128])
vector1 = np.array([127, 127, 127], dtype=np.int8)
vector2 = np.array([255, 255, 255], dtype=np.uint32)

vector1_arrange = np.arange(10)
vector2_arrange = np.arange(1, 10, 0.5)
vector_linspace = np.linspace(0, 1, 10)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.dot(a, b)
print(c)
