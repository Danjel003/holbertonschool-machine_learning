#!/usr/bin/env python3
"""
Task 13: Calculate descriptive statistics for all columns except Timestamp
"""

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')


def analyze(df):
    stats = df.drop(columns=['Timestamp']).describe()
    return status
