# Marvellous Infosystems — Machine Learning Assignment 53
## Bagging (Bootstrap Aggregating)

---

## Q1. What is Bagging?

**Bagging (Bootstrap Aggregating)** is an ensemble technique that:
1. Creates multiple **bootstrap samples** (random samples *with replacement*) from the training data.
2. Trains one base model on each sample, **independently and in parallel**.
3. **Aggregates** their predictions — majority vote for classification, average for regression.

The result is a single strong, stable model from many unstable base models.

---

## Q2. What is the basic working principle of Bagging?

1. **Bootstrap** — from a dataset of N rows, draw N rows *with replacement*, B times → B different training sets (each misses ~37% of original rows; those are the "out-of-bag" samples).
2. **Train** — fit one base learner (typically a Decision Tree) on each bootstrap sample, independently.
3. **Aggregate** — for a new input, collect all B predictions and combine: majority vote (classification) or mean (regression).

Because each tree sees a slightly different dataset, the trees disagree on noisy points — averaging cancels those disagreements.

---

## Q3. Why sampling *with replacement*?

- With replacement, each bootstrap sample is a **different random variation** of the dataset — some rows repeat, some are left out.
- This variation is what makes the base models **diverse**; without it (sampling without replacement = same data every time), all models would be nearly identical and bagging would gain nothing.
- Mathematically, sampling N rows with replacement from N rows leaves out about **36.8% (≈1/e)** of the original rows in each sample — these out-of-bag rows can even be used for validation.

---

## Q4. Can the same record appear multiple times in a bootstrap sample?

**Yes — that is the defining property of sampling with replacement.** After a row is drawn, it goes back into the pool, so it can be drawn again. A bootstrap sample of size N typically contains some rows 2–3 times and omits ~37% of the original rows entirely. The duplicates act as implicit weighting: repeated rows influence that tree's training more.

---

## Q5. Are Bagging models trained sequentially or independently?

**Independently.** Each base model is trained on its own bootstrap sample with no knowledge of the other models. No model depends on another's output — this is the fundamental contrast with boosting, where each model corrects the previous one's errors.

---

## Q6. Can Bagging be trained in parallel? Why?

**Yes.** Because the models are independent (Q5), each bootstrap sample + model training is a separate task with no dependencies. They can be distributed across CPU cores or machines with near-linear speedup. This is a major practical advantage of bagging (and Random Forest) over boosting, which is inherently sequential.

---

## Q7. How are predictions combined in Bagging for regression?

By **averaging** — the final prediction is the arithmetic mean of all base models' predictions:

```
ŷ_final = (ŷ₁ + ŷ₂ + ... + ŷB) / B
```

Averaging smooths out the high variance of individual regressors (e.g. deep trees), producing a stable prediction. (For classification, the equivalent is majority vote.)

---

## Q8. Which problem does Bagging reduce: bias or variance?

**Variance.** Bagging is designed for **high-variance, low-bias** base learners (like deep Decision Trees).

- A single deep tree overfits — small data changes produce very different trees (high variance).
- Averaging B such trees keeps the low bias (trees are flexible) but divides the variance roughly by B (for uncorrelated trees).
- It does **not** reduce bias much: if every base model is systematically wrong (underfit), their average is wrong too — that is boosting's job.

---

## Q9. Why are Decision Trees used as base estimators in Bagging?

1. **High variance** — trees are unstable; tiny data changes reshape them. Bagging's variance reduction helps them the most.
2. **Low bias** — deep trees fit complex patterns well, so the ensemble stays accurate.
3. **Fast to train** — needed since we train dozens/hundreds of them.
4. **No scaling needed, handles mixed data** — trees work on raw features, keeping the pipeline simple.
5. **Diversity for free** — different bootstrap samples naturally produce very different trees.

This combination is exactly why Bagging + Decision Trees = Random Forest (with extra feature randomness) is so effective.

---

## Q10. Can Logistic Regression be a base estimator in Bagging?

**Yes, technically — but it gains little.** Bagging helps only high-variance, unstable learners. Logistic Regression is a **stable, low-variance, high-bias** model: training it on slightly different bootstrap samples produces nearly identical models, so the ensemble barely differs from a single Logistic Regression. Bagging is *valid* with it (sklearn's `BaggingClassifier` accepts any estimator), but the accuracy improvement is negligible compared to bagging trees. It is occasionally used to stabilize LR on very noisy data, not as a standard practice.
