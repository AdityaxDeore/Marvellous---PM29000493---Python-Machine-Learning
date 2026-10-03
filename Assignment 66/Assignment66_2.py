# Plot sigmoid, ReLU and tanh activation functions
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

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
print()
print("Sigmoid: squashes output to (0, 1). Used in output layer for binary classification.")
print("ReLU: outputs x if x > 0 else 0. Used in hidden layers of CNNs and deep networks; fast and avoids vanishing gradient.")
print("Tanh: squashes output to (-1, 1), zero-centered. Used in hidden layers, commonly in RNNs.")
