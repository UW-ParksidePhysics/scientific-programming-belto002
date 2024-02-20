import numpy as np
matrix = np.array([[2,3], [7,11]]
                 )
print(matrix)
vector = np.array([5,13])
print(f'A = (matrix)')
determinant = np.linalg.det(matrix)
print(determinant)
print(f'det(A) = {determinant}')
inverse = np.linalg.inv(matrix)
print(f'A^-1 = {inverse}')




