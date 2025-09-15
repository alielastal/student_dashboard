# scripts/predictor.py
import pickle
import numpy as np

def load_model(model_path='model.pkl'):
    """Download the saved Model"""
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model, input_data):
    """Make predictions based on user input"""
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]