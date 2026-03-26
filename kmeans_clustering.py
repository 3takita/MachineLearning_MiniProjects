# Project 2: K-Means Student Clustering
# ------------------------------------------------
# Scenario:
# Group students based on sleep and coffee habits.

import numpy as np
from sklearn.cluster import KMeans

# -----------------------------
# Step 1: Dataset
# -----------------------------
# Each row: [hours_of_sleep, cups_of_coffee]
X = np.array([
    [5, 3],
    [7, 1],
    [8, 3],
    [8, 1],
    [6, 2],
    [7, 2],
    [6, 1],
    [6, 1],
    [5, 2]
])

# -----------------------------
# Step 2: Create Model
# -----------------------------
kmeans = KMeans(n_clusters=2, n_init=10, random_state=0)

# -----------------------------
# Step 3: Train Model
# -----------------------------
kmeans.fit(X)

# -----------------------------
# Step 4: Extract Results
# -----------------------------
clusters = kmeans.labels_              # cluster assignment per data point
centroids = kmeans.cluster_centers_    # cluster centers

# -----------------------------
# Step 5: Display Results
# -----------------------------
print("Student data with cluster assignments:\n")
for i in range(len(X)):
    print(
        f"Student {i+1}: sleep={X[i][0]} hours, "
        f"coffee={X[i][1]} cups -> cluster {clusters[i]}"
    )

print("\nCluster centers (centroids):")
print(centroids)

print("\nInterpretation:")
print(f"Cluster 0: sleep={centroids[0][0]:.2f}, coffee={centroids[0][1]:.2f}")
print(f"Cluster 1: sleep={centroids[1][0]:.2f}, coffee={centroids[1][1]:.2f}")
