"""
Question 9:
Write a Python program using scikit-learn to generate a classification
report for the following data:
actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]
Display the complete classification report including precision, recall,
F1-score, and support.
"""

from sklearn.metrics import classification_report


def ShowClassificationReport(Actual, Predicted):
    report = classification_report(Actual, Predicted)
    print(report)


def main():
    print("----- Classification Report -----")

    actual = [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    ShowClassificationReport(actual, predicted)


if __name__ == "__main__":
    main()
