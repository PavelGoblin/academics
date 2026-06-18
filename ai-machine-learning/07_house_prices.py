"""
House Price Prediction (Advanced Regression)
===============================================
Goal: Predict sale price of houses
ML Task: Regression
Algorithm: Gradient Boosting (XGBoost)
"""

import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor

# 1. Load Data
print("[1] Downloading dataset...")
path = kagglehub.competition_download("house-prices-advanced-regression-techniques")
train = pd.read_csv(f"{path}/train.csv")
test = pd.read_csv(f"{path}/test.csv")
print(f"Train: {train.shape}, Test: {test.shape}")

# 2. Quick EDA
print(f"\n[2] Exploring...")
print(f"Price stats:\n{train['SalePrice'].describe()}")
print(f"Missing columns (>50%): "
      f"{list(train.columns[train.isnull().mean() > 0.5])}")

# 3. Preprocessing
print("\n[3] Preprocessing features...")

def preprocess(df, is_train=True):
    data = df.copy()

    # Drop columns with too many missing values
    drop_cols = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu']
    data = data.drop([c for c in drop_cols if c in data.columns], axis=1)

    # Separate numeric and categorical
    num_cols = data.select_dtypes(include=[np.number]).columns
    cat_cols = data.select_dtypes(include=['object']).columns

    # Fill numeric with median
    for col in num_cols:
        if col != 'Id':
            data[col] = data[col].fillna(data[col].median())

    # Fill categorical with mode and encode
    for col in cat_cols:
        if col != 'Id':
            data[col] = data[col].fillna(data[col].mode()[0])
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col].astype(str))

    return data

# Preprocess both
train_proc = preprocess(train)
test_proc = preprocess(test)

# Align columns (drop cols in train not in test)
common_cols = [c for c in train_proc.columns if c in test_proc.columns]
X = train_proc[[c for c in common_cols if c != 'SalePrice']]
y = train['SalePrice']
X_test = test_proc[[c for c in common_cols if c != 'SalePrice']]

print(f"Features: {X.shape[1]}")

# 4. Log-transform the target (prices are skewed)
print("\n[4] Log-transforming target...")
y_log = np.log1p(y)  # log(1 + price) to handle skewness

# 5. Train/Test Split
X_tr, X_val, y_tr, y_val = train_test_split(
    X, y_log, test_size=0.2, random_state=42
)

# 6. Train Model
print("\n[5] Training Gradient Boosting...")
model = GradientBoostingRegressor(
    n_estimators=300, max_depth=4, learning_rate=0.05,
    min_samples_leaf=5, random_state=42
)
model.fit(X_tr, y_tr)

# 7. Evaluate (convert back from log)
y_val_pred = np.expm1(model.predict(X_val))
y_val_actual = np.expm1(y_val)
rmse = np.sqrt(mean_squared_error(y_val_actual, y_val_pred))

print(f"\n[6] Results:")
print(f"RMSE (dollars): ${rmse:.2f}")
print(f"RMSLE: {np.sqrt(mean_squared_error(y_val, model.predict(X_val))):.4f}")

# 8. Feature Importance
print("\n[7] Top 10 features:")
importances = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(importances.head(10).to_string(index=False))

# 9. Predict on test and save
print("\n[8] Predicting on test set...")
test_pred = np.expm1(model.predict(X_test))
submission = pd.DataFrame({
    'Id': test['Id'],
    'SalePrice': test_pred
})
submission.to_csv('07_house_prices_submission.csv', index=False)
print(f"  Saved to '07_house_prices_submission.csv'")
print(f"  Price range: ${test_pred.min():.0f} - ${test_pred.max():.0f}")
