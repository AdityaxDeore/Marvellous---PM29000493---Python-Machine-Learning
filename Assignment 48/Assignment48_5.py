labels = ['A', 'B', 'A', 'A', 'B']

counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1

majority = max(counts, key=counts.get)
print("Counts:", counts)
print("Majority class:", majority)
