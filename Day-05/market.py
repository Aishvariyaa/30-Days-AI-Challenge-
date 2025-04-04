import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load your dataset
df = pd.read_csv("store.csv")  # Replace with actual dataset file

# Encode categorical columns (if not already done)
label_encoders = {}
for col in ['reps', 'product', 'region']:  # Encoding categorical columns
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Store encoders for later decoding if needed

# Select numerical columns for clustering
X = df[['qty', 'revenue']]

# Normalize data (important for hierarchical clustering)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform hierarchical clustering
linkage_matrix = linkage(X_scaled, method='ward')

# Extract clusters (cutting at threshold distance)
max_d = 50  # Adjust based on dendrogram
df['Cluster'] = fcluster(linkage_matrix, max_d, criterion='distance')

# ---- STEP 1: Analyze clusters ----
cluster_summary = df.groupby('Cluster')[['qty', 'revenue']].mean()
print("\nCluster Summary:\n", cluster_summary)

# ---- STEP 2: Visualize clusters ----
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='qty', y='revenue', hue='Cluster', palette='tab10', s=100, edgecolor='black')

plt.title("Market Segmentation Using Hierarchical Clustering")
plt.xlabel("Quantity Sold")
plt.ylabel("Revenue")
plt.legend(title="Cluster")
plt.grid(True)
plt.show()
