# Flatten a 2D matrix and pass it through a fully connected layer

matrix = [[6, 4],
          [8, 6]]

flattened = [v for row in matrix for v in row]
print("2D matrix:", matrix)
print("Flattened vector:", flattened)

weights = [0.5, -0.2, 0.3, 0.1]
bias = 0.5
print("FC weights:", weights, ", bias:", bias)

weighted_sum = sum(v * w for v, w in zip(flattened, weights)) + bias
print("Weighted sum =", round(weighted_sum, 4))

output = 1 / (1 + __import__("math").exp(-weighted_sum))
print("Output after sigmoid =", round(output, 4))
print()
print("Role of the flatten layer: it converts the 2D feature maps into a 1D vector,")
print("so the fully connected layer can read them and produce the final prediction.")
