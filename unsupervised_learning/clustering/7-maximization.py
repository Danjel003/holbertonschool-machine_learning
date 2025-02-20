#!/usr/bin/env python3
""" 0x01. Clustering """
import numpy as np


def maximization(X, g):
    """calculates the maximization step in the EM algorithm for a GMM"""
    if not isinstance(X, np.ndarray) or len(X.shape) != 2\
            or not isinstance(g, np.ndarray) or len(g.shape) != 2\
            or X.shape[0] != g.shape[1]:
        return None, None, None

    n, d = X.shape
    k = g.shape[0]

    probs = np.sum(g, axis=0)
    validation = np.ones((n,))
    if not np.isclose(probs, validation).all():
        return None, None, None

    pi = np.zeros((k,))
    m = np.zeros((k, d))
    S = np.zeros((k, d, d))

    for i in range(k):
        pi[i] = np.sum(g[i]) / n
        m[i] = np.matmul(g[i], X) / np.sum(g[i])
        S[i] = np.matmul(g[i] * (X - m[i]).T, X - m[i]) / np.sum(g[i])

    return pi, m, S
