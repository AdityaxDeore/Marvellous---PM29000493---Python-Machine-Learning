"""
Question 1:
Write a Python program to manually perform convolution.

Input:
5x5 matrix image = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
3x3 edge detection kernel = [[-1, -1, -1],
                             [0, 0, 0],
                             [1, 1, 1]]

Tasks:
1. Move the kernel over the image.
2. Perform multiplication and addition.
3. Generate the feature map.
4. Print each region calculation.

Expected Output: feature_map = [[3, 3, 3], [0, 0, 0], [-3, -3, -3]]
"""


def ApplyConvolution(Image, Kernel):
    feature_map = []

    for i in range(3):
        row = []
        for j in range(3):
            region = [[Image[i + ki][j + kj] for kj in range(3)]
                      for ki in range(3)]
            value = sum(Image[i + ki][j + kj] * Kernel[ki][kj]
                        for ki in range(3) for kj in range(3))
            print(f"Region at ({i},{j}): {region} -> sum = {value}")
            row.append(value)
        feature_map.append(row)

    return feature_map


def DisplayFeatureMap(FeatureMap):
    print()
    print("Final feature map:")
    for r in FeatureMap:
        print(r)


def main():
    print("----- Manual 2D Convolution -----")

    image = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

    kernel = [[-1, -1, -1],
              [0, 0, 0],
              [1, 1, 1]]

    feature_map = ApplyConvolution(image, kernel)
    DisplayFeatureMap(feature_map)

    assert feature_map == [[3, 3, 3], [0, 0, 0], [-3, -3, -3]], \
        "Feature map mismatch!"
    print("Assertion passed: feature map matches the expected output.")


if __name__ == "__main__":
    main()
