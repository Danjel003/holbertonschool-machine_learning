#!/usr/bin/env python3
""" Derivative """

def poly_derivative(poly):
"""    Kontrolli nëse është një listë e vlefshme """
    if not isinstance(poly, list):
        return None

    """Nëse polinomi ka vetëm një element, derivati është 0 (për një konstante)"""
    if len(poly) <= 1:
        return [0]

    """ """
    return [poly[i] * i for i in range(1, len(poly))]
