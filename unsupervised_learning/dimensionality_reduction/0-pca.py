#!/usr/bin/env python3
import numpy as np

"""
This module implements Principal Component Analysis (PCA)
for dimensionality reduction.

The function `pca()` takes a dataset `X`,
and returns the weights matrix `W` that retains
the specified fraction of the variance.
"""


def pca(X, var=0.95):
    """
    Perform PCA on the dataset X and return the weights
    matrix W that maintains the specified fraction of the variance.

    Parameters:
    - X: numpy.ndarray of shape (n, d), where n is the number
    of data points and d is the number of features.
    - var: Fraction of variance to retain (default is 0.95).

    Returns:
    - W: numpy.ndarray of shape (d, nd), where nd is the number of
      principal components selected.
    """
    X_centered = X - np.mean(X, axis=0)

    covariance_matrix = np.cov(X_centered, rowvar=False)

    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues_sorted = eigenvalues[sorted_indices]
    eigenvectors_sorted = eigenvectors[:, sorted_indices]

    total_variance = np.sum(eigenvalues_sorted)
    variance_explained = np.cumsum(eigenvalues_sorted) / total_variance

    num_components = np.argmax(variance_explained >= var) + 1

    num_components = max(num_components, 1)

    W = eigenvectors_sorted[:, :num_components]

    return W
