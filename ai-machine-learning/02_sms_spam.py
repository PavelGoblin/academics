"""
SMS Spam Detection
===================
Goal: Detect spam messages (binary classification)
ML Task: Binary Text Classification
Algorithm: Naive Bayes + TF-IDF
"""

import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (classification_report, confusion_matrix,
                             accuracy_score, precision_score, recall_score)

# 1. Load Data
print("[1] Downloading dataset...")
path = kagglehub.dataset_download("uciml/sms-spam-collection-dataset")
df = pd.read_csv(f"{path}/spam.csv", encoding='latin-1')
print(f"Shape: {df.shape}")

# 2. Quick EDA
print("\n[2] Exploring data...")
# Keep only the first two columns (label, message)
df = df[['v1', 'v2']].rename(columns={'v1': 'label', 'v2': 'message'})
print(f"Label distribution:\n{df['label'].value_counts()}")
print(f"Spam ratio: {df['label'].value_counts(normalize=True)['spam']:.2%}")
print(f"Sample:\n{df.head(3)}")

# 3. Preprocessing
print("\n[3] Cleaning text...")

def clean_text(text):
    import re
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # keep letters + digits
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['clean'] = df['message'].apply(clean_text)

# 4. Feature Extraction
print("[4] TF-IDF vectorization...")
vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
X = vectorizer.fit_transform(df['clean']).toarray()

# Encode: ham=0, spam=1
y = df['label'].map({'ham': 0, 'spam': 1})

# 5. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

# 6. Train Model
print("\n[5] Training Naive Bayes (best for text!)...")
model = MultinomialNB()
model.fit(X_train, y_train)

# 7. Evaluate
y_pred = model.predict(X_test)
print(f"\n[6] Results:")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
print(f"\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred,
      target_names=['Ham', 'Spam'])}")

# 8. Test custom messages
print("\n[7] Testing custom messages:")
tests = ["Hey, want to grab coffee?", "CONGRATS! You won $1000 cash prize!!"]
for msg in tests:
    cleaned = clean_text(msg)
    vec = vectorizer.transform([cleaned]).toarray()
    prob = model.predict_proba(vec)[0]
    pred = model.predict(vec)[0]
    label = 'SPAM' if pred == 1 else 'HAM'
    print(f"  '{msg[:40]}...' -> {label} (spam prob: {prob[1]:.2%})")
