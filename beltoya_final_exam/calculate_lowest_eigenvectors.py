import numpy as np


def calculate_lowest_eigenvectors(matrix, num_eigenvectors=3):
    """
    Identify the eigenvectors with the smallest eigenvalues given an input matrix.

    Parameters:
        matrix (ndarray): Square matrix to be characterized. Must be a square matrix of M rows and M columns
            where M is greater than or equal to 1.
        num_eigenvectors (int, optional): Number of eigenvectors with eigenvalues to return.
            Default is 3.

    Returns:
        ndarray: Array of the K lowest-value eigenvalues ordered from lowest to highest.
        ndarray: Array of K eigenvectors with M components arranged in order corresponding to their eigenvalues.
            The first index corresponds to the eigenvalue index in the eigenvalues array. The order of the components
            in the eigenvector remains the same as output by NumPy's eig.

                 __author__ = Jackson
    """
    eigvals, eigvecs = np.linalg.eig(matrix)
    sorted_indices = np.argsort(eigvals)
    lowest_eigenvalues = eigvals[sorted_indices][:num_eigenvectors]
    lowest_eigenvectors = eigvecs[:, sorted_indices][:, :num_eigenvectors]

    return lowest_eigenvalues, lowest_eigenvectors


if __name__ == "__main__":
    # Test the module
    square_matrix = np.array([[2, -1], [-1, 2]])
    number_of_eigenvectors = 2
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:")
    print(eigenvectors)
