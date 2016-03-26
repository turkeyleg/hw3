import numpy as np

mat = np.array([[7, -4, -3, 0, 0],
                [-4, 6, -2, 0, 0],
                [-3, -2, 8, -1, -2],
                [0, 0, -1, 1, 0],
                [0, 0, -2, 0, 2]])

eigenvalues, eigenvectors = np.linalg.eig(mat)

second_smallest_eigenvalue, second_smallest_eigenvector = eigenvalues[1], eigenvectors[:,1]

print second_smallest_eigenvalue
print second_smallest_eigenvector

