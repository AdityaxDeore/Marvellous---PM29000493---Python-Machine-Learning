"""
Question 5:
Create a Python program that:
a) Takes a list of training labels, e.g. ['A', 'B', 'A', 'A', 'B'].
b) Counts how many times each class appears.
c) Returns the class with the highest count (majority vote).
"""


def CountLabels(Labels):
    counts = {}
    for label in Labels:
        counts[label] = counts.get(label, 0) + 1
    return counts


def FindMajorityClass(Counts):
    return max(Counts, key=Counts.get)


def main():
    print("----- Majority Voting -----")

    labels = ['A', 'B', 'A', 'A', 'B']

    counts = CountLabels(labels)
    print("Counts:", counts)

    majority = FindMajorityClass(counts)
    print("Majority class:", majority)


if __name__ == "__main__":
    main()
