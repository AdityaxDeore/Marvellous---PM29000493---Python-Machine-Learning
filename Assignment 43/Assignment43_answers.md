# Assignment 43 — Answers

## Q1. Supervised vs Unsupervised Machine Learning

**Supervised Learning** learns from labeled data, i.e. every training example comes with the correct answer (label). The model learns the mapping from inputs to outputs so it can predict the label of new, unseen data. Example: a model trained on thousands of emails labeled "spam" or "not spam" learns to classify new emails.

**Unsupervised Learning** learns from unlabeled data, i.e. no correct answers are provided. The model discovers hidden patterns, groups, or structures in the data on its own. Example: grouping customers with similar buying habits into segments without any predefined categories.

**Key differences:**

| Aspect | Supervised | Unsupervised |
|---|---|---|
| Training data | Labeled (input + correct output) | Unlabeled (input only) |
| Goal | Predict/classify new data | Find hidden structure/patterns |
| Feedback | Error measured against known labels | No error signal; judged by internal structure |
| Examples | Spam detection, price prediction | Customer segmentation, anomaly detection |

## Q2. Supervised or Unsupervised — with reasons

a) **Predicting house prices based on size and location — Supervised.** The model trains on houses with known prices (labels) and learns to predict the price of a new house.

b) **Grouping customers based on shopping behavior — Unsupervised.** No predefined categories exist; the algorithm itself discovers groups of similar customers.

c) **Predicting whether an email is spam or not — Supervised.** Training emails are labeled "spam"/"not spam", and the model learns to classify new emails.

## Q3. Classification vs Regression

**Classification** predicts a *discrete category* (class label) from a fixed set of possible classes. The output is qualitative — which group an input belongs to.
*Example:* An email spam filter predicts "spam" or "not spam" for each incoming email.

**Regression** predicts a *continuous numerical value*. The output is quantitative — a number on a scale.
*Example:* A model predicting the resale price of a car (e.g. ₹4,20,000) from its age, mileage, and brand.

| Aspect | Classification | Regression |
|---|---|---|
| Output type | Discrete class labels | Continuous numbers |
| Evaluation | Accuracy, precision, recall, F1 | MSE, RMSE, R² |
| Example algorithms | Logistic Regression, Decision Tree classifier, KNN | Linear Regression, Ridge, SVR |

## Q4. Student marks dataset — which ML task?

A dataset of students with marks in Math, Science, and English, by itself, is **neither classification, regression, nor clustering** until a goal is defined — but the most natural task is **clustering (unsupervised)** if we group students by performance patterns, or **regression (supervised)** if we define a target.

Reasoning: marks are continuous numerical features with no label/target column. If the goal is "find groups of similar-performing students", it is **clustering** — an unsupervised task, since no target is given and the algorithm discovers the groups itself. If the goal becomes "predict a student's English marks from Math and Science marks", it is **regression** — a supervised task with a defined target. It would only be **classification** if marks were converted to labels (e.g. Pass/Fail) and predicted as categories.

## Q8. EDA — concept, importance, common steps

**Exploratory Data Analysis (EDA)** is the process of examining and summarizing a dataset — using statistics and visualizations — to understand its structure, patterns, anomalies, and relationships *before* building a model.

**Why it is important before training a model:**
- Reveals missing values, outliers, and errors that would corrupt training.
- Shows feature distributions and relationships, helping choose the right model and features.
- Prevents garbage-in-garbage-out: a model trained on misunderstood data gives misleading results.

**At least 3 common EDA steps:**
1. **Summary statistics** — `df.describe()`, mean/median/std of each column to understand scale and spread.
2. **Missing-value and duplicate check** — `df.isnull().sum()`, `df.duplicated().sum()`, then clean the data.
3. **Visualization** — histograms for distributions, box plots for outliers, heatmaps/correlation matrices for feature relationships.
