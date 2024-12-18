import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Step 1: Generate a synthetic clustering dataset
X, _ = make_blobs(n_samples=300, centers=4, random_state=42)

# Step 2: Visualize the generated data
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Generated Clustering Dataset")
plt.show()

# Step 3: Use the elbow method to find the optimal number of clusters
inertia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(k_range, inertia, marker='o')
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.show()

# Step 4: Apply KMeans clustering with the optimal number of clusters (let's assume it's 4)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Step 5: Plot the results of KMeans clustering
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title(f"KMeans Clustering with {optimal_k} Clusters")
plt.legend()
plt.show()