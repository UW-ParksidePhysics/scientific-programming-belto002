import numpy as np
import matplotlib.pyplot as plt

elements = [[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0,0, -1, 2]]
diag_elements np.diagflat(elements)

#define the scalar
scalar = 1 / (2 * ((1 / (5+1) ** 2)))

#multiply diagonal matrix by the scalar
H = scalar * diag_elements

print(H)

#Define a matrix H
H = np.array([[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]])

# Compute the eigenvectors and eigenvalues of H
eigenvalues, eigenvectors = np.linalg.eig(H)

#sort eigenvaule and eigenvectors
x = eigenvalues.argsort()
eigenvalues = eigenvalues[x]
eigenvectors = eigenvectors[:, x]

#define x Values
x_values = np.linsspace(1/(5+1), 5/(5+1), 5)

#plot fifth eigenvector
plt.plot(eigenvectors[:, 4], label="Fifth Eigenvector")

#labels
plt.xlabel('x')
plt.ylabel('value')
plt.legend()

#plot the sqrt 2 sin pix functuin
sin = np.sqrt(2) * np.sin(np.pi * x_values)
plt.plot(x_values, sin)

#show plot
plt.show()
