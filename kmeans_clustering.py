# Unsupervised learning (Clustering)
# k-means clustering technique

import numpy as np
from sklearn.cluster import KMeans

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

kmeans = KMeans(n_clusters=2, n_init=10, random_state=0)

# train model
kmeans.fit(X)

# extract cluster assignment
clusters = kmeans.labels_

# extract centroids
centroids = kmeans.cluster_centers_

print("Student data with cluster assignments:\n")
for i in range(len(X)):
    print(
        f"Student {i+1}: sleep={X[i][0]} hours, "
        f"coffee={X[i][1]} cups -> cluster {clusters[i]}"
    )

print("\nCluster centers (centroids):")
print(centroids)

print("\nInterpretation:")
print(f"Cluster 0 center: sleep={centroids[0][0]:.2f}, coffee={centroids[0][1]:.2f}")
print(f"Cluster 1 center: sleep={centroids[1][0]:.2f}, coffee={centroids[1][1]:.2f}")

print("\nThis means the algorithm discovered two natural groups of students.")
