#!/usr/bin/env python3
""" Derivative """


def poly_derivative(poly):
    if not isinstance(poly, list):
        return None
    """Nëse polinomi është një konstante, derivati është 0"""
    if len(poly) <= 1:
        return [0]

    """ Llogaritja e derivatit duke përdorur një listë të re"""
    return [i * poly[i] for i in range(1, len(poly))]
