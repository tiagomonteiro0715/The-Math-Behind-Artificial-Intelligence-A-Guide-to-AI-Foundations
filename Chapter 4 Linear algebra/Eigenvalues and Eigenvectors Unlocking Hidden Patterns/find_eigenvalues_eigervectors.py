import numpy as np

# Define matrix A
A = np.array([[2, 0],
              [0, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors (columns):")
print(eigenvectors)