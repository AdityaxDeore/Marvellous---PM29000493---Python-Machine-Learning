"""
Question 4:
Show one weight update step in an Artificial Neural Network.

Tasks:
1. Take input, weight, bias, target and learning rate.
2. Calculate the prediction.
3. Calculate the error.
4. Update the weight using gradient descent.
5. Display the old and the updated weight.
"""

import math


def Sigmoid(Value):
    return 1 / (1 + math.exp(-Value))


def UpdateWeight(Input, Weight, Bias, Target, LearningRate):
    z = Weight * Input + Bias
    prediction = Sigmoid(z)
    error = Target - prediction

    # Gradient of MSE loss w.r.t. weight, then one update step
    gradient = -2 * error * prediction * (1 - prediction) * Input
    new_weight = Weight - LearningRate * gradient

    print("Input x =", Input, ", target =", Target, ", learning rate =", LearningRate)
    print("Old weight =", Weight, ", bias =", Bias)
    print("Prediction (sigmoid) =", round(prediction, 4))
    print("Error (target - prediction) =", round(error, 4))
    print("New weight =", round(new_weight, 4))


def main():
    print("----- Weight Update using Gradient Descent -----")

    x = 2.0
    w = 0.4
    b = 0.5
    target = 1.0
    learning_rate = 0.1

    UpdateWeight(x, w, b, target, learning_rate)


if __name__ == "__main__":
    main()
