import numpy as np

training_points = np.array([[2, 3], [3, 4], [4, 3], [7, 8], [8, 7], [6, 9]])
new_point = np.array([5, 5])

distances = np.sqrt(np.sum((training_points - new_point) ** 2, axis=1))
print("Distances:", distances)
print("Index of closest training point:", np.argmin(distances))
