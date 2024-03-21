from sklearn.cluster import KMeans
import numpy as np

# Sample data - students and their course enrollment represented as binary vectors
students_courses = np.array([
    [1, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 1]
])

# Part (a): K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(students_courses)

print("K-Means Clusters:")
print(kmeans.labels_)