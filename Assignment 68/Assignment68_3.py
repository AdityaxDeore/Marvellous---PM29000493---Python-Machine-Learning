"""
Question 3:
Write a Python program to show flattening.

Input: matrix = [[6, 4], [8, 6]]

Tasks:
1. Take a 2D matrix.
2. Convert it into a 1D vector.
3. Pass it to a fully connected layer.
4. Calculate the final output manually.
5. Explain the role of the flatten layer in CNN.

Expected Output: flatten_output = [6, 4, 8, 6]
"""

import math


def FlattenMatrix(Matrix):
    flattened = []
    for row in Matrix:
        for v in row:
            flattened.append(v)
    return flattened


def FullyConnectedLayer(Vector, Weights, Bias):
    weighted_sum = sum(v * w for v, w in zip(Vector, Weights)) + Bias
    output = 1 / (1 + math.exp(-weighted_sum))
    return weighted_sum, output


def main():
    print("----- Flattening and Fully Connected Layer -----")

    matrix = [[6, 4],
              [8, 6]]

    flattened = FlattenMatrix(matrix)
    print("2D matrix:", matrix)
    print("Flattened vector:", flattened)

    weights = [0.5, -0.2, 0.3, 0.1]
    bias = 0.5
    print("FC weights:", weights, ", bias:", bias)

    weighted_sum, output = FullyConnectedLayer(flattened, weights, bias)
    print("Weighted sum =", round(weighted_sum, 4))
    print("Output after sigmoid =", round(output, 4))

    print()
    print("Role of the flatten layer: it converts the 2D feature maps into a 1D vector,")
    print("so the fully connected layer can read them and produce the final prediction.")


if __name__ == "__main__":
    main()
