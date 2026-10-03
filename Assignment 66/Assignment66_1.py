# Simulate a single artificial neuron
import math

x1, x2 = 2, 3
w1, w2 = 0.4, 0.6
bias = 0.5

weighted_sum = x1 * w1 + x2 * w2 + bias
output = 1 / (1 + math.exp(-weighted_sum))

print("Inputs: x1 =", x1, ", x2 =", x2)
print("Weights: w1 =", w1, ", w2 =", w2, ", bias =", bias)
print("Weighted sum =", weighted_sum)
print("Sigmoid output =", round(output, 4))

if output >= 0.5:
    print("The output is close to 1 (neuron is activated).")
else:
    print("The output is close to 0 (neuron is not activated).")
