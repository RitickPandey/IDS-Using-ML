import argparse
from joblib import load
from utils import load_and_preprocess_data
from sklearn.metrics import classification_report, confusion_matrix

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True)
    parser.add_argument('--test', required=True)
    args = parser.parse_args()

    model = load(args.model)
    X_test, y_test = load_and_preprocess_data(args.test)
    y_pred = model.predict(X_test)

    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
