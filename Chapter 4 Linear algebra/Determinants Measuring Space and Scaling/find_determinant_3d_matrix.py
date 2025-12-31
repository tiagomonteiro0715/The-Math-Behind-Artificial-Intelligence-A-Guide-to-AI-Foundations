import numpy as np

# Define the matrix
B = np.array([
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
])

# Calculate the determinant
det_B = np.linalg.det(B)

print("Determinant of B:", det_B)