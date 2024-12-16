#!/usr/bin/env python3


import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove the Weighted_Price column
df = df.drop(columns=['Weighted_Price'])

# Fill missing values
df['Close'].fillna(method='ffill', inplace=True)  # Set missing values in Close to the previous row's value
df[['High', 'Low', 'Open']] = df[['High', 'Low', 'Open']].fillna(df['Close'], axis=0)  # Set missing values in High, Low, Open to the same row’s Close value
df[['Volume_(BTC)', 'Volume_(Currency)']] = df[['Volume_(BTC)', 'Volume_(Currency)']].fillna(0)  # Set missing values in Volume_(BTC) and Volume_(Currency) to 0

print(df.head())
print(df.tail())
