from sklearn.neighbors import KNeighborsClassifier

X_train = [[2, 3], [3, 4], [4, 3], [2, 4], [3, 3], [4, 4], [1, 2], [5, 3],
           [3, 2], [2, 5],
           [7, 8], [8, 7], [6, 9], [7, 7], [8, 8], [6, 8], [9, 7], [7, 9],
           [9, 8], [6, 7]]
y_train = ['A'] * 10 + ['B'] * 10
test_point = [[5, 5]]

for k in [1, 3, 5, 7]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    print(f"K = {k}: predicted class =", model.predict(test_point)[0])
