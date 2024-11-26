#!/usr/bin/env python3
""" Write a function that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ A function that concatenates two matrices along a specific axis """
    if axis == 0:
        # check cols
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
        # return mat1.copy() + mat2.copy()

    elif axis == 1:
        # check rows
        if len(mat1) != len(mat2):
            return None
        result = []
        for i in range(len(mat1)):  # Loop over the number of rows
            result.append(mat1[i] + mat2[i])  # Concatenate each row pair
        return result
    else:
        return None
