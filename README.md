# Intrusion Detection System using Machine Learning

This is a simple demonstration project for **Intrusion Detection in Computer Networks using Machine Learning**.

## 🧠 Overview
This project implements a Random Forest classifier to detect abnormal network traffic patterns.
It uses standard CSV datasets like NSL-KDD or KDDCup99.

## ⚙️ Files
- `train.py` → Train model using dataset
- `evaluate.py` → Evaluate model performance
- `utils.py` → Data loading and preprocessing
- `requirements.txt` → Required dependencies
- `data/` → Folder for training & testing CSV files
- `models/` → Folder for storing trained models

## 🚀 How to Run
```bash
# 1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # For Windows

# 2️⃣ Install Dependencies
pip install -r requirements.txt

# 3️⃣ Train Model
python train.py --train data/train.csv --test data/test.csv --model-output models/rf-id-model.joblib

# 4️⃣ Evaluate Model
python evaluate.py --model models/rf-id-model.joblib --test data/test.csv
```

## 📊 Output
- Prints accuracy, precision, recall, and F1-score.
- Displays confusion matrix.
- Saves trained model in `models/` folder.

## 🧾 Author
**Ritick Pandey**
Assignment Project — Intrusion Detection System using Machine Learning
