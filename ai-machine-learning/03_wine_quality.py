"""
Red Wine Quality Prediction
============================
Goal: Predict wine quality score (0-10)
ML Task: Regression + Classification
Algorithm: Random Forest
"""

import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import matplotlib.pyplot as plt

# 1. Load Data
print("[1] Downloading dataset...")
path = kagglehub.dataset_download("uciml/red-wine-quality-cortez-et-al-2009")
df = pd.read_csv(f"{path}/winequality-red.csv", sep=';')
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# 2. Quick EDA
print("\n[2] Exploring...")
print(f"Quality distribution:\n{df['quality'].value_counts().sort_index()}")
print(f"Stats:\n{df.describe()}")
print(f"Missing: {df.isnull().sum().sum()}")

# 3. Feature/Target split
X = df.drop('quality', axis=1)
y_reg = df['quality']                 # regression target (0-10)
y_clf = (df['quality'] >= 7).astype(int)  # classification: good=1, not=0

# 4. Train/Test Split
X_train, X_test, yr_train, yr_test = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)
_, _, yc_train, yc_test = train_test_split(
    X, y_clf, test_size=0.2, random_state=42
)

# 5. Train Models
print("\n[3] Training Random Forest Regressor...")
reg = RandomForestRegressor(n_estimators=200, random_state=42)
reg.fit(X_train, yr_train)

print("[4] Training Random Forest Classifier (Good/Bad)...")
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train, yc_train)

# 6. Evaluate Regression
yr_pred = reg.predict(X_test)
print(f"\n[5] Regression Results (predicting exact score):")
print(f"RMSE: {np.sqrt(mean_squared_error(yr_test, yr_pred)):.3f}")
print(f"R²:   {r2_score(yr_test, yr_pred):.3f}")

# 7. Evaluate Classification
yc_pred = clf.predict(X_test)
print(f"\n[6] Classification Results (Good [>=7] vs Bad):")
print(f"Accuracy: {accuracy_score(yc_test, yc_pred):.4f}")

# 8. Feature Importance
print("\n[7] Top 5 important features:")
importances = pd.DataFrame({
    'feature': X.columns,
    'importance': reg.feature_importances_
}).sort_values('importance', ascending=False)
print(importances.head(5).to_string(index=False))

# 9. Predict on a new sample
print("\n[8] Sample prediction:")
sample = X.iloc[0:1]
print(f"Actual quality: {y_reg.iloc[0]}")
print(f"Predicted quality: {reg.predict(sample)[0]:.2f}")
print(f"Good wine?: {'Yes' if clf.predict(sample)[0] == 1 else 'No'}")
