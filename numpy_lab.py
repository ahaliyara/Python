import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3])

# Basic math operations
print(arr + 2)           # [3 4 5]
print(np.mean(arr))      # 2.0

# 2D array (matrix)
matrix = np.array([[1, 2], [3, 4]])

# Transpose
print(matrix.T)

# Dot product
print(np.dot(matrix, matrix))
