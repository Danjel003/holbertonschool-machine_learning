#!/usr/bin/env python3


from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data from the CSV file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove the Weighted_Price column
df = df.drop(columns=['Weighted_Price'])

# Rename the Timestamp column to Date
df = df.rename(columns={'Timestamp': 'Date'})

# Convert the Timestamp values to datetime
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# Set the DataFrame index to Date
df = df.set_index('Date')

# Fill missing values in Close with the previous row's value
df['Close'].fillna(method='ffill', inplace=True)

# Fill missing values in High, Low, Open with the same row's Close value
"""
# Fill missing values
df['Close'] = df['Close'].ffill()
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])
"""
df[['High', 'Low', 'Open']] = df[['High', 'Low', 'Open']].fillna(df['Close'])

# Fill missing values in Volume_(BTC) and Volume_(Currency) with 0
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

# Filter the DataFrame for data from 2017 onwards
df = df[df.index >= '2017-01-01']

# Group by date and aggregate the data
daily_data = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Plotting the data
plt.figure(figsize=(14, 7))
plt.plot(
    daily_data.index, daily_data['Close'],
    label='Close Price',
    color='blue')
plt.title('Daily Close Price of Bitcoin (2017 and Beyond)')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.legend()
plt.grid()
plt.show()
