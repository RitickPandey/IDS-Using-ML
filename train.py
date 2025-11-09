import argparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump
from utils import load_and_preprocess_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', required=True)
    parser.add_argument('--test', required=True)
    parser.add_argument('--model-output', required=True)
    args = parser.parse_args()

    X_train, y_train = load_and_preprocess_data(args.train)
    X_test, y_test = load_and_preprocess_data(args.test)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    dump(model, args.model_output)
    print(f"\n✅ Model saved at: {args.model_output}")
