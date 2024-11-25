#!/usr/bin/env python3
""" calculates the shape of a matrix: """


def matrix_shape(matrix):
    """ Function that calculates the shape of a matrix """

    result = []

    while (type(matrix) is list):
        result.append(len(matrix))
        matrix = matrix[0]
    return result
