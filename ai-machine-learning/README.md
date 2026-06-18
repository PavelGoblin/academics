# 🤖 AI & Machine Learning — 8 Classic Kaggle Problems

A collection of **8 complete ML solutions** for popular Kaggle datasets.  
Each script is **self-contained** (auto-downloads from Kaggle) and follows a clear **7-step pipeline**.

---

## 📋 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run any script
python 01_twitter_sentiment.py
```

> **Need a Kaggle API key?**  
> Run `kagglehub.login()` first time, or place `kaggle.json` in `~/.kaggle/`.

---

## 📂 Problems Solved

| # | Dataset | Problem Type | Algorithm | Lines |
|---|---------|-------------|-----------|-------|
| 1 | [Twitter Airline Sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) | Multi-class Text Classification | Logistic Regression + TF-IDF | ~90 |
| 2 | [SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) | Binary Text Classification | Naive Bayes + TF-IDF | ~85 |
| 3 | [Red Wine Quality](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) | Regression + Classification | Random Forest | ~80 |
| 4 | [Customer Segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) | Unsupervised Clustering | K-Means + PCA | ~100 |
| 5 | [Credit Card Fraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) | Imbalanced Classification | Random Forest + Undersampling | ~80 |
| 6 | [Titanic](https://www.kaggle.com/c/titanic) | Binary Classification | Random Forest + Feature Engineering | ~100 |
| 7 | [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) | Regression | Gradient Boosting | ~85 |
| 8 | [Dogs vs Cats](https://www.kaggle.com/competitions/dogs-vs-cats) | Image Classification | CNN (TensorFlow/Keras) | ~120 |

---

## 🧠 Step-by-Step Learning Guide

### Phase 1: Fundamentals (Start Here)

| Step | Script | What You'll Learn |
|------|--------|-------------------|
| 1 | `01_twitter_sentiment.py` | Text cleaning, TF-IDF, multi-class classification |
| 2 | `02_sms_spam.py` | Naive Bayes, precision/recall, confusion matrix |
| 3 | `03_wine_quality.py` | Regression vs classification, feature importance |

### Phase 2: Intermediate

| Step | Script | What You'll Learn |
|------|--------|-------------------|
| 4 | `04_customer_segmentation.py` | K-Means, Elbow Method, PCA visualization |
| 5 | `05_credit_card_fraud.py` | Imbalanced data, undersampling, ROC-AUC |
| 6 | `06_titanic.py` | Feature engineering, GridSearchCV, submission |

### Phase 3: Advanced

| Step | Script | What You'll Learn |
|------|--------|-------------------|
| 7 | `07_house_prices.py` | Log-transform, Gradient Boosting, RMSLE |
| 8 | `08_dogs_vs_cats.py` | CNN architecture, data augmentation, image generators |

---

## 📐 Universal ML Pipeline (Memory Aid)

Every script follows this **7-step pattern** — memorize it for your CT/exam:

```
┌─────────────────────────────────────────────┐
│  1. LOAD     — Download & read data          │
│  2. EXPLORE  — Shape, distribution, missing   │
│  3. CLEAN    — Handle nulls, encode, scale    │
│  4. SPLIT    — train_test_split (80/20)       │
│  5. TRAIN    — Fit model on training set      │
│  6. EVALUATE — Accuracy, confusion, metrics   │
│  7. PREDICT  — New predictions + export       │
└─────────────────────────────────────────────┘
```

**Remember:** **L**oad → **E**xplore → **C**lean → **S**plit → **T**rain → **E**valuate → **P**redict  
→ **"LEC STEP"** (easy to recall!)

---

## 📊 Model Comparison Table

| # | Accuracy | Key Challenge | Best For Learning |
|---|----------|---------------|--------------------|
| 1 | ~75% | Text preprocessing | NLP fundamentals |
| 2 | ~98% | Class imbalance | Text classification |
| 3 | ~70% | Subjective scores | Regression metrics |
| 4 | — | Choosing K | Unsupervised learning |
| 5 | ~95%+ (AUC) | Extreme imbalance | Handling skewed data |
| 6 | ~82% | Feature engineering | Kaggle competition workflow |
| 7 | ~0.88 (R²) | Many features | Advanced regression |
| 8 | ~85% | Training time | Deep learning basics |

---

## 🚀 Submission Files (for competitions)

| Script | Output File |
|--------|-------------|
| `06_titanic.py` | `06_titanic_submission.csv` |
| `07_house_prices.py` | `07_house_prices_submission.csv` |

Upload these to Kaggle to see your leaderboard rank!

---

## 🧪 Quick Test (after running all scripts)

```bash
python -c "
# Verify all scripts ran successfully
import os
files = [
    '04_elbow_plot.png',
    '04_clusters_pca.png',
    '06_titanic_submission.csv',
    '07_house_prices_submission.csv',
    '08_training_history.png'
]
for f in files:
    if os.path.exists(f):
        print(f'✅ {f}')
    else:
        print(f'❌ {f}')
"
```

---

*Happy Learning! 🚀 For questions, open an issue on GitHub.*
