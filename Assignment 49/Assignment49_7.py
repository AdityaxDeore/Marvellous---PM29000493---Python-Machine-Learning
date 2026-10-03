actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

tp = tn = fp = fn = 0

for a, p in zip(actual, predicted):
    if a == 1 and p == 1:
        tp += 1
    elif a == 0 and p == 0:
        tn += 1
    elif a == 0 and p == 1:
        fp += 1
    else:
        fn += 1

print("True Positive (TP):", tp)
print("True Negative (TN):", tn)
print("False Positive (FP):", fp)
print("False Negative (FN):", fn)
