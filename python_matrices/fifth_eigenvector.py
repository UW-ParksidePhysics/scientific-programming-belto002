import numpy as np
import matplotlib.pyplot as plt

# Create the matrix H
diag = np.diagflat([-1, 2, -1], -1) + np.diagflat([2, 2, 2, 2, 2]) + np.diagflat([-1, -1, -1], 1)
H = 1 / (2 * (1 / (5 + 1)) ** 2) * diag

# Find eigenvalues and eigenvectors of H
eigenvalues, eigenvectors = np.linalg.eig(H)

# Find the fifth eigenvector
fifth_eigenvector = eigenvectors[:, 4]

# Create x values
x_values = np.linspace(1 / (5 + 1), 5 / (5 + 1), 5)

# Plot the fifth eigenvector and sqrt(2) * sin(pi*x)
plt.plot(x_values, fifth_eigenvector, label='Fifth Eigenvector')
plt.plot(x_values, np.sqrt(2) * np.sin(np.pi * x_values), label=r'$\sqrt{2} \sin(\pi x)$')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Values')
plt.legend()
plt.title('Plot of Fifth Eigenvector and $\\sqrt{2} \\sin(\\pi x)$')

# Show plot
plt.show()
