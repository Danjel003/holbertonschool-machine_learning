#!/usr/bin/env python3


import pandas as pd

def from_file(filename, delimiter):
    """Load data from a file as a pd.DataFrame."""
    return pd.read_csv(filename, delimiter=delimiter)