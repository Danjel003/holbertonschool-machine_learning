#!/usr/bin/env python3
"""
Task 11: Concat
"""


def concat(df1, df2):
    """ Concat"""
    df1.set_index('Timestamp', inplace=True)
    df2.set_index('Timestamp', inplace=True)

    # Filter df2 to only include timestamps up to and including 1417411920
    df2 = df2.loc[:1417411920]

    # Concatenate the DataFrames
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])

    return df
