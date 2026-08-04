# Assignment 37 — Answers

## Q1. Define Artificial Intelligence (AI). How is AI different from traditional software systems?

**Artificial Intelligence** is the field of computer science concerned with building systems that can perform tasks requiring human-like intelligence — learning, reasoning, perception, decision-making, and language understanding.

**AI vs traditional software:**

| Traditional software | AI systems |
|---|---|
| Executes fixed, hand-written logic for every case | Learns behavior from data or reasons over knowledge |
| Output is fully determined by the programmer's rules | Output can adapt to inputs never explicitly programmed for |
| Fails on situations the programmer did not anticipate | Generalizes to new, unseen situations |
| Example: a calculator, a payroll program | Example: a chatbot, a fraud-detection model |

## Q2. Explain the three types of AI based on capability: Narrow AI, General AI, Super AI.

1. **Narrow AI (Weak AI):** Designed for one specific task. Cannot transfer its skill to other domains. *Example:* spam filters, chess engines, voice assistants. All AI in use today is narrow AI.
2. **General AI (Strong AI / AGI):** Hypothetical human-level intelligence — can understand, learn, and apply knowledge across any domain like a human. Does not exist yet.
3. **Super AI (Superintelligence):** Hypothetical AI that surpasses human intelligence in all fields, including creativity and decision-making. Purely theoretical at present.

## Q3. Is Machine Learning a part of AI, or is AI a part of Machine Learning? Explain with a hierarchy.

**Machine Learning is a part of AI** — a subset, not the other way round. Hierarchy (outermost to innermost):

```
Artificial Intelligence (broadest: any intelligent behavior)
 └─ Machine Learning (AI that learns from data)
     └─ Deep Learning (ML using deep neural networks)
```

AI also includes non-ML areas such as rule-based expert systems, search algorithms, and symbolic reasoning. ML is one approach *within* AI: the approach where the system learns from data rather than from hand-coded rules.

## Q4. Define Machine Learning. Explain the three main types with one example each.

**Machine Learning** is the subset of AI in which computers learn patterns from data and improve at a task with experience, without being explicitly programmed.

1. **Supervised Learning** — learns from labeled data (input + correct answer). *Example:* email spam classification trained on emails labeled spam/not-spam.
2. **Unsupervised Learning** — finds structure in unlabeled data. *Example:* grouping customers into segments based on shopping behavior (clustering).
3. **Reinforcement Learning** — an agent learns by trial and error, receiving rewards or penalties from an environment. *Example:* a program learning to play chess by winning/losing games.

## Q5. Differentiate Supervised, Unsupervised, and Reinforcement Learning on: data requirement, output, real-world applications.

| Aspect | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
|---|---|---|---|
| **Data requirement** | Labeled data: every sample has the correct answer | Unlabeled data: only inputs, no answers | No fixed dataset: an environment that gives reward/penalty feedback |
| **Output** | A predicted label (classification) or value (regression) for new inputs | Discovered structure: clusters, associations, reduced dimensions | A policy: the best action to take in each state to maximize reward |
| **Real-world applications** | Spam detection, house-price prediction, disease diagnosis | Customer segmentation, anomaly/fraud detection, recommendation grouping | Game playing (chess, Go), robotics control, self-driving cars |

## Q6. What is Reinforcement Learning?

**Reinforcement Learning** is the ML paradigm where an **agent** learns optimal behavior through interaction with an **environment**. The agent takes **actions**, the environment returns a new **state** and a **reward** (positive or negative), and the agent adjusts its **policy** to maximize cumulative reward over time. There is no labeled "correct answer" per step — learning happens by trial, error, and delayed feedback. *Example:* training a robot to walk: falling gives negative reward, moving forward gives positive reward, and the robot gradually learns a stable gait.

## Q7. Define Deep Learning. How is Deep Learning different from traditional Machine Learning?

**Deep Learning** is the subset of ML that uses **artificial neural networks with many layers** (deep networks) to learn hierarchical representations directly from raw data.

**DL vs traditional ML:**

| Traditional ML | Deep Learning |
|---|---|
| Relies on manual feature engineering by humans | Learns features automatically from raw data |
| Works well on small/medium structured datasets | Needs large datasets to perform well |
| Models: decision trees, SVM, linear regression | Models: CNNs, RNNs, transformers |
| Trains fast on CPU | Training is compute-heavy, usually needs GPUs |
| Example: predicting sales from a spreadsheet | Example: image recognition, machine translation |

## Q8. What is Data Science? How is Data Science different from Machine Learning?

**Data Science** is the interdisciplinary field of extracting knowledge and insights from data using statistics, data analysis, visualization, and machine learning. It covers the full pipeline: collecting, cleaning, analyzing, and communicating findings from data.

**Difference from ML:**

| Data Science | Machine Learning |
|---|---|
| Broader discipline: the entire data-to-insight pipeline | A set of techniques (subset) used within data science |
| Goal: understand data and support decisions (dashboards, reports, predictions) | Goal: build models that learn and predict automatically |
| Uses statistics, SQL, visualization, and ML | Focuses on algorithms that learn from data |
| Output may be a report or dashboard, not just a model | Output is a trained model |

In short: ML is a tool in the data scientist's toolbox; data science is the end-to-end practice.

## Q9. Explain the complete Data Science lifecycle.

1. **Data Collection** — Gather data from databases, APIs, files, sensors, or web scraping. Define the problem and identify relevant data sources.
2. **Data Cleaning** — Handle missing values, duplicates, outliers, and inconsistent formats. Convert data into a usable form (preprocessing).
3. **Data Analysis** — Exploratory Data Analysis (EDA): summary statistics, visualizations, and correlation analysis to understand patterns and relationships.
4. **Model Building** — Select features, split data into train/test sets, train ML models, tune hyperparameters, and evaluate performance.
5. **Deployment** — Put the model or insights into production (API, dashboard, application), monitor performance over time, and retrain as new data arrives.

## Q10. What is Generative AI (GenAI)? How is it different from traditional predictive ML models?

**Generative AI** refers to AI models that **create new content** — text, images, audio, video, or code — rather than just analyzing or classifying existing data. Examples: ChatGPT (text), image generators, code assistants. They are typically built on large neural networks (e.g. transformers) trained on massive datasets.

**GenAI vs traditional predictive ML:**

| Traditional predictive ML | Generative AI |
|---|---|
| Predicts a label or value for a given input (discriminative) | Generates new, original content (generative) |
| Output: a class, a number, a yes/no decision | Output: a paragraph, an image, a song |
| Example: "Is this email spam?" → Yes/No | Example: "Write a product description" → new text |
| Usually trained on smaller, task-specific datasets | Trained on vast, general datasets |
| Answers questions about data | Creates data that resembles its training distribution |
