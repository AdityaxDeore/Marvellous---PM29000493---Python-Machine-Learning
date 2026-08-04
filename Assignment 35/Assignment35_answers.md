# Assignment 35 — Answers

## Q1. Define Machine Learning. How is it different from traditional rule-based programming? Give a real-world example.

**Machine Learning** is a field of AI in which a computer learns patterns from data and improves its performance on a task with experience, instead of being explicitly programmed with rules.

**Difference from rule-based programming:**

| Traditional (rule-based) programming | Machine Learning |
|---|---|
| Programmer writes explicit rules: `Input + Rules → Output` | Model learns rules from data: `Input + Output → Rules (model)` |
| Rules are hand-coded by humans | Rules are derived automatically from training data |
| Cannot improve without a human rewriting the rules | Improves as more data is provided |
| Fails when situations were not anticipated by the programmer | Handles unseen variations by generalizing patterns |

**Example:** Spam email filtering. A rule-based system checks hand-written rules like "if subject contains 'lottery', mark as spam" — spammers quickly bypass it. An ML system is trained on thousands of emails already labeled spam/not-spam and learns which words, patterns, and sender behaviors indicate spam, so it detects new spam emails that follow no known rule.

## Q2. What are Independent Variables and Dependent Variables in ML? Using the Ball classification case study, identify them.

- **Independent variables (features, X):** the input attributes used to make a prediction. They are assumed to influence, but not be influenced by, the outcome.
- **Dependent variable (label, y):** the output we want to predict. Its value "depends" on the independent variables.

**Ball case study:** We classify balls as Cricket or Tennis using:

| Variable | Role |
|---|---|
| Surface (Rough/Smooth) | Independent variable (feature) |
| Colour (Red/White) | Independent variable (feature) |
| Label (Cricket/Tennis) | Dependent variable (label) |

The ball's type depends on its surface and colour; the label is what we predict from them.

## Q3. Explain the difference between Features and Labels. Are features always numeric? Justify.

- **Features** are the measurable input attributes of each sample (the X columns), e.g. Surface, Colour, StudyHours.
- **Label** is the target output we want to predict (the y column), e.g. ball type, Pass/Fail.

**Features are not always numeric.** Raw features can be text (product reviews), images (pixel data), audio (waveforms), or categories (Surface = Rough/Smooth). However, most ML algorithms require numeric input, so non-numeric features are converted — e.g. categorical features via label encoding or one-hot encoding — before training. The label also need not be numeric (e.g. "Cricket"/"Tennis"), though it too is encoded for training.

## Q4. What is Supervised Machine Learning? Why is labeled data mandatory in supervised learning?

**Supervised ML** is learning from labeled data: every training sample pairs input features with the correct answer, and the algorithm learns the mapping from inputs to outputs. Types: classification (discrete labels) and regression (continuous values).

**Labeled data is mandatory** because supervision comes from the labels themselves. During training, the model predicts an output, compares it with the true label, computes the error, and adjusts its parameters to reduce that error. Without labels there is no "correct answer" to compare against, so the model has no signal to learn from — that is unsupervised learning instead.

## Q5. Explain why we cannot train and test a model using the same dataset. What problem may occur?

Training and testing on the same data defeats the purpose of evaluation. The model has already seen every sample and its label, so it can simply memorize the answers instead of learning general patterns. This causes **overfitting** — the model scores deceptively high on the seen data but performs poorly on new, unseen data. Since the real goal is performance on future unseen inputs, evaluation must be done on data the model never trained on.

## Q6. What is the purpose of splitting a dataset into training and testing sets? What is the typical ratio used in industry?

**Purpose:** To obtain an honest, unbiased estimate of how the model will perform on unseen data. The model learns from the training set, and the testing set is held back purely for evaluation — simulating real-world conditions.

**Typical industry ratio:** 80/20 (80% training, 20% testing). Other common splits are 70/30 and 75/25. For large datasets, sometimes 90/10. A validation set may also be carved out (e.g. 60/20/20) for tuning hyperparameters.

## Q7. Explain the meaning of: X_train, X_test, y_train, y_test.

After splitting a dataset (X = features, y = label):

- **X_train** — feature values of the training samples; the input the model learns from.
- **y_train** — the true labels of the training samples; what the model learns to predict.
- **X_test** — feature values of the held-out test samples; the unseen inputs used for evaluation.
- **y_test** — the true labels of the test samples; compared against the model's predictions to measure performance.

Typical usage: `model.fit(X_train, y_train)` then `model.predict(X_test)` and compare with `y_test`.

## Q8. What is Data Preprocessing? Why is it necessary before training a Machine Learning model?

**Data preprocessing** is the set of cleaning and transformation steps applied to raw data to make it suitable for training: handling missing values, removing duplicates, encoding categorical variables, scaling features, removing outliers, and splitting features/labels.

**Why necessary:** Real-world data is messy — missing values crash or bias algorithms, categorical text cannot be processed numerically, features on different scales distort distance-based and gradient-based models, and noise/outliers mislead learning. Preprocessing ensures the model receives clean, consistent, numeric data, which directly improves accuracy and reliability.

## Q9. Explain Label Encoding with a suitable example. When should it be used?

**Label Encoding** converts categorical values into integers by assigning each unique category a number.

**Example:** Ball dataset, feature Colour:

| Colour (original) | Encoded |
|---|---|
| Red | 0 |
| White | 1 |

And Label: Tennis → 0, Cricket → 1.

**When to use:** for categorical features/labels with tree-based models (decision trees, random forests), which handle arbitrary integer codes well. **Avoid** label encoding for linear models or distance-based models (KNN, SVM) on nominal categories, because the assigned numbers imply a false ordering (e.g. White=1 > Red=0) — use one-hot encoding there instead. It is safe for ordinal data (e.g. Low=0, Medium=1, High=2) where the order is meaningful.

## Q10. Define the following terms in one or two lines each.

- **Model** — The learned mathematical function (parameters + structure) that maps inputs to predictions.
- **Training** — The process of feeding labeled data to an algorithm so it adjusts its parameters to minimize error.
- **Testing** — Evaluating the trained model on unseen data to measure how well it generalizes.
- **Prediction** — The model's output for a given input sample.
- **Accuracy** — The fraction of correct predictions: (correct predictions / total predictions) × 100%.
