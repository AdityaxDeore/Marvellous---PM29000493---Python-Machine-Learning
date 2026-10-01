"""
Question 2:
Demonstrate the activation functions: Sigmoid, ReLU and Tanh.

Tasks:
1. Take input values from -10 to 10.
2. Plot all three functions using Matplotlib.
3. Explain the use of each activation function.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def PlotActivations():
    x = np.linspace(-10, 10, 200)

    sigmoid = 1 / (1 + np.exp(-x))
    relu = np.maximum(0, x)
    tanh = np.tanh(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, sigmoid, label="Sigmoid")
    plt.plot(x, relu, label="ReLU")
    plt.plot(x, tanh, label="Tanh")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.title("Activation Functions")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("activation_functions.png")
    plt.close()

    print("Plot saved as activation_functions.png")


def ExplainActivations():
    print()
    print("Sigmoid: squashes output to (0, 1). Used in output layer for binary classification.")
    print("ReLU: outputs x if x > 0 else 0. Used in hidden layers of CNNs and deep networks; fast and avoids vanishing gradient.")
    print("Tanh: squashes output to (-1, 1), zero-centered. Used in hidden layers, commonly in RNNs.")


def main():
    print("----- Activation Functions -----")

    PlotActivations()
    ExplainActivations()


if __name__ == "__main__":
    main()
