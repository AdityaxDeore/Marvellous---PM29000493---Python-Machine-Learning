"""
Question 7:
Consider the following data:
Actual Values
[1, 1, 1, 1, 0, 0, 0, 0]
Predicted Values
[1, 1, 0, 1, 0, 1, 0, 0]
Determine the following values:
True Positive (TP)
True Negative (TN)
False Positive (FP)
False Negative (FN)

Expected Output: TP: 3, TN: 3, FP: 1, FN: 1
"""


def FindConfusionValues(Actual, Predicted):
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for a, p in zip(Actual, Predicted):
        if a == 1 and p == 1:
            tp += 1
        elif a == 0 and p == 0:
            tn += 1
        elif a == 0 and p == 1:
            fp += 1
        else:
            fn += 1

    return tp, tn, fp, fn


def main():
    print("----- Confusion Matrix Values -----")

    actual = [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    tp, tn, fp, fn = FindConfusionValues(actual, predicted)

    print("True Positive (TP):", tp)
    print("True Negative (TN):", tn)
    print("False Positive (FP):", fp)
    print("False Negative (FN):", fn)


if __name__ == "__main__":
    main()
