# Assignment 36 — Answers

## Q1. Differentiate between model.fit() and model.predict(). Which is used during training and which during testing?

| model.fit(X_train, y_train) | model.predict(X_test) |
|---|---|
| Trains the model: learns parameters/patterns from the training data | Uses the trained model to generate outputs for new inputs |
| Requires both features and true labels | Requires only features (labels are unknown in real use) |
| Used during **training** | Used during **testing** (and in real-world deployment) |

`fit()` is "learning"; `predict()` is "answering". You fit once on training data, then predict on test data and compare with true labels to evaluate.

## Q2. Define Accuracy. Write the mathematical formula and explain it in simple words.

**Accuracy** is the proportion of predictions the model got right out of all predictions made.

**Formula:**

```
Accuracy = (Number of correct predictions / Total number of predictions) × 100%
```

**In terms of confusion-matrix terms:**

```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

**Simple words:** If the model answered 100 questions and got 80 right, its accuracy is 80%.

## Q3. If a model predicts 80 correct results out of 100 samples: what is the accuracy? Is high accuracy always good? Explain.

**Accuracy = 80/100 × 100% = 80%.**

**High accuracy is not always good.** On imbalanced data it can be misleading. Example: a disease test dataset with 95 healthy and 5 sick patients. A useless model that always predicts "healthy" gets 95% accuracy yet detects zero sick patients — the very cases that matter. This is why accuracy must be interpreted alongside precision, recall, and the confusion matrix, especially when classes are imbalanced or errors have unequal costs.

## Q4. Explain the concept of a Confusion Matrix. Why is it more informative than accuracy?

A **confusion matrix** is a table that breaks predictions down by actual vs predicted class:

|  | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actual Positive** | TP (True Positive) | FN (False Negative) |
| **Actual Negative** | FP (False Positive) | TN (True Negative) |

**Why more informative than accuracy:** Accuracy collapses everything into one number and hides *which kind* of errors the model makes. The confusion matrix shows whether the model misses positives (FN), raises false alarms (FP), or is biased toward one class — information essential for choosing the right metric (precision vs recall) and for diagnosing problems accuracy alone cannot reveal.

## Q5. In the Ball classification case study (Cricket vs Tennis), explain TP, TN, FP, FN with real meaning.

Take **Tennis as the positive class** (we are "testing for tennis"):

- **True Positive (TP):** An actual tennis ball correctly predicted as tennis. (Rough, red ball → predicted Tennis ✓)
- **True Negative (TN):** An actual cricket ball correctly predicted as cricket. (Smooth, white ball → predicted Cricket ✓)
- **False Positive (FP):** An actual cricket ball wrongly predicted as tennis — a false alarm.
- **False Negative (FN):** An actual tennis ball wrongly predicted as cricket — a missed detection.

## Q6. If a tennis ball is predicted as cricket ball: what type of error is this? Why is it called that?

This is a **False Negative** (taking Tennis as the positive class).

**Why called that:** The prediction is "negative" (the model said "not tennis" → cricket), and it is "false" because the true answer was positive (it actually was a tennis ball). So: a negative prediction that is false = False Negative. It is the error of *missing* a true positive.

## Q7. Given the confusion matrix below, calculate total errors and total correct predictions.

|  | Predicted Cricket | Predicted Tennis |
|---|---|---|
| **Actual Cricket** | 40 | 5 |
| **Actual Tennis** | 3 | 52 |

(Taking Cricket as positive: TP = 40, FN = 5, FP = 3, TN = 52.)

- **Total correct predictions** = TP + TN = 40 + 52 = **92**
- **Total errors** = FP + FN = 3 + 5 = **8**
- Total samples = 100; Accuracy = 92/100 = **92%**

## Q8. What is the difference between Binary Classification and Multiclass Classification? Give one real-world example of each.

| Binary Classification | Multiclass Classification |
|---|---|
| Exactly **2** possible output classes | **More than 2** possible output classes |
| Output: yes/no, 0/1 | Output: one of N classes |
| Confusion matrix is 2×2 | Confusion matrix is N×N |

**Examples:**
- Binary: Email spam detection — Spam vs Not Spam.
- Multiclass: Handwritten digit recognition — the digit is one of 0–9 (10 classes).

## Q9. Explain how the confusion matrix changes in multiclass classification compared to binary.

In binary classification the confusion matrix is 2×2 with the four cells TP, TN, FP, FN. In multiclass classification with N classes it becomes an **N×N matrix**: rows are actual classes, columns are predicted classes. Correct predictions lie on the **diagonal**; every off-diagonal cell is a specific misclassification (actual class i predicted as class j). TP/TN/FP/FN are then computed **per class** (one-vs-rest): for class i, TP is cell (i,i), FN is the rest of row i, FP is the rest of column i, and TN is everything else.

## Q10. In the Iris dataset: what are the features? What is the label? Why is it a multiclass classification problem? How many possible output classes?

- **Features (4):** sepal length, sepal width, petal length, petal width (all in cm).
- **Label:** the iris species.
- **Why multiclass:** The output is a category chosen from more than two possibilities — classification with >2 classes is by definition multiclass.
- **Number of output classes:** **3** — Iris-setosa, Iris-versicolor, Iris-virginica.
