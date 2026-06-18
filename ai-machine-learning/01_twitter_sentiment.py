"""
Twitter US Airline Sentiment Analysis
======================================
Goal: Classify tweets as positive, neutral, or negative
ML Task: Multi-class Text Classification
Algorithm: Logistic Regression + TF-IDF
"""

import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Load Data from Kaggle
print("[1] Downloading dataset...")
path = kagglehub.dataset_download("crowdflower/twitter-airline-sentiment")
df = pd.read_csv(f"{path}/Tweets.csv")
print(f"Shape: {df.shape}")

# 2. Quick EDA
print("\n[2] Exploring data...")
print(f"Sentiment distribution:\n{df['airline_sentiment'].value_counts()}")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Sample text:\n{df['text'].head(3)}")

# 3. Preprocessing
print("\n[3] Preprocessing text...")

def clean_text(text):
    import re
    text = text.lower()
    text = re.sub(r'http\S+', '', text)      # remove URLs
    text = re.sub(r'@\w+', '', text)          # remove mentions
    text = re.sub(r'[^a-z\s]', '', text)      # keep only letters
    text = re.sub(r'\s+', ' ', text).strip()  # collapse spaces
    return text

df['clean_text'] = df['text'].apply(clean_text)

# 4. Feature Extraction (TF-IDF)
print("\n[4] Converting text to features (TF-IDF)...")
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X = vectorizer.fit_transform(df['clean_text']).toarray()

# Encode labels: negative=0, neutral=1, positive=2
y = df['airline_sentiment'].map({'negative': 0, 'neutral': 1, 'positive': 2})

# 5. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

# 6. Train Model
print("\n[5] Training Logistic Regression...")
model = LogisticRegression(max_iter=1000, multi_class='multinomial')
model.fit(X_train, y_train)

# 7. Evaluate
y_pred = model.predict(X_test)
print(f"\n[6] Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred,
      target_names=['Negative', 'Neutral', 'Positive'])}")

# 8. Test with custom tweets
print("\n[7] Testing custom tweets:")
test_tweets = [
    "Great flight, amazing service!",
    "Worst experience ever, delayed 5 hours",
    "The flight was okay, nothing special"
]
for tweet in test_tweets:
    cleaned = clean_text(tweet)
    vec = vectorizer.transform([cleaned]).toarray()
    pred = model.predict(vec)[0]
    sentiment = ['Negative', 'Neutral', 'Positive'][pred]
    print(f"  '{tweet}' -> {sentiment}")
