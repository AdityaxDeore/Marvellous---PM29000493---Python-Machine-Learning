# Marvellous Infosystems — Deep Learning Assignment 60
## Activation Functions: Sigmoid, Tanh, ReLU, Softmax

---

## Q1. Explain Sigmoid activation function with graph. σ(x) = 1 / (1 + e^(−x))

The **sigmoid (logistic) function** squashes any real input into the range **(0, 1)**:

```
σ(x) = 1 / (1 + e^(−x))
```

**Graph description (S-shaped curve):**

- **Axes:** horizontal = input x (−∞ to +∞), vertical = output (0 to 1).
- As x → −∞, the curve flattens toward **0**; as x → +∞, it flattens toward **1**.
- It passes through **(0, 0.5)** — the midpoint.
- Steepest in the middle (|x| < 2); nearly flat (saturated) for |x| > 4.
- Its derivative is σ(x)·(1 − σ(x)), maximum 0.25 at x = 0.

**Use:** output layer of **binary classification** (output reads as P(class = 1)).

---

## Q2. Advantages and disadvantages of Sigmoid.

**Advantages:**

- Output in (0, 1) → natural **probability interpretation** for binary classification.
- **Smooth and differentiable** everywhere — gradient-based learning works.
- Historically the standard activation; simple to understand.

**Disadvantages:**

- **Vanishing gradient:** derivative ≤ 0.25, and ≈ 0 in saturated regions — in deep networks gradients shrink exponentially layer by layer, stalling learning.
- **Not zero-centered:** outputs are always positive, so gradients for a neuron's weights all share the same sign → zig-zag, inefficient updates.
- **Expensive:** computing e^(−x) costs more than simpler functions like ReLU.

(Because of these, sigmoid is now rarely used in hidden layers — ReLU replaced it.)

---

## Q3. Explain Tanh activation function.

The **hyperbolic tangent** squashes inputs into **(−1, +1)**:

```
tanh(x) = (e^x − e^(−x)) / (e^x + e^(−x))  =  2·σ(2x) − 1
```

**Graph description:**

- Same S-shape as sigmoid but **vertically stretched and centered at zero**: passes through **(0, 0)**, flattens toward −1 (left) and +1 (right).
- Steeper than sigmoid around zero (derivative max = 1 at x = 0 vs 0.25 for sigmoid).
- **Zero-centered output** (−1 to 1) → fixes sigmoid's zig-zag update problem, so it generally trains faster than sigmoid in hidden layers.
- Still suffers from **vanishing gradients** when saturated (|x| large), and still needs expensive exponentials.

**Classic use:** hidden layers of RNNs/LSTMs (gates use sigmoid, cell-state updates use tanh).

---

## Q4. Differentiate Sigmoid and Tanh.

| Aspect | Sigmoid σ(x) = 1/(1+e^(−x)) | Tanh |
|---|---|---|
| Output range | **(0, 1)** | **(−1, +1)** |
| Zero-centered? | **No** — always positive | **Yes** |
| Value at x = 0 | 0.5 | 0 |
| Max derivative | 0.25 (at x = 0) | 1.0 (at x = 0) |
| Gradient flow | Weaker, zig-zag updates | Stronger near zero, cleaner updates |
| Vanishing gradient | Yes (saturates) | Yes (saturates) |
| Typical use | **Binary-classification output** | **Hidden layers** (esp. RNNs) |

**Memory hook:** tanh is just a scaled, zero-centered sigmoid: tanh(x) = 2σ(2x) − 1.

---

## Q5. Explain ReLU activation function with graph. f(x) = max(0, x)

**ReLU (Rectified Linear Unit)** is the simplest non-linearity:

```
f(x) = max(0, x)   i.e.  x if x > 0, else 0
```

**Graph description:**

- **Axes:** horizontal = input x, vertical = output.
- For all **x < 0**: the graph is **flat along the x-axis** (output = 0).
- For all **x ≥ 0**: the graph is a **45° straight line** through the origin (output = x).
- It looks like a "hockey stick" with the bend exactly at (0, 0).
- Derivative: 1 for x > 0, 0 for x < 0 (undefined at exactly 0 — treated as 0 in practice).

---

## Q6. Why is ReLU commonly used in hidden layers?

1. **No vanishing gradient for positive inputs** — derivative is exactly 1 for all x > 0 (unlike sigmoid's ≤ 0.25), so gradients flow undiminished through deep networks.
2. **Computationally trivial** — just a max(0, x) comparison; no exponentials → much faster training than sigmoid/tanh.
3. **Sparsity** — negative inputs output exactly 0, so many neurons are "off"; sparse representations are efficient and often generalize better.
4. **Faster convergence** — empirically, ReLU networks train several times faster than sigmoid/tanh networks.
5. **Simple and effective** — despite its simplicity it is the default choice for hidden layers in CNNs and MLPs.

**Caveat (dying ReLU):** a neuron stuck with negative input forever outputs 0 and stops learning; variants like **Leaky ReLU** (f(x) = 0.01x for x < 0) fix this.

---

## Q7. What is Softmax activation function?

**Softmax** converts a vector of raw scores (logits) into a **probability distribution** over classes:

```
softmax(zi) = e^(zi) / Σj e^(zj)
```

- Each output is in (0, 1), and **all outputs sum to exactly 1**.
- It **amplifies differences**: the largest logit gets the dominant share of probability.
- Unlike sigmoid (which treats each output independently), softmax outputs **compete** — raising one class's probability lowers the others'.

**Example:** logits [2.0, 1.0, 0.1] → softmax ≈ [0.66, 0.24, 0.10] → predicted class 0 with 66% confidence.

---

## Q8. Why is Softmax used in multiclass classification?

1. **Valid probabilities** — outputs sum to 1 and lie in (0, 1), so they read directly as class probabilities / confidence scores.
2. **Mutually exclusive classes** — multiclass problems assume each input belongs to exactly one class; softmax enforces this competition, unlike independent sigmoids.
3. **Pairs with cross-entropy loss** — the softmax + cross-entropy combination has a beautifully simple gradient (prediction − target), making training stable and efficient.
4. **Clear decision rule** — pick the class with the highest probability (argmax).

---

## Q9. Which activation function is commonly used for binary classification output layer?

**Sigmoid.** A single output neuron with σ(z) gives P(class = 1) ∈ (0, 1); classify as class 1 if output ≥ 0.5, else class 0. Trained with **binary cross-entropy** loss.

---

## Q10. Which activation function is used for multiclass output layer?

**Softmax,** with one output neuron per class. It produces a probability distribution over all classes; the predicted class is the one with maximum probability. Trained with **categorical cross-entropy** loss.

**Quick reference:**

| Task | Output neurons | Activation | Loss |
|---|---|---|---|
| Binary classification | 1 | Sigmoid | Binary cross-entropy |
| Multiclass classification | one per class | Softmax | Categorical cross-entropy |
| Regression | 1 | Linear (none) | MSE |
