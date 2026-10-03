# ReLU activation followed by 2x2 max pooling

feature_map = [[3, 3, 3],
               [0, 0, 0],
               [-3, -3, -3]]

print("Feature map:")
for r in feature_map:
    print(r)

relu_output = [[v if v > 0 else 0 for v in row] for row in feature_map]
print()
print("After ReLU (negative values -> 0):")
for r in relu_output:
    print(r)

pooled = []
for i in range(len(relu_output) - 1):
    row = []
    for j in range(len(relu_output[0]) - 1):
        window = [relu_output[i][j], relu_output[i][j + 1],
                  relu_output[i + 1][j], relu_output[i + 1][j + 1]]
        row.append(max(window))
    pooled.append(row)

print()
print("After 2x2 max pooling (stride 1):")
for r in pooled:
    print(r)
print()
print("Pooling reduces size because each 2x2 window is replaced by a single value,")
print("so the output shrinks (3x3 -> 2x2 here). This keeps the strongest feature,")
print("cuts computation and makes the model tolerant to small shifts in position.")
