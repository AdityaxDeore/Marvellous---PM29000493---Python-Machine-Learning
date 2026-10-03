import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([[25, 20000],
                 [30, 40000],
                 [35, 80000]])

point1 = np.array([25, 20000])
point2 = np.array([35, 80000])

dist_before = np.linalg.norm(point1 - point2)
print("Euclidean distance before scaling:", dist_before)

scaler = StandardScaler()
scaled = scaler.fit_transform(data)
sp1 = scaler.transform([point1])[0]
sp2 = scaler.transform([point2])[0]

dist_after = np.linalg.norm(sp1 - sp2)
print("Euclidean distance after scaling:", dist_after)

print("\nExplanation: before scaling, the second feature (salary, in tens of thousands)")
print("dominates the distance calculation and the first feature (age) has almost no")
print("effect. After scaling, both features contribute equally, so the distance")
print("reflects differences in both features fairly.")
