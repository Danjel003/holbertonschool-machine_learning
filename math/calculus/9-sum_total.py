#!/usr/bin/env python3
"""Function to calculate """


def summation_i_squared(n):
    """Calculates the summation of i^2 from 1 to n using a formula"""

    if n < 1:
        return None

    return (n * (n + 1) * (2 * n + 1)) // 6
