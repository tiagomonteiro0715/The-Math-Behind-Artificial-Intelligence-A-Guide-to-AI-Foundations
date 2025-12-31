import numpy as np
from scipy.linalg import solve

A = np.array([[3, 2, -1, 4, 5],
              [1, 1, 3, 2, -2],
              [4, -1, 2, 1, 0],
              [5, 3, -2, 1, 1],
              [2, -3, 1, 3, 4]])

b = np.array([12, 5, 7, 9, 10])

solution = solve(A, b)

print(solution)