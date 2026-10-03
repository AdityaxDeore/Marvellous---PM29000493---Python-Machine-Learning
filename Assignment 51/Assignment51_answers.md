# Marvellous Infosystems — Machine Learning Assignment 51
## Variance, Standard Deviation & Feature Scaling

---

## Q1. What is variance? What does it tell about a dataset? Why is it important in ML?

**Variance** is the average of the squared differences of each data point from the mean. It measures how spread out the data is.

- Variance = 0 → all values are identical (no spread).
- Small variance → data points are tightly clustered around the mean.
- Large variance → data points are widely scattered.

**Importance in ML:**
- Feature scaling decisions (StandardScaler uses variance).
- Feature selection — near-zero variance features carry no information and can be dropped.
- Model behavior — high variance in a target/ feature can dominate distance-based algorithms (KNN, K-Means, SVM).
- PCA is built on variance: it finds directions that capture maximum variance.
- Bias–variance tradeoff: model error is decomposed into bias² + variance + noise.

Population variance formula:

```
σ² = Σ(xᵢ − μ)² / N        (μ = mean, N = number of points)
```

---

## Q2. Dataset: 4, 6, 8, 10, 12. Calculate mean, deviations, squared deviations and variance (show steps).

**Step 1 — Mean:**

```
μ = (4 + 6 + 8 + 10 + 12) / 5 = 40 / 5 = 8
```

**Step 2 — Deviations (xᵢ − μ):**

| xᵢ  | xᵢ − μ |
|-----|--------|
| 4   | 4 − 8 = −4 |
| 6   | 6 − 8 = −2 |
| 8   | 8 − 8 = 0  |
| 10  | 10 − 8 = 2 |
| 12  | 12 − 8 = 4 |

**Step 3 — Squared deviations (xᵢ − μ)²:**

| xᵢ  | (xᵢ − μ)² |
|-----|-----------|
| 4   | (−4)² = 16 |
| 6   | (−2)² = 4  |
| 8   | 0² = 0     |
| 10  | 2² = 4     |
| 12  | 4² = 16    |

**Step 4 — Variance (population, divide by N):**

```
σ² = (16 + 4 + 0 + 4 + 16) / 5 = 40 / 5 = 8
```

**Answer: mean = 8, variance = 8 (population).**

---

## Q3. Explain standard deviation. Its relation to variance. What does it tell about the distribution?

**Standard deviation (σ)** is the square root of variance:

```
σ = √variance
```

**Why it exists:** variance is in *squared units* (e.g. if data is in cm, variance is in cm²), which is hard to interpret. Taking the square root brings the spread back to the **same units as the data**, so it is directly comparable with the mean.

**What it tells about the distribution:**
- ~68% of data lies within μ ± σ, ~95% within μ ± 2σ, ~99.7% within μ ± 3σ (empirical rule, for roughly normal data).
- Small σ → data concentrated near the mean (tall, narrow distribution).
- Large σ → data spread wide (flat, wide distribution).

**Relation:** variance = σ², standard deviation = √variance. They describe the same spread; σ is the interpretable one.

---

## Q4. Dataset: 5, 7, 9, 11, 13. Calculate mean, variance and standard deviation (show steps).

**Step 1 — Mean:**

```
μ = (5 + 7 + 9 + 11 + 13) / 5 = 45 / 5 = 9
```

**Step 2 — Deviations and squared deviations:**

| xᵢ  | xᵢ − μ | (xᵢ − μ)² |
|-----|--------|-----------|
| 5   | −4     | 16        |
| 7   | −2     | 4         |
| 9   | 0      | 0         |
| 11  | 2      | 4         |
| 13  | 4      | 16        |

**Step 3 — Variance (population):**

```
σ² = (16 + 4 + 0 + 4 + 16) / 5 = 40 / 5 = 8
```

**Step 4 — Standard deviation:**

```
σ = √8 ≈ 2.83
```

**Answer: mean = 9, variance = 8, standard deviation ≈ 2.83.**

---

## Q5. What is feature scaling? Why is it required before training certain models?

**Feature scaling** is the process of bringing all features to a comparable scale (e.g. a common range or a standard distribution) before training.

**Why it is required:**
- **Distance-based models** (KNN, K-Means, SVM with RBF) compute distances between points. A feature with a large range (e.g. salary in lakhs) will completely dominate a feature with a small range (e.g. age), so the model effectively ignores the small-scale feature.
- **Gradient-descent models** (linear/logistic regression, neural networks) converge much faster when features are on similar scales; otherwise the cost surface is elongated and optimization oscillates.
- **Regularization** (L1/L2) penalizes coefficients — without scaling, features on larger scales are penalized unfairly.

**Not always needed:** tree-based models (Decision Tree, Random Forest) split on thresholds per feature, so scaling does not change their splits.

**Common methods:** Standardization (z-score) and Min-Max normalization.

---

## Q6. What is Standard Scaling (Standardization)? What happens to the mean and standard deviation after scaling?

**Standardization** transforms each feature so it has **mean = 0 and standard deviation = 1**:

```
z = (x − μ) / σ
```

where μ and σ are the mean and standard deviation of the training feature.

**Effect on the data:**
- After standardization, the transformed feature has **mean exactly 0** and **standard deviation exactly 1** (population statistics of the scaled values).
- The *shape* of the distribution is unchanged — values keep their relative positions; outliers remain outliers.
- Values now express "how many standard deviations away from the mean" each point is (z-scores).

---

## Q7. Values 6, 7, 8, 9, 10, 11, 12 with mean = 9, std = 2. Compute standard-scaled values for 6, 9 and 12.

Formula: `z = (x − μ) / σ` with μ = 9, σ = 2.

**For x = 6:**

```
z = (6 − 9) / 2 = −3 / 2 = −1.5
```

**For x = 9:**

```
z = (9 − 9) / 2 = 0 / 2 = 0
```

**For x = 12:**

```
z = (12 − 9) / 2 = 3 / 2 = 1.5
```

| Original value | Scaled value (z) |
|----------------|------------------|
| 6              | −1.5             |
| 9              | 0                |
| 12             | 1.5              |

**Interpretation:** 6 lies 1.5 standard deviations below the mean, 9 is exactly at the mean, and 12 lies 1.5 standard deviations above the mean.
