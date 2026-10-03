# Marvellous Infosystems — Deep Learning Assignment 57
## Deep Learning Foundations: ANN, Neurons, Weights & Bias

---

## Q1. What is Deep Learning? Why is it considered a subset of Machine Learning?

**Deep Learning (DL)** is a branch of Machine Learning that uses **artificial neural networks with multiple hidden layers** ("deep" networks) to learn hierarchical representations directly from raw data.

- A shallow network (1 hidden layer) can approximate simple functions; a deep network stacks layers so that **early layers learn simple features and deeper layers combine them into complex concepts** (e.g. edges → shapes → faces in an image).
- DL models are trained end-to-end with **backpropagation + gradient descent** on large datasets.

**Why a subset of ML:** Machine Learning is the field of algorithms that learn patterns from data instead of being explicitly programmed. Deep Learning is one such family of algorithms — it learns from data, so it sits strictly inside ML:

```
Artificial Intelligence  ⊃  Machine Learning  ⊃  Deep Learning
```

Every deep learning model is a machine learning model, but not every ML model (e.g. decision trees, SVM) is deep learning.

---

## Q2. Differentiate AI, ML, DL with examples.

| Aspect | Artificial Intelligence (AI) | Machine Learning (ML) | Deep Learning (DL) |
|---|---|---|---|
| Definition | Machines performing tasks that need human-like intelligence | AI subset: systems that **learn patterns from data** | ML subset: learning with **deep neural networks** |
| How it works | Rules, search, logic, or learning | Statistical models trained on data | Multi-layer neural nets, backpropagation |
| Data need | Varies | Moderate datasets | Large datasets |
| Example 1 | Chess-playing program using search | Spam filter trained on labeled emails | CNN classifying images (ResNet) |
| Example 2 | Rule-based chatbot | House-price prediction with regression | LLM generating text (transformers) |

**One-line memory hook:** AI is the goal, ML is an approach to reach it, DL is a powerful technique within ML.

---

## Q3. Difference between rule-based and learning-based systems.

| Aspect | Rule-based systems | Learning-based systems |
|---|---|---|
| Logic source | Human experts write explicit **if-then rules** | Model **learns patterns from data** |
| Example | "If email contains 'lottery' AND sender unknown → spam" | Spam classifier trained on 1M labeled emails |
| Adaptability | Brittle — fails on cases the rules didn't cover | Generalizes to unseen, similar cases |
| Maintenance | Rules must be manually updated as the world changes | Retrain on new data |
| Best for | Well-defined, stable domains (tax calculation, eligibility checks) | Fuzzy, high-variation domains (vision, speech, language) |
| Weakness | Cannot handle ambiguity or exceptions gracefully | Needs data; can be a black box |

---

## Q4. What is meant by training a model in DL?

Training means **adjusting the network's weights and biases so its predictions match the true answers** on a training dataset. The loop:

1. **Forward pass** — feed input through the network, get a prediction.
2. **Compute loss** — measure prediction error with a loss function (e.g. MSE, cross-entropy).
3. **Backward pass (backpropagation)** — compute how much each weight contributed to the error (gradients via chain rule).
4. **Update** — nudge each weight opposite to its gradient, scaled by the learning rate (gradient descent).
5. **Repeat** over many epochs until the loss stops decreasing.

Result: the network has "learned" — its weights now encode the patterns in the data, so it performs well on new, unseen inputs.

---

## Q5. What is ANN? Explain with block diagram.

An **Artificial Neural Network (ANN)** is a computing model inspired by the brain: a network of interconnected processing units (**neurons**) organized in layers. Each connection carries a **weight**; each neuron computes a **weighted sum of its inputs, adds a bias, and passes the result through an activation function**.

### Block diagram

```
                    ┌──────────────────────────────────────┐
  Input features    │        Hidden layer(s)               │   Output
                    │                                      │
   x1 ──┐           │    h1 ──┐                            │
        │           │         │                            │
   x2 ──┼────▶ weighted sum ──┼──▶ activation ──▶ ... ──▶──┼──▶ y
        │      + bias│    h2 ──┘                            │
   x3 ──┘           │                                      │
                    └──────────────────────────────────────┘
         ◀──────── forward propagation ────────▶
```

- **Input layer** — receives raw features (x1, x2, x3).
- **Hidden layers** — transform inputs into increasingly abstract features.
- **Output layer** — produces the final prediction (class label, probability, or value).
- Every arrow is a weighted connection; learning = tuning those weights.

---

## Q6. Why is it called a Neural Network? Relation with human brain neurons.

It is called a *neural* network because its design is **loosely inspired by biological neural networks in the human brain**:

- The brain has ~86 billion **neurons** connected by **synapses**; an ANN has artificial neurons connected by weighted links.
- A biological neuron receives signals through dendrites, processes them in the cell body, and fires an output down the axon if the signal is strong enough. An artificial neuron similarly receives weighted inputs, sums them, and "fires" (produces a non-zero output) via an activation function.
- Learning in the brain = strengthening/weakening synaptic connections; learning in an ANN = adjusting weights.

The resemblance is **functional inspiration, not replication** — artificial neurons are drastic mathematical simplifications of real neurons.

---

## Q7. Biological neuron vs artificial neuron comparison.

| Aspect | Biological neuron | Artificial neuron |
|---|---|---|
| Signal receiver | Dendrites | Input connections (x1, x2, …) |
| Connection strength | Synaptic strength | Weight (w1, w2, …) |
| Processing | Cell body sums incoming signals | Computes weighted sum Σwi·xi + b |
| Firing decision | Fires if membrane potential crosses threshold | Activation function decides output |
| Output carrier | Axon | Output value passed to next layer |
| Learning | Synapses strengthen/weaken with experience | Weights updated by backpropagation |
| Speed | Slow (milliseconds), massively parallel | Fast (nanoseconds), far fewer units |

---

## Q8. What is a neuron in ANN? Explain working.

A **neuron (node/unit)** is the basic computational unit of an ANN. Working, step by step:

1. **Receive inputs** — the neuron gets values x1, x2, …, xn from the previous layer (or raw features).
2. **Weighted sum** — multiply each input by its connection weight and add the bias:
   `z = w1·x1 + w2·x2 + … + wn·xn + b`
3. **Activation** — pass z through a non-linear activation function:
   `a = f(z)` (e.g. sigmoid, ReLU, tanh)
4. **Output** — send `a` as input to neurons in the next layer.

Without the activation function the whole network would collapse into a single linear transformation, no matter how many layers it has — the non-linearity is what lets the network learn complex patterns.

---

## Q9. What are weights? Why are they important?

**Weights (w1, w2, …)** are the learnable parameters on the connections between neurons. Each weight scales its input — it decides **how much influence that input has** on the neuron's output.

Why important:

- **They encode everything the network has learned.** A trained network's "knowledge" is entirely stored in its weights.
- **Large |weight|** → the input strongly affects the output; **weight ≈ 0** → the input is effectively ignored.
- **Sign matters:** positive weight = excitatory (input pushes output up), negative = inhibitory.
- During training, backpropagation computes gradients and updates weights to reduce error — **learning IS weight adjustment**.
- Random initialization of weights (not zeros) is essential so neurons learn different features (symmetry breaking).

---

## Q10. What is bias in ANN? Why is it required?

**Bias (b)** is an extra learnable parameter added to the weighted sum of every neuron:

```
z = w1·x1 + w2·x2 + … + wn·xn + b
```

It acts like the neuron's **threshold / baseline shift** — an intercept term, exactly like `c` in the line `y = mx + c`.

Why required:

- **Without bias, the decision boundary must pass through the origin.** A neuron could never output a non-zero value when all inputs are zero, and it could never shift its activation left/right.
- Bias gives each neuron **independent control over when it fires**, regardless of the inputs — it shifts the activation function horizontally.
- Like weights, biases are learned during training via backpropagation.

**Example:** a neuron with weights (1, 1) and no bias can only separate classes with a line through the origin; adding bias `b = -1.5` lets the same neuron implement the AND gate (fires only when x1 = x2 = 1).
