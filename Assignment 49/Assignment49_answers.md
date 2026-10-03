# Assignment 49 — Answers (Q5 & Q6)

## Q5. Explain the concept of a classification report in machine learning. Why is it used and what type of models require it?

A **classification report** is a summary of the performance of a classification model, showing the main classification metrics — precision, recall, F1-score, and support — for each class, along with macro/weighted averages and overall accuracy.

It is used because **accuracy alone can be misleading**, especially with imbalanced datasets. A model that always predicts the majority class can show high accuracy while failing completely on the minority class. The classification report breaks performance down per class, revealing such weaknesses.

It is required for **classification models** (e.g., Logistic Regression, Decision Trees, Random Forest, KNN, SVM, Naive Bayes, neural network classifiers) — any model whose target variable consists of discrete class labels. It is not applicable to regression models, which predict continuous values.

## Q6. In a classification report, explain the meaning of the following metrics: Precision, Recall, F1 Score, Support, Accuracy.

**Precision** — Of all instances the model predicted as positive, how many were actually positive.

$$\text{Precision} = \frac{TP}{TP + FP}$$

High precision means few false alarms. Prefer it when false positives are costly (e.g., spam filtering, fraud alerts).

**Recall** — Of all instances that were actually positive, how many did the model correctly identify.

$$\text{Recall} = \frac{TP}{TP + FN}$$

High recall means few missed positives. Prefer it when false negatives are costly (e.g., disease detection, where missing a real case is dangerous).

**F1 Score** — The harmonic mean of precision and recall, giving a single balanced measure.

$$F1 = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

Use it when both false positives and false negatives matter, or when classes are imbalanced and you need one summary number.

**Support** — The number of actual occurrences of each class in the dataset (i.e., how many true samples belong to that class). It shows whether the evaluation is based on enough samples per class and explains the weighting of averages.

**Accuracy** — The overall fraction of correct predictions.

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

Useful when classes are balanced and all errors are equally costly; unreliable on imbalanced data, which is exactly why the other metrics in the report exist.
