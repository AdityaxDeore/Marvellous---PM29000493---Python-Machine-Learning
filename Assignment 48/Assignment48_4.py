import math

def euclidean(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

print("Distance between (1,2) and (4,6):", euclidean((1, 2), (4, 6)))

training_points = [(2, 3), (3, 4), (4, 3), (7, 8), (8, 7), (6, 9)]
new_point = (5, 5)

distances = [euclidean(new_point, p) for p in training_points]
print("Distances:", distances)

sorted_distances = sorted(distances)
print("Sorted distances:", sorted_distances)
print("Nearest neighbor distance:", sorted_distances[0])
