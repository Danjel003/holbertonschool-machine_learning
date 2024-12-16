#!/usr/bin/env python3


import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data from the CSV files
df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Filter the DataFrames for the specified timestamps
df1_filtered = df1[(df1.index >= 1417411980) & (df1.index <= 1417417980)]
df2_filtered = df2[(df2.index >= 1417411980) & (df2.index <= 1417417980)]

# Concatenate the DataFrames and add keys
df = pd.concat([df2_filtered, df1_filtered], keys=['bitstamp', 'coinbase'])

# Reorganize the MultiIndex to have timestamp as the first level
df.index = df.index.reorder_levels(['Timestamp', 'key'])

# Sort the DataFrame by index (which now includes timestamp first)
df = df.sort_index(level='Timestamp')

# Display the resulting DataFrame
print(df)
