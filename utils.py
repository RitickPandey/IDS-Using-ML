import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    if 'label' not in data.columns:
        raise ValueError("Dataset must include a 'label' column.")
    data['label'] = data['label'].apply(lambda x: 0 if x.strip().lower() == 'normal' else 1)
    X = data.drop('label', axis=1)
    y = data['label']
    return X, y
