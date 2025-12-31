import numpy as np

# Define the matrix
A = np.array([
    [2, 3],
    [1, 4]
])

# Calculate the determinant
det_A = np.linalg.det(A)

print("Determinant of A:", det_A)