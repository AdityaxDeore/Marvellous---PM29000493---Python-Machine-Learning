# Assignment 48 — K-Nearest Neighbors (KNN)

## Q1. How does KNN classify a new data point? Explain the role of K and how the final class is decided.

KNN (K-Nearest Neighbors) is a lazy, distance-based classifier:

1. Store all training points with their class labels (no model is "trained" upfront).
2. For a new point, compute its distance (usually Euclidean) to every training point.
3. Select the K nearest training points — these are the "neighbors".
4. Take a majority vote among the neighbors' labels: the class that appears most often becomes the predicted class of the new point.

The parameter K controls how many neighbors vote. Small K makes the decision depend on very few nearby points (sensitive to noise); large K considers a wider neighborhood (smoother, but may include irrelevant far-away points). For ties, K is usually chosen odd for binary classification, or the tie is broken by the closest neighbor.

## Q2. Class A: (2,3), (3,4), (4,3); Class B: (7,8), (8,7), (6,9); new point (5,5).

**(a) Euclidean distance from (5,5) to each training point** (d = √[(x₂−x₁)² + (y₂−y₁)²]):

- (2,3): √[(5−2)² + (5−3)²] = √(9+4) = √13 ≈ 3.61 → Class A
- (3,4): √[(5−3)² + (5−4)²] = √(4+1) = √5 ≈ 2.24 → Class A
- (4,3): √[(5−4)² + (5−3)²] = √(1+4) = √5 ≈ 2.24 → Class A
- (7,8): √[(5−7)² + (5−8)²] = √(4+9) = √13 ≈ 3.61 → Class B
- (8,7): √[(5−8)² + (5−7)²] = √(9+4) = √13 ≈ 3.61 → Class B
- (6,9): √[(5−6)² + (5−9)²] = √(1+16) = √17 ≈ 4.12 → Class B

**(b) K = 3 nearest neighbors:** the two closest are (3,4) and (4,3) (both √5 ≈ 2.24, Class A). The third-nearest distance is √13 ≈ 3.61, shared by three points — (2,3) of Class A and (7,8), (8,7) of Class B. Whichever √13 point is taken third, the vote is:

**(c) Majority vote → Class A.** Taking the natural ordering, neighbors are (3,4)→A, (4,3)→A, (2,3)→A: 3 votes for A, 0 for B. Even in the worst tie-break (two B points picked), A still gets 2 of 3 votes. Predicted class: **A**.

## Q3. Effect of very small K (e.g. 1) vs very large K (e.g. 100). Which is better and why?

- Very small K (K = 1): the prediction depends on a single nearest point. The decision boundary becomes jagged and the model memorizes noise and outliers — high variance, overfitting. One mislabeled point can flip the prediction.
- Very large K (K = 100): the prediction averages over a huge neighborhood, washing out local patterns — high bias, underfitting. In the extreme (K = all data), every point gets the majority class.

Neither extreme is good. A moderate K (commonly chosen via cross-validation, often around √n, and odd for binary problems) balances bias and variance: smooth enough to ignore noise, local enough to capture the true pattern.

## Q10. Why may accuracy decrease when K is too small or too large? How to choose the best K in practice?

Accuracy drops at small K because the model overfits noise — it is unstable, and a single noisy neighbor changes the prediction. Accuracy drops at large K because the model underfits — distant, irrelevant points dilute the vote and erase local structure; with K too large, minority classes may never win a vote.

Choosing the best K in the real world:

1. Try a range of K values (e.g. 1 to 20, or 1 to √n) and evaluate each with cross-validation.
2. Pick the K with the highest validation accuracy (or F1), preferring odd K for binary classification to reduce ties.
3. Also consider the elbow in the error-vs-K curve and domain constraints (cost of misclassification, class balance).
