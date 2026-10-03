# Mean Squared Error and Binary Cross-Entropy implemented manually
import numpy as np

def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)

def binary_cross_entropy(actual, predicted):
    eps = 1e-15
    predicted = np.clip(predicted, eps, 1 - eps)
    return -np.mean(actual * np.log(predicted) + (1 - actual) * np.log(1 - predicted))

actual = np.array([1.0, 0.0, 1.0, 0.0])
predicted = np.array([0.9, 0.1, 0.8, 0.4])

mse_loss = mse(actual, predicted)
bce_loss = binary_cross_entropy(actual, predicted)

print("Actual:", actual)
print("Predicted:", predicted)
print("MSE loss =", round(mse_loss, 4))
print("Binary Cross-Entropy loss =", round(bce_loss, 4))
print()
print("MSE is used for regression problems (predicting continuous values).")
print("Binary Cross-Entropy is used for binary classification problems (predicting class probabilities).")
