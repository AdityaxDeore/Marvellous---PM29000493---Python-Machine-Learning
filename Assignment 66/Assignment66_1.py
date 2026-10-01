"""
Question 1:
Simulate a single artificial neuron.

Given: x1 = 2, x2 = 3, w1 = 0.4, w2 = 0.6, bias = 0.5.

Tasks:
1. Calculate the weighted sum.
2. Apply the sigmoid activation function.
3. Display the output.
4. Explain whether the output is close to 0 or 1.
"""

import math


def Sigmoid(Value):
    return 1 / (1 + math.exp(-Value))


def SimulateNeuron(X1, X2, W1, W2, Bias):
    weighted_sum = X1 * W1 + X2 * W2 + Bias
    output = Sigmoid(weighted_sum)

    print("Inputs: x1 =", X1, ", x2 =", X2)
    print("Weights: w1 =", W1, ", w2 =", W2, ", bias =", Bias)
    print("Weighted sum =", weighted_sum)
    print("Sigmoid output =", round(output, 4))

    if output >= 0.5:
        print("The output is close to 1 (neuron is activated).")
    else:
        print("The output is close to 0 (neuron is not activated).")


def main():
    print("----- Single Neuron Simulation -----")

    x1, x2 = 2, 3
    w1, w2 = 0.4, 0.6
    bias = 0.5

    SimulateNeuron(x1, x2, w1, w2, bias)


if __name__ == "__main__":
    main()
