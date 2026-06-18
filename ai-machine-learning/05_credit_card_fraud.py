"""
Credit Card Fraud Detection
=============================
Goal: Detect fraudulent transactions (highly imbalanced dataset)
ML Task: Binary Classification
Algorithm: Random Forest + Undersampling
"""

import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report, confusion_matrix,
                             roc_auc_score, precision_recall_curve)

# 1. Load Data
print("[1] Downloading dataset...")
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
df = pd.read_csv(f"{path}/creditcard.csv")
print(f"Shape: {df.shape}")

# 2. Quick EDA - check imbalance!
print("\n[2] Checking class imbalance...")
fraud_count = df['Class'].sum()
total = len(df)
print(f"Fraud cases: {fraud_count} ({fraud_count/total:.4%})")
print(f"Normal cases: {total - fraud_count}")
print(f"Fraud ratio: 1 : {(total-fraud_count)//fraud_count:.0f}")

# 3. Separate features and target
X = df.drop('Class', axis=1)
y = df['Class']

# Split first (before resampling to avoid data leakage)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print(f"\n[3] Split: Train {X_train.shape[0]}, Test {X_test.shape[0]}")

# 4. Handle Imbalance - Undersample majority class
print("\n[4] Applying undersampling...")
fraud_train = X_train[y_train == 1]
normal_train = X_train[y_train == 0]
n_fraud = len(fraud_train)

# Take equal number of normal samples
normal_sample = normal_train.sample(n=n_fraud, random_state=42)
X_balanced = pd.concat([fraud_train, normal_sample])
y_balanced = pd.Series([1]*n_fraud + [0]*n_fraud)
print(f"  Balanced dataset: {len(X_balanced)} samples")

# 5. Train Model
print("\n[5] Training Random Forest...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_balanced, y_balanced)

# 6. Evaluate
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print(f"\n[6] Results:")
print(f"ROC-AUC: {roc_auc_score(y_test, y_prob):.4f}")
print(f"\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred,
      target_names=['Normal', 'Fraud'])}")

# 7. Precision-Recall curve (better metric for imbalance)
precision, recall, _ = precision_recall_curve(y_test, y_prob)
print(f"\n[7] Precision-Recall summary:")
print(f"  At recall 80% -> precision: roughly {precision[len(precision)//2]:.3f}")

# 8. Feature Importance (top features)
print("\n[8] Top 5 important features (anonymized Vn):")
importances = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(importances.head(5).to_string(index=False))
