import pandas as pd
import numpy as np


def load_and_clean(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    
    # Perform initial cleaning
    data.dropna(inplace=True)  # Drop rows with missing values
    data['date'] = pd.to_datetime(data['date'])  # Convert date to datetime
    return data


def engineer_features(data):
    # Create additional features from existing data
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['day_of_week'] = data['date'].dt.dayofweek
    return data


def merge_weather_data(irrigation_data, weather_data):
    # Merge irrigation data with weather data based on date
    merged_data = pd.merge(irrigation_data, weather_data, on='date', how='left')
    return merged_data


def create_target_variable(data, target_column):
    # Create the target variable for modeling
    return data[target_column]


def prepare_training_data(data, features, target):
    # Prepare the final training data
    X = data[features]
    y = data[target]
    return X, y
