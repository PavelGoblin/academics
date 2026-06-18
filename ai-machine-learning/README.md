# Kaggle ML Problems — Jupyter Notebooks

Complete solutions to 8 classic Kaggle problems.  
Each notebook is **self-contained** (uses synthetic data — no API key needed) and follows a **clean step-by-step pipeline**.

---

## Notebooks

| # | Notebook | Problem | Algorithm |
|---|----------|---------|-----------|
| 1 | `01_twitter_sentiment.ipynb` | Sentiment Analysis (Multi-class) | Logistic Regression + TF-IDF |
| 2 | `02_sms_spam.ipynb` | Spam Detection (Binary) | Naive Bayes + TF-IDF |
| 3 | `03_wine_quality.ipynb` | Wine Quality (Regression + Classification) | Random Forest |
| 4 | `04_customer_segmentation.ipynb` | Customer Clustering (Unsupervised) | K-Means + PCA |
| 5 | `05_credit_card_fraud.ipynb` | Fraud Detection (Imbalanced) | Random Forest + Undersampling |
| 6 | `06_titanic.ipynb` | Titanic Survival (Binary) | Random Forest + Feature Engineering |
| 7 | `07_house_prices.ipynb` | House Price (Regression) | Gradient Boosting |
| 8 | `08_dogs_vs_cats.ipynb` | Image Classification (CNN) | Convolutional Neural Network |

---

## How to Run

```bash
# 1. Install dependencies
pip install pandas numpy matplotlib scikit-learn tensorflow

# 2. Launch Jupyter
jupyter notebook
```

Each notebook generates synthetic data — no Kaggle account required.

---

## Learning Path

| Phase | Notebooks | Concepts |
|-------|-----------|----------|
| **Fundamentals** | 1, 2, 3 | Text processing, TF-IDF, Regression vs Classification |
| **Intermediate** | 4, 5, 6 | Clustering, Imbalanced data, Feature engineering |
| **Advanced** | 7, 8 | Gradient Boosting, CNN, Deep Learning |

---

## Universal ML Pipeline

Every notebook follows this pattern:

```
1. Load Data    → Generate synthetic dataset
2. Explore      → Shape, distribution, statistics
3. Preprocess   → Clean, encode, scale
4. Split        → train_test_split (80/20)
5. Train        → Fit model
6. Evaluate     → Accuracy, metrics, visualization
7. Predict      → Test with new samples
```

**Memory Aid:** **L**oad → **E**xplore → **P**rocess → **S**plit → **T**rain → **E**valuate → **P**redict  
→ **"LEP STEP"**
