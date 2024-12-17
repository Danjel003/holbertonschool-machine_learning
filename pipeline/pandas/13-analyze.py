#!/usr/bin/env python3
"""
Task 13: Calculate descriptive statistics for all columns except Timestamp
"""
def analyze(df):
    """
    Analyze
    """
    # Drop the Timestamp column if it exists
    if 'Timestamp' in df.columns:
        df = df.drop(columns=['Timestamp'])
    
    # Compute descriptive statistics
    stats = df.describe()
    
    return stats
