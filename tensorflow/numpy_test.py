import numpy as np

vector = np.array([1, 2, 3])
print(vector.shape, vector.ndim)

matrix = np.array([[1, 2],
                   [3, 4]])
print(matrix.shape, matrix.ndim)

one = np.arange(12)
print(one, "\n", one.reshape(3, 4))

zero = np.zeros((3, 4))
print(zero)
