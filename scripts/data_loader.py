# scripts/data_loader.py
import pandas as pd

def load_data(path='data/student_exam_scores.csv'):
    """Load data from a CSV file"""
    df = pd.read_csv(path)
    return df