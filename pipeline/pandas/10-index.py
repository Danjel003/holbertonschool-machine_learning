#!/usr/bin/env python3
"""
Task 10: Indexing
"""


def index(df):
    """Indexing"""
    df.set_index('Timestamp', inplace=True)
    return df
