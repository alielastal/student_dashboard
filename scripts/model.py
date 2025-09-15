# scripts/model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
from data_loader import load_data
from data_cleaning import clean_data

def train_model(df, save_path='model.pkl'):
    """Build and store a linear regression model"""
    X = df[['hours_studied', 'sleep_hours', 'attendance_percent', 'previous_scores']]
    y = df['exam_score']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Saving Model
    with open(save_path, 'wb') as f:
        pickle.dump(model, f)
    
    return model

if __name__ == "__main__":
    print("🚀 Start uploading and training the model...")
    df = load_data()
    df = clean_data(df)
    train_model(df)