import numpy as np

data = np.array([6, 7, 8, 9, 10, 11, 12])

variance = np.var(data)      # population variance (ddof=0, divides by N)
std = np.std(data)           # population standard deviation (ddof=0)

print("Dataset:", data)
print("Variance:", variance)
print("Standard Deviation:", std)
