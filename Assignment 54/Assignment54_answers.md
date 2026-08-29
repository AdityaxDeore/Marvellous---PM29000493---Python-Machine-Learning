# Marvellous Infosystems — Machine Learning Assignment 54
## Random Forest & Boosting

---

## Q1. Why is Random Forest an ensemble algorithm?

Because a Random Forest does not make predictions with a single model — it trains **many Decision Trees** (often hundreds) and **combines their predictions** (majority vote for classification, average for regression). The "forest" *is* the ensemble: its accuracy and stability come from aggregating a crowd of trees rather than trusting any one tree.

---

## Q2. Is Random Forest bagging or boosting?

**Bagging.** Random Forest is bagging applied to Decision Trees, with one extra randomization step:

1. Each tree is trained on a **bootstrap sample** (bagging's sampling with replacement).
2. Additionally, at each split, only a **random subset of features** is considered (feature randomness — the "random" in Random Forest).
3. Trees are trained **independently and in parallel**, then aggregated by voting/averaging.

It has nothing sequential or error-correcting, so it is not boosting.

---

## Q3. What is the relationship between Bagging and Random Forest?

**Random Forest is a specialized extension of bagging:**

- **Bagging** = bootstrap samples + train base models independently + aggregate.
- **Random Forest** = bagging **where the base model is a Decision Tree, plus random feature selection at each split**.

So every Random Forest is a bagging ensemble, but not every bagging ensemble is a Random Forest (bagging can use any base estimator). The extra feature randomness is what decorrelates the trees further and gives RF its edge over plain bagged trees.

---

## Q4. What is the difference between "Bagging with Decision Trees" and Random Forest?

| Aspect | Bagging with Decision Trees | Random Forest |
|--------|-----------------------------|---------------|
| **Row sampling** | Bootstrap sample per tree | Bootstrap sample per tree (same) |
| **Feature selection at splits** | Considers **all** features at every split | Considers only a **random subset** of features (e.g. √p for classification) at each split |
| **Tree correlation** | Trees can be highly correlated — a dominant feature gets chosen by most trees | Trees are **decorrelated** — different trees are forced to use different features |
| **Variance reduction** | Good | Better (averaging works best on uncorrelated models) |
| **Typical trees** | Often shallower/pruned | Fully grown, unpruned trees |

**Key takeaway:** feature randomness is the single difference, and it is what makes RF outperform plain bagged trees.

---

## Q5. Can Random Forest do both classification and regression?

**Yes.**
- **Classification** → `RandomForestClassifier`: final prediction by **majority vote** of the trees. Example: predicting whether a customer will churn (yes/no).
- **Regression** → `RandomForestRegressor`: final prediction by **averaging** the trees' numeric outputs. Example: predicting house prices.

---

## Q6. How is the final prediction generated in RF classification? In RF regression?

- **Classification:** each tree casts one vote for a class; the class with the **most votes (majority vote)** wins.
  ```
  Tree votes: [1, 0, 1, 1, 0] → class 1 wins 3–2 → predict 1
  ```
- **Regression:** each tree outputs a number; the forest predicts their **arithmetic mean**.
  ```
  Tree outputs: [210, 225, 218, 230, 205] → predict (210+225+218+230+205)/5 = 217.6
  ```

---

## Q7. What is Boosting?

**Boosting** is an ensemble technique that builds models **sequentially**, where **each new model focuses on the mistakes of the previous ones**, and the final prediction is a **weighted combination** of all models (better models get more weight).

Unlike bagging (parallel, variance reduction), boosting primarily reduces **bias** — it turns a sequence of weak learners into one strong learner. Examples: AdaBoost, Gradient Boosting, XGBoost, LightGBM.

---

## Q8. What is the basic working principle of Boosting?

1. Train a **weak learner** (e.g. a shallow tree / "stump") on the data.
2. **Identify the errors** — find which samples it got wrong.
3. **Increase the importance** of the misclassified samples (in AdaBoost: raise their weights; in Gradient Boosting: fit the next model to the residual errors).
4. Train the **next learner** on the reweighted data / residuals, so it focuses on the hard cases.
5. Repeat for M rounds. Final prediction = **weighted vote/average** of all learners, with more accurate learners getting higher weight.

Each round "patches" the mistakes of the ensemble so far.

---

## Q9. Are Boosting models trained independently or sequentially?

**Sequentially.** Model *m+1* cannot be trained until model *m* is finished, because it needs model *m*'s errors (misclassified samples or residuals) to know what to focus on. This dependency chain is why boosting **cannot be parallelized** the way bagging can — a practical tradeoff for its higher accuracy.

---

## Q10. "Every new learner tries to correct the mistakes of previous learners" — explain with an example.

**Example — email spam classification with AdaBoost:**

- **Round 1:** A decision stump trains on all emails with equal weight. It correctly classifies most, but misclassifies 20 tricky emails (e.g. legitimate newsletters containing the word "offer").
- **Reweighting:** those 20 misclassified emails get *higher weights* — the algorithm now pays more attention to them.
- **Round 2:** the next stump trains on the reweighted data. Because the 20 tricky emails now count more, it chooses a split that gets *them* right (e.g. splitting on "sender is in contacts"), even if it sacrifices accuracy on some easy emails.
- **Round 3+:** remaining errors get boosted again; each new learner specializes in whatever the current ensemble still gets wrong.
- **Final model:** weighted vote of all stumps. Early accurate stumps get high weight; later specialist stumps get weight proportional to their accuracy.

**Net effect:** the ensemble's error keeps shrinking round after round, because every new learner is explicitly aimed at the previous ensemble's blind spots — this is how boosting converts weak learners into a strong one.
