# Marvellous Infosystems — Deep Learning Assignment 61
## Feedforward Networks, Loss Functions, Training Concepts & CNN

---

## Q1. What is a Feedforward Neural Network (FNN)? Explain architecture.

A **Feedforward Neural Network** is the simplest deep network architecture: information flows in **one direction only** — from input, through hidden layers, to output — with **no cycles or feedback loops**.

**Architecture:**

```
Input layer → Hidden layer 1 → Hidden layer 2 → … → Output layer
     x ──▶│ W1,b1,f1 │──▶│ W2,b2,f2 │──▶ … ──▶│ Wout,bout,fout │──▶ ŷ
```

- **Input layer** — one neuron per feature; pass-through.
- **Hidden layers** — each computes `a = f(W·a_prev + b)` (fully connected: every neuron links to every neuron in the next layer).
- **Output layer** — task-specific activation (sigmoid / softmax / linear).
- An MLP (Multi-Layer Perceptron) is the classic example of an FNN. RNNs and their feedback connections are explicitly *not* feedforward.

---

## Q2. Why is it called a "feedforward" network?

Because data is **fed forward** through the network — it moves strictly in one direction (input → output) and **never flows backward or loops**:

- There are **no cycles**: a neuron's output never becomes (directly or indirectly) its own input.
- Contrast with **recurrent** networks (RNNs), where hidden states feed *back* into the network at the next time step.

The name describes the **direction of information flow during the forward pass**. (Backpropagation does send gradients backward, but only during training — the network's data flow remains feedforward.)

---

## Q3. Explain working steps of FNN from input to output.

**Training-time forward pass** (inference uses steps 1–4 only):

1. **Present input** — feed feature vector x into the input layer.
2. **Layer-by-layer transformation** — for each hidden layer in order:
   a. Weighted sum: `z = W·a_prev + b`
   b. Activation: `a = f(z)` (e.g. ReLU)
3. **Output computation** — final layer applies its activation to produce prediction ŷ.
4. **(Inference stops here** — ŷ is the answer.)
5. **Loss computation** — compare ŷ with true label y: `L = loss(y, ŷ)`.
6. **Backpropagation** — compute ∂L/∂w for every weight, backward through layers.
7. **Weight update** — `w ← w − η·∂L/∂w`; repeat steps 1–7 over many epochs until loss converges.

---

## Q4. Explain Mean Squared Error with example.

**Mean Squared Error (MSE)** is the average of squared differences between true and predicted values:

```
MSE = (1/n) · Σ (yi − ŷi)²
```

Squaring **penalizes large errors much more** than small ones and keeps the loss differentiable.

**Worked example:** actual = [3, 5, 2], predicted = [2.5, 5.0, 3.0]

| i | yi | ŷi | yi − ŷi | (yi − ŷi)² |
|---|---|---|---|---|
| 1 | 3 | 2.5 | 0.5 | 0.25 |
| 2 | 5 | 5.0 | 0.0 | 0.00 |
| 3 | 2 | 3.0 | −1.0 | 1.00 |

MSE = (0.25 + 0.00 + 1.00) / 3 = 1.25 / 3 ≈ **0.417**

**Used for:** regression tasks (predicting continuous values like prices, temperatures).

---

## Q5. What is Binary Cross-Entropy loss function?

**Binary Cross-Entropy (BCE)** measures how far predicted probabilities are from true binary labels (0/1):

```
BCE = −(1/n) · Σ [ yi·log(ŷi) + (1 − yi)·log(1 − ŷi) ]
```

- If y = 1, only the first term matters: loss = −log(ŷ) → **0** when ŷ = 1 (confident + correct), → **∞** when ŷ → 0 (confident + wrong). Wrong confident predictions are punished harshly.
- If y = 0, symmetric via the second term.

**Why not MSE for classification?** MSE on sigmoid outputs creates a non-convex loss with flat regions (slow learning); BCE + sigmoid gives clean, steep gradients. **Standard pairing:** sigmoid output + binary cross-entropy for binary classification.

---

## Q6. What is an optimizer in Deep Learning?

An **optimizer** is the algorithm that **updates the network's weights** to minimize the loss, using the gradients computed by backpropagation. The basic update rule is gradient descent:

```
w ← w − η · ∇wL
```

Common optimizers:

| Optimizer | Idea |
|---|---|
| **SGD** (Stochastic Gradient Descent) | Update on each mini-batch; simple, noisy |
| **SGD + Momentum** | Adds a velocity term to push through flat regions |
| **RMSprop** | Adapts learning rate per weight using recent gradient magnitudes |
| **Adam** | Combines momentum + adaptive rates; the **default choice** — fast and robust |

The optimizer is distinct from the loss function: the **loss** defines *what* to minimize; the **optimizer** defines *how* to move through weight space.

---

## Q7. What is an epoch in neural network training?

One **epoch** = **one complete pass through the entire training dataset** — every training example has been fed through the network (forward + backward) exactly once.

- Training typically needs **many epochs** (tens to hundreds) because one pass is not enough for weights to converge.
- **Too few epochs** → underfitting (model hasn't learned enough).
- **Too many epochs** → overfitting (model memorizes training data; validation loss starts rising while training loss keeps falling) — controlled with **early stopping**.

---

## Q8. Differentiate epoch, batch size, and iteration.

| Term | Meaning |
|---|---|
| **Epoch** | One full pass over the entire training dataset |
| **Batch size** | Number of training examples used in **one** weight update |
| **Iteration** | One weight update = one batch processed (one forward + backward pass) |

**Relationship:** iterations per epoch = (dataset size) / (batch size)

**Example:** 1,000 training images, batch size = 100 → **10 iterations per epoch**. Training for 50 epochs = 500 iterations total.

**Batch-size trade-off:** small batches → noisy updates but better generalization and less memory; large batches → stable gradients, faster per-epoch compute, but more memory and can generalize worse.

---

## Q9. What is CNN? Why is it popular for image processing?

A **Convolutional Neural Network (CNN)** is a deep network designed for grid-like data (images) built from three layer types:

1. **Convolutional layers** — small filters (kernels) slide over the image, computing dot products to produce **feature maps** (edges → textures → object parts, hierarchically).
2. **Pooling layers** — downsample feature maps (e.g. max-pooling), keeping dominant features while reducing size.
3. **Fully connected layers** — final classification from the extracted features.

**Why popular for images:**

- **Preserves spatial structure** — processes pixels in their 2D neighborhoods instead of flattening them into an unordered vector.
- **Weight sharing / translation invariance** — one filter detects an edge *anywhere* in the image; far fewer parameters than dense layers.
- **Hierarchical features** — learns edges → shapes → objects automatically, which is exactly how visual recognition works.

---

## Q10. Why does CNN perform better than ANN for image data?

1. **Parameter explosion in ANN:** a 256×256×3 image flattened = 196,608 inputs. One dense layer of just 100 neurons needs **~19.7 million** weights — huge, slow, and prone to overfitting. A CNN's 3×3×3 filter needs only **27 weights**, reused across the whole image.
2. **Destroys spatial structure:** flattening throws away the fact that neighboring pixels form edges and shapes; CNNs exploit locality directly through convolution.
3. **No translation invariance:** an ANN must relearn a cat's ear separately at every pixel position; a CNN's shared filter detects it anywhere.
4. **Overfitting:** with millions of parameters and limited image data, dense ANNs memorize instead of generalizing; CNNs' weight sharing acts as strong regularization.

**Bottom line:** ANNs treat an image as an unstructured bag of pixels; CNNs treat it as what it is — a 2D spatial signal — and that inductive bias is why they dominate vision.
