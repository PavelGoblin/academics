# Kaggle ML Problems — Jupyter Notebooks

8 complete ML solutions using **real Kaggle datasets** (auto-downloaded via `kagglehub`).  
Each notebook follows a clear **step-by-step pipeline**: Load → Explore → Preprocess → Train → Evaluate → Predict.

---

## Notebooks

| # | Notebook | Dataset | Problem Type | Algorithm |
|---|----------|---------|-------------|-----------|
| 1 | `01_twitter_sentiment.ipynb` | [Twitter Airline Sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) | Multi-class Text Classification | Logistic Regression + TF-IDF |
| 2 | `02_sms_spam.ipynb` | [SMS Spam](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) | Binary Text Classification | Naive Bayes + TF-IDF |
| 3 | `03_wine_quality.ipynb` | [Red Wine Quality](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) | Regression + Classification | Random Forest |
| 4 | `04_customer_segmentation.ipynb` | [Mall Customers](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) | Unsupervised Clustering | K-Means + PCA |
| 5 | `05_credit_card_fraud.ipynb` | [Credit Card Fraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) | Imbalanced Classification | Random Forest + Undersampling |
| 6 | `06_titanic.ipynb` | [Titanic](https://www.kaggle.com/c/titanic) | Binary Classification | Random Forest + Feature Engineering |
| 7 | `07_house_prices.ipynb` | [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) | Regression | Gradient Boosting |
| 8 | `08_dogs_vs_cats.ipynb` | [Dogs vs Cats](https://www.kaggle.com/competitions/dogs-vs-cats) | Image Classification | CNN (Keras) |

---

## Quick Start

### 🖥️ Local Jupyter
```bash
pip install -r requirements.txt
jupyter notebook
```

### ☁️ Google Colab (Recommended)
1. Open any notebook on GitHub
2. Click **"Open in Colab"** button
3. Run the first cell → upload your `kaggle.json` when prompted
4. Run All (Runtime → Run all)

> **Get your Kaggle API key:**
> 1. Go to [kaggle.com](https://kaggle.com) → Account → API → Create New Token
> 2. Download `kaggle.json` and upload it when the notebook asks

## Universal ML Pipeline (Memory Aid)

```
1. LOAD      → Download real data from Kaggle
2. EXPLORE   → Visualize distributions, correlations, missing values
3. CLEAN     → Handle nulls, encode categories, scale features
4. SPLIT     → train_test_split (80/20)
5. TRAIN     → Fit model (with tuning)
6. EVALUATE  → Accuracy, confusion matrix, ROC, feature importance
7. PREDICT   → Test new samples, export submission
```

**L**oad → **E**xplore → **C**lean → **S**plit → **T**rain → **E**valuate → **P**redict  
→ **"LEC STEP"**
