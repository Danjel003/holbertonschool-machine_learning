#!/usr/bin/env python3
import numpy as np

"""
This module implements Principal Component Analysis
(PCA) for dimensionality reduction.

The function `pca()` reduces the dimensionality of
the dataset `X` to the specified
number of dimensions `ndim`.
"""


def pca(X, ndim):
    """
    Perform PCA on the dataset X and return
    the transformed data with the specified number
    of dimensions.

    Parameters:
    - X: numpy.ndarray of shape (n, d),
    where n is the number of data points and
      d is the number of features.
    - ndim: Number of dimensions to retain after PCA transformation.

    Returns:
    - T: numpy.ndarray of shape (n, ndim),
    the transformed version of X with reduced dimensions.
    """
    # Center the data by subtracting the mean of each feature
    X_centered = X - np.mean(X, axis=0)

    # Compute the covariance matrix of the centered data
    covariance_matrix = np.cov(X_centered, rowvar=False)

    # Compute the eigenvalues and eigenvectors of the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    # Sort the eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues_sorted = eigenvalues[sorted_indices]
    eigenvectors_sorted = eigenvectors[:, sorted_indices]

    # Ensure the signs of the eigenvectors are consistent with the desired output
    for i in range(eigenvectors_sorted.shape[1]):
        if eigenvectors_sorted[0, i] < 0:
            eigenvectors_sorted[:, i] = -eigenvectors_sorted[:, i]

    # Select the top 'ndim' eigenvectors to form the projection matrix
    W = eigenvectors_sorted[:, :ndim]

    # Project the data onto the new lower-dimensional space
    T = np.dot(X_centered, W)

    return T
