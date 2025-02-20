#!/usr/bin/env python3
""" PCA """
import numpy as np

def pca(X, var=0.95):
    """
    Perform PCA on the dataset X and return the weights matrix W that 
    maintains the specified variance fraction.

    Parameters:
    - X: numpy.ndarray of shape (n, d), where n is the number of data 
      points, and d is the number of features.
    - var: Fraction of variance to retain (default is 0.95).
    
    Returns:
    - W: numpy.ndarray of shape (d, nd), where nd is the number of 
      principal components selected.
    """
    # Step 1: Center the data (subtract the mean of each feature)
    X_centered = X - np.mean(X, axis=0)
    
    # Step 2: Compute the covariance matrix
    covariance_matrix = np.cov(X_centered, rowvar=False)
    
    # Step 3: Perform eigen decomposition on the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    
    # Step 4: Sort the eigenvalues and corresponding eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues_sorted = eigenvalues[sorted_indices]
    eigenvectors_sorted = eigenvectors[:, sorted_indices]
    
    # Step 5: Calculate the cumulative variance explained by the eigenvalues
    total_variance = np.sum(eigenvalues_sorted)
    variance_explained = np.cumsum(eigenvalues_sorted) / total_variance
    
    # Step 6: Select the number of components that explain the desired variance fraction
    num_components = np.argmax(variance_explained >= var) + 1
    
    # Ensure at least one component is selected (in case of very low variance explained)
    num_components = max(num_components, 1)
    
    # Step 7: The weights matrix W contains the eigenvectors corresponding to the top components
    W = eigenvectors_sorted[:, :num_components]
    
    return W
