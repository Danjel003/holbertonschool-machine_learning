#!/usr/bin/env python3
"""Exponential class"""


class Exponential:
    """Class contructor"""
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha < 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data)/len(data))
