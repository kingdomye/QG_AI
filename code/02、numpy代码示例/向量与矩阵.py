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

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.eye(3)
matrix3 = np.eye(3, 4)
matrix4 = np.zeros((3, 4))
matrix5 = np.ones((3, 4))

matrixA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrixB = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
print(np.dot(matrixA, matrixB))
