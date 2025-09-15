# scripts/data_cleaning.py
import pandas as pd

def clean_data(df):
    """Cleanse data from missing or illogical values"""
    # Delete rows that contain missing values
    df = df.dropna()
    
    # Ensure that all numeric columns are numbers
    numeric_cols = ['hours_studied', 'sleep_hours', 'attendance_percent', 'previous_scores', 'exam_score']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    # Re-delete any missing values ​​after conversion
    df = df.dropna()
    
    return df