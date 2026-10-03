from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

best_k, best_accuracy = 1, 0.0
for k in range(1, 11):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"K = {k}: accuracy = {accuracy:.4f}")
    if accuracy > best_accuracy:
        best_k, best_accuracy = k, accuracy

print("Best K:", best_k, "with accuracy:", round(best_accuracy, 4))
