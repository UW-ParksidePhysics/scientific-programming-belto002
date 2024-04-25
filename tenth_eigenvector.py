import numpy as np
import matplotlib.pyplot as plt

matrix_dimension = 10

# Define a matrix H
H = np.diagflat(2 * np.ones(matrix_dimension) - np.diagflat(np.ones(matrix_dimension - 1), 1) - np.diagflat(np.ones(matrix_dimension - 1), -1)

# Compute the eigenvectors and eigenvalues of H
eigenvalues, eigenvectors = np.linalg.eig(H)

#sort eigenvaule and eigenvectors
x = eigenvalues.argsort()
eigenvalues = eigenvalues[x]
eigenvectors = eigenvectors[:, x]

#define x Values
x_values = np.linsspace(1/(matrix_dimension+1), matrix_dimension/(matrix_dimension+1), matrix_dimension)

#plot fifth eigenvector
plt.plot(eigenvectors[:, matrix_dimension-1], label="Tenth Eigenvector")

#labels
plt.xlabel('x')
plt.ylabel('value')
plt.legend()

#plot the sqrt 2 sin pix functuin
sin = np.sqrt(2) * np.sin(np.pi * x_values)
plt.plot(x_values, sin)

#show plot
plt.show()
