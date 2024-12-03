#!/usr/bin/env python3
""" defines a function that calculates the derivative of a polynomial """


def poly_derivative(poly):
    """ function to calculate derivative"""

    if type(poly) is not list or len(poly) < 1:
        return None
    for coefficient in poly:
        if type(coefficient) is not int and type(coefficient) is not float:
            return None
    for power, coefficient in enumerate(poly):
        if power == 0:
            derivative = [0]
            continue
        if power == 1:
            derivative = []
        derivative.append(power * coefficient)
    while derivative[-1] == 0 and len(derivative) > 1:
        derivative = derivative[:-1]
    return derivative
