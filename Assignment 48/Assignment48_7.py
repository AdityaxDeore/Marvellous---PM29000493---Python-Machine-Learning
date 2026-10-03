from sklearn.neighbors import KNeighborsClassifier

X_train = [[2, 3], [3, 4], [4, 3], [7, 8], [8, 7], [6, 9]]
y_train = ['A', 'A', 'A', 'B', 'B', 'B']

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

print("Predicted class for [5,5]:", model.predict([[5, 5]])[0])
