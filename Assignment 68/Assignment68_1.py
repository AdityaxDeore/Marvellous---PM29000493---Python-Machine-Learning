# Manual 2D convolution with a 3x3 edge-detection kernel

image = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

kernel = [[-1, -1, -1],
          [0, 0, 0],
          [1, 1, 1]]

feature_map = []
for i in range(3):
    row = []
    for j in range(3):
        region = [[image[i + ki][j + kj] for kj in range(3)] for ki in range(3)]
        value = sum(image[i + ki][j + kj] * kernel[ki][kj]
                    for ki in range(3) for kj in range(3))
        print(f"Region at ({i},{j}): {region} -> sum = {value}")
        row.append(value)
    feature_map.append(row)

print()
print("Final feature map:")
for r in feature_map:
    print(r)

assert feature_map == [[3, 3, 3], [0, 0, 0], [-3, -3, -3]], "Feature map mismatch!"
print("Assertion passed: feature map matches the expected output.")
