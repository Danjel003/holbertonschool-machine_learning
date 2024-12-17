#!/usr/bin/env python3
"""
Task 13: Analyze
"""
import pandas as pd


def analyze(df):
    # Calculate descriptive statistics for all columns except Timestamp
    stats = df.drop(columns=['Timestamp']).describe()
    return status
