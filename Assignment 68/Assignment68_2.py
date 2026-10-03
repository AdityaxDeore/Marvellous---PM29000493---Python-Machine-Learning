"""
Question 2:
Write a Python program to demonstrate ReLU and Max Pooling.

Input: feature_map = [[3, 3, 3], [0, 0, 0], [-3, -3, -3]]
ReLU rule: value < 0 -> 0, else keep the value.

Tasks:
1. Create a feature map with positive and negative values.
2. Apply ReLU.
3. Apply 2x2 max pooling.
4. Display the output after each step.
5. Explain why pooling reduces size.
"""


def ApplyRelu(FeatureMap):
    relu_output = []
    for row in FeatureMap:
        new_row = []
        for v in row:
            if v > 0:
                new_row.append(v)
            else:
                new_row.append(0)
        relu_output.append(new_row)
    return relu_output


def ApplyMaxPooling(Matrix):
    pooled = []
    for i in range(len(Matrix) - 1):
        row = []
        for j in range(len(Matrix[0]) - 1):
            window = [Matrix[i][j], Matrix[i][j + 1],
                      Matrix[i + 1][j], Matrix[i + 1][j + 1]]
            row.append(max(window))
        pooled.append(row)
    return pooled


def DisplayMatrix(Title, Matrix, First=False):
    if not First:
        print()
    print(Title)
    for r in Matrix:
        print(r)


def main():
    print("----- ReLU and Max Pooling -----")

    feature_map = [[3, 3, 3],
                   [0, 0, 0],
                   [-3, -3, -3]]

    DisplayMatrix("Feature map:", feature_map, First=True)

    relu_output = ApplyRelu(feature_map)
    DisplayMatrix("After ReLU (negative values -> 0):", relu_output)

    pooled = ApplyMaxPooling(relu_output)
    DisplayMatrix("After 2x2 max pooling (stride 1):", pooled)

    print()
    print("Pooling reduces size because each 2x2 window is replaced by a single value,")
    print("so the output shrinks (3x3 -> 2x2 here). This keeps the strongest feature,")
    print("cuts computation and makes the model tolerant to small shifts in position.")


if __name__ == "__main__":
    main()
