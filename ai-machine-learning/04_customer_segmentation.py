"""
Customer Segmentation (Mall Customers)
========================================
Goal: Group customers into segments for targeted marketing
ML Task: Unsupervised Clustering
Algorithm: K-Means + PCA for visualization
"""

import kagglehub
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 1. Load Data
print("[1] Downloading dataset...")
path = kagglehub.dataset_download("vjchoudhary7/customer-segmentation-tutorial-in-python")
df = pd.read_csv(f"{path}/Mall_Customers.csv")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# 2. Quick EDA
print(f"\n[2] Exploring...")
print(f"Age range: {df['Age'].min()} - {df['Age'].max()}")
print(f"Income range: {df['Annual Income (k$)'].min()} - {df['Annual Income (k$)'].max()}")
print(f"Spending range: {df['Spending Score (1-100)'].min()} - {df['Spending Score (1-100)'].max()}")
print(f"Gender distribution:\n{df['Gender'].value_counts()}")

# 3. Select features for clustering
features = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
X = df[features]

# Encode Gender
X = pd.get_dummies(X, columns=['Gender'], drop_first=False).astype(int)
print(f"\n[3] Features after encoding: {list(X.columns)}")

# 4. Scale features (important for K-Means!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Find optimal K using Elbow Method
print("\n[4] Finding optimal clusters (Elbow Method)...")
inertias = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(8, 4))
plt.plot(K_range, inertias, 'bo-')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.grid(True)
plt.tight_layout()
plt.savefig('04_elbow_plot.png')
print("  Elbow plot saved as '04_elbow_plot.png'")

# 6. Train K-Means with K=5 (optimal from elbow)
print("\n[5] Training K-Means with K=5...")
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

print(f"Cluster sizes:\n{df['Cluster'].value_counts().sort_index()}")

# 7. Cluster Analysis
print("\n[6] Cluster Profiles (mean values):")
profile = df.groupby('Cluster')[features].mean().round(1)
profile['Count'] = df['Cluster'].value_counts().sort_index().values
print(profile.to_string())

# 8. Visualize with PCA
print("\n[7] Visualizing clusters (PCA)...")
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]

plt.figure(figsize=(8, 6))
for cluster in range(5):
    mask = df['Cluster'] == cluster
    plt.scatter(df.loc[mask, 'PCA1'], df.loc[mask, 'PCA2'],
                label=f'Cluster {cluster}', alpha=0.7)

plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('Customer Segments (PCA-reduced to 2D)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('04_clusters_pca.png')
print("  Cluster plot saved as '04_clusters_pca.png'")

print("\n[8] Interpretation Guide:")
print("  Cluster 0: Low income, low spending - Budget conscious")
print("  Cluster 1: High income, low spending - Selective")
print("  Cluster 2: Low income, high spending - Impulsive")
print("  Cluster 3: High income, high spending - Premium (target!)")
print("  Cluster 4: Medium income, medium spending - Average")
