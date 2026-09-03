# Marvellous Infosystems — Deep Learning Assignment 58
## Forward/Backward Propagation, Learning Rate & the Perceptron

---

## Q1. Explain weighted sum in neural networks.

The **weighted sum** is the first computation inside every neuron: each input is multiplied by its connection weight, and the products are summed together with the bias:

```
z = w1·x1 + w2·x2 + … + wn·xn + b
```

- **xi** — input values (features or outputs of the previous layer).
- **wi** — weights; control how strongly each input influences the neuron.
- **b** — bias; shifts the sum independently of the inputs.

**Example:** inputs x = [2, 3], weights w = [0.4, 0.6], bias b = 0.5:
z = 0.4×2 + 0.6×3 + 0.5 = 0.8 + 1.8 + 0.5 = **3.1**

The weighted sum is then passed through an activation function to produce the neuron's output. It is the "voting" step — every input votes, and its weight decides how loud the vote is.

---

## Q2. What is forward propagation? Explain step by step.

**Forward propagation** is the process of passing input data through the network, layer by layer, to produce a prediction. Steps:

1. **Input layer** — present the feature vector x = [x1, x2, …, xn].
2. **For each hidden layer (in order):**
a. Compute the weighted sum for every neuron: `z = W·a_prev + b`
b. Apply the activation function: `a = f(z)`
c. Pass `a` as input to the next layer.
3. **Output layer** — compute its weighted sum and apply the output activation (e.g. sigmoid for binary, softmax for multiclass) to get the prediction ŷ.
4. **Compute loss** — compare ŷ with the true label y using the loss function.

Information flows strictly **forward** (input → hidden → output); no cycles. Forward propagation is also all that happens at **inference time** — backpropagation is only used during training.

---

## Q3. What is backpropagation? Why is it important?

**Backpropagation** is the algorithm that trains neural networks: it computes the **gradient of the loss with respect to every weight** by applying the **chain rule of calculus backwards** through the network (output → hidden → input), and then each weight is updated to reduce the loss.

How it works (one training step):

1. Forward pass → prediction ŷ and loss L.
2. Compute ∂L/∂(output) — how the loss changes with the output.
3. Propagate backwards layer by layer: for each weight, `∂L/∂w = ∂L/∂z × ∂z/∂w`, reusing already-computed terms (this reuse is what makes it efficient).
4. Update: `w ← w − η × ∂L/∂w` (η = learning rate).

**Why important:**

- It is the **only practical way to train deep networks** — computing gradients naively per weight would be impossibly slow; backpropagation computes all gradients in roughly the cost of one forward pass.
- Without it, multi-layer networks could not learn — it is the engine behind all of modern deep learning.

---

## Q4. What is learning rate? What happens if it is too high or too low?

The **learning rate (η)** is the hyperparameter that controls **how big a step** the optimizer takes when updating weights:

```
w_new = w_old − η × gradient
```

| Learning rate | Effect |
|---|---|
| **Too high** | Steps overshoot the minimum — loss oscillates or **diverges** (explodes to NaN); the model never converges |
| **Too low** | Steps are tiny — training is painfully **slow**, wastes compute, and can get stuck in a poor local minimum or saddle point |
| **Just right** | Loss decreases steadily and converges to a good minimum |

**Intuition:** descending a mountain in fog — too large a stride and you leap over the valley and fall off a cliff; too small and you crawl. In practice, values like 0.001–0.01 with the Adam optimizer work well, and learning-rate schedules reduce η as training progresses.

---

## Q5. What is Perceptron? Explain its history and inventor.

The **Perceptron** is the simplest artificial neuron — a single-layer binary classifier that computes a weighted sum of inputs, adds a bias, and passes the result through a **step (threshold) activation function**.

**History:**

- **1943** — McCulloch & Pitts propose the first mathematical model of a neuron.
- **1958** — **Frank Rosenblatt** (Cornell Aeronautical Laboratory) invents the **Perceptron** and builds the **Mark I Perceptron** machine for image recognition — one of the first machines that could "learn".
- Rosenblatt also gave it a learning rule (the perceptron learning algorithm) that provably converges if the data is linearly separable.
- **1969** — Minsky & Papert publish *Perceptrons*, proving a single-layer perceptron **cannot solve non-linear problems like XOR** — this triggered the first "AI winter" for neural networks.
- **1980s** — backpropagation revives the field by enabling **multi-layer** perceptrons (MLPs) that overcome the XOR limitation.

The perceptron is the historical and conceptual ancestor of every modern neural network.

---

## Q6. Explain the structure of a Perceptron: inputs, weights, bias, output.

A perceptron has exactly four structural elements:

1. **Inputs (x1, x2, …, xn)** — the feature values fed into the model (e.g. pixel values, measurements).
2. **Weights (w1, w2, …, wn)** — one learnable number per input; decides each input's influence. Initialized randomly, updated by the perceptron learning rule.
3. **Bias (b)** — a learnable threshold-shifter added to the weighted sum; lets the decision boundary move away from the origin.
4. **Output (y)** — a single binary value, 0 or 1, produced by the step activation:
`y = 1 if (Σwi·xi + b) ≥ 0 else 0`

There are **no hidden layers** — inputs connect directly to the single output neuron. Because of this, a perceptron can only learn **linearly separable** decision boundaries (a straight line/plane).

---

## Q7. Draw and explain the Perceptron model.

```
w1
x1 ──────┐
▼
x2 ──────┼──▶ ──▶ z = Σwi·xi + b ──▶ ──▶ y ∈ {0, 1}
▲ ▲
x3 ──────┘ │
b (bias)
wn
xn ──────┘
```

**Explanation of the flow:**

1. Each input xi travels along a connection carrying weight wi.
2. The **summation unit (Σ)** computes the weighted sum plus bias: `z = w1·x1 + … + wn·xn + b`.
3. The **step activation function** thresholds z: outputs **1** if z ≥ 0 (neuron "fires"), else **0**.
4. During training, if the prediction is wrong, weights are nudged: `wi ← wi + η·(target − prediction)·xi` — the perceptron learning rule.

---

## Q8. Explain the perceptron formula y = f(w1·x1 + w2·x2 + … + b).

Breaking the formula into its three parts:

- **w1·x1 + w2·x2 + … (weighted sum)** — each input's contribution, scaled by its learned importance. This is the neuron's "evidence gathering".
- **+ b (bias)** — shifts the total; sets the firing threshold independently of inputs. Without it the separating line would be forced through the origin.
- **f(…) (activation function)** — the decision step. In the classic perceptron, `f` is the **step function**: f(z) = 1 if z ≥ 0, else 0. It converts the continuous sum into a crisp binary decision.

**Worked example:** x = [1, 0], w = [0.5, −0.6], b = 0.2:
z = 0.5×1 + (−0.6)×0 + 0.2 = 0.7 → f(0.7) = 1 → perceptron outputs class 1.

---

## Q9. What is the activation function in a Perceptron?

The classic perceptron uses the **step function (Heaviside step / threshold function)**:

```
f(z) = 1 if z ≥ 0
f(z) = 0 if z < 0
```

- It converts the continuous weighted sum into a **binary decision** — the neuron either fires (1) or stays silent (0), mimicking a biological neuron's all-or-nothing firing.
- **Limitation:** the step function is flat almost everywhere (derivative = 0), so **gradient-based learning is impossible** — this is why the perceptron uses its own special learning rule instead of backpropagation.
- Modern multi-layer networks replace it with **differentiable** activations (sigmoid, tanh, ReLU) precisely so that backpropagation can compute gradients through them.

---

## Q10. Differentiate Single Layer vs Multi Layer Perceptron.

| Aspect | Single Layer Perceptron (SLP) | Multi Layer Perceptron (MLP) |
|---|---|---|
| Hidden layers | **None** — inputs connect directly to output | **One or more** hidden layers between input and output |
| Activation | Step function (non-differentiable) | Sigmoid / tanh / ReLU (differentiable) |
| Training | Perceptron learning rule | **Backpropagation** + gradient descent |
| Decision boundary | Only **linear** (line/plane) | **Non-linear** — can carve complex boundaries |
| XOR problem | **Cannot** solve (Minsky & Papert, 1969) | **Can** solve — the classic motivation for hidden layers |
| Example use | AND / OR gates | Digit recognition, tabular classification, regression |
| Relation to DL | Historical building block | The original "deep" network — an MLP with 2+ hidden layers is deep learning |
