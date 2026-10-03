import numpy as np

actual = np.array([1, 1, 1, 1, 0, 0, 0, 0])
predicted = np.array([1, 1, 0, 1, 0, 1, 0, 0])

tp = np.sum((actual == 1) & (predicted == 1))
tn = np.sum((actual == 0) & (predicted == 0))
fp = np.sum((actual == 0) & (predicted == 1))
fn = np.sum((actual == 1) & (predicted == 0))

print("True Positive (TP):", tp)
print("True Negative (TN):", tn)
print("False Positive (FP):", fp)
print("False Negative (FN):", fn)
