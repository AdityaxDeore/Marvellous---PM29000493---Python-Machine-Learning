# One gradient-descent weight update step
import math

x = 2.0
w = 0.4
b = 0.5
target = 1.0
lr = 0.1

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

z = w * x + b
pred = sigmoid(z)
error = target - pred

# Gradient of MSE loss w.r.t. weight, then one update step
dL_dw = -2 * error * pred * (1 - pred) * x
w_new = w - lr * dL_dw

print("Input x =", x, ", target =", target, ", learning rate =", lr)
print("Old weight =", w, ", bias =", b)
print("Prediction (sigmoid) =", round(pred, 4))
print("Error (target - prediction) =", round(error, 4))
print("New weight =", round(w_new, 4))
