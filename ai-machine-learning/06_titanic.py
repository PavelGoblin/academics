"""
Titanic - Predict Survival
============================
Goal: Predict which passengers survived the Titanic
ML Task: Binary Classification
Algorithm: Random Forest + Feature Engineering
"""

import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import re

# 1. Load Data
print("[1] Downloading dataset...")
path = kagglehub.competition_download("titanic")
train = pd.read_csv(f"{path}/train.csv")
test = pd.read_csv(f"{path}/test.csv")
print(f"Train: {train.shape}, Test: {test.shape}")

# 2. Quick EDA
print(f"\n[2] Exploring training data...")
print(f"Survival distribution:\n{train['Survived'].value_counts()}")
print(f"Missing values:\n{train.isnull().sum()[train.isnull().sum() > 0]}")

# 3. Feature Engineering (the key to Titanic!)
def engineer_features(df):
    data = df.copy()

    # Title from Name (e.g., Mr, Mrs, Miss)
    data['Title'] = data['Name'].apply(
        lambda x: re.search(r' ([A-Za-z]+)\.', x).group(1) if re.search(r' ([A-Za-z]+)\.', x) else 'Other'
    )
    title_map = {'Mr': 1, 'Mrs': 2, 'Miss': 3, 'Master': 4, 'Dr': 5}
    data['Title'] = data['Title'].map(title_map).fillna(0).astype(int)

    # Family size
    data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
    data['IsAlone'] = (data['FamilySize'] == 1).astype(int)

    # Age fill with median
    data['Age'] = data['Age'].fillna(data['Age'].median())

    # Fare fill with median
    data['Fare'] = data['Fare'].fillna(data['Fare'].median())

    # Embarked fill with mode
    data['Embarked'] = data['Embarked'].fillna('S')
    data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

    # Sex: male=0, female=1
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

    # Cabin: has cabin or not
    data['HasCabin'] = data['Cabin'].notna().astype(int)

    # Select features
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare',
                'Embarked', 'Title', 'FamilySize', 'IsAlone', 'HasCabin']
    return data[features]

print("\n[3] Engineering features...")
X_train = engineer_features(train)
y_train = train['Survived']
X_test = engineer_features(test)

print(f"Features: {list(X_train.columns)}")

# 4. Train/Validation Split
X_tr, X_val, y_tr, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=42
)

# 5. Train Model with Hyperparameter Tuning
print("\n[4] Training Random Forest with tuning...")
params = {'n_estimators': [100, 200], 'max_depth': [5, 10, None]}
grid = GridSearchCV(RandomForestClassifier(random_state=42),
                    params, cv=5, scoring='accuracy')
grid.fit(X_tr, y_tr)
model = grid.best_estimator_
print(f"Best params: {grid.best_params_}")
print(f"Best CV score: {grid.best_score_:.4f}")

# 6. Validate
y_pred = model.predict(X_val)
print(f"\n[5] Validation Results:")
print(f"Accuracy: {accuracy_score(y_val, y_pred):.4f}")
print(f"\nClassification Report:\n{classification_report(y_val, y_pred)}")

# 7. Feature Importance
print("\n[6] Feature Importance:")
importances = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(importances.to_string(index=False))

# 8. Predict on test and save
print("\n[7] Predicting on test set...")
test_pred = model.predict(X_test)
submission = pd.DataFrame({
    'PassengerId': test['PassengerId'],
    'Survived': test_pred
})
submission.to_csv('06_titanic_submission.csv', index=False)
print("  Saved to '06_titanic_submission.csv'")
print(f"  Predicted survivors: {test_pred.sum()}/{len(test_pred)}")
