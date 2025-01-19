import numpy as np

vector = np.array([128, 128, 128])
vector1 = np.array([127, 127, 127], dtype=np.int8)
vector2 = np.array([255, 255, 255], dtype=np.uint32)

vector1_arrange = np.arange(10)
vector2_arrange = np.arange(1, 10, 0.5)
vector_linspace = np.linspace(0, 1, 10)
print(vector2_arrange)
