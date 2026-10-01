"""
Question 3:
Calculate the loss manually.

Tasks:
1. Implement Mean Squared Error.
2. Implement Binary Cross Entropy.
3. Take actual and predicted values.
4. Display the loss.
5. Explain which loss is used for regression and which for classification.
"""

import numpy as np


def CalculateMSE(Actual, Predicted):
    return np.mean((Actual - Predicted) ** 2)


def CalculateBCE(Actual, Predicted):
    eps = 1e-15
    clipped = np.clip(Predicted, eps, 1 - eps)
    return -np.mean(Actual * np.log(clipped) + (1 - Actual) * np.log(1 - clipped))


def CalculateLosses():
    actual = np.array([1.0, 0.0, 1.0, 0.0])
    predicted = np.array([0.9, 0.1, 0.8, 0.4])

    mse_loss = CalculateMSE(actual, predicted)
    bce_loss = CalculateBCE(actual, predicted)

    print("Actual:", actual)
    print("Predicted:", predicted)
    print("MSE loss =", round(mse_loss, 4))
    print("Binary Cross-Entropy loss =", round(bce_loss, 4))


def ExplainLosses():
    print()
    print("MSE is used for regression problems (predicting continuous values).")
    print("Binary Cross-Entropy is used for binary classification problems (predicting class probabilities).")


def main():
    print("----- Loss Functions -----")

    CalculateLosses()
    ExplainLosses()


if __name__ == "__main__":
    main()
