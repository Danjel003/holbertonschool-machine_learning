#!/usr/bin/env python3


import pandas as pd

def from_numpy(array):
    """Creates a DataFrame from a np.ndarray with columns labeled A-Z"""
    num_cols = array.shape[1]
    columns = [chr(i) for i in range(65, 65 + num_cols)]
    df = pd.DataFrame(array, columns=columns)
    return df
