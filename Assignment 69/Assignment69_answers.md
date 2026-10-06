# Assignment 69 — Answers (RNN Theory)

## Q1. Explain hidden state in RNN. Describe how hidden state stores previous information.

The **hidden state (hₜ)** is a fixed-length vector produced at each time step of an RNN that carries a summary of all information seen so far in the sequence.

- It acts as the **memory** of the network: at time step *t*, hₜ is computed from the current input xₜ **and** the previous hidden state hₜ₋₁.
- Because each new hidden state is a function of the previous one, information from earlier steps is **recursively folded** into the vector: h₁ → h₂ → h₃ … hₜ.
- The final hidden state h_T therefore represents the entire sequence in one vector, which can be fed to an output layer for classification (e.g., sentiment of a sentence).
- How it stores previous information: the recurrence hₜ = f(Wₓxₜ + Wₕhₜ₋₁ + b) mixes the old memory (hₜ₋₁) with new evidence (xₜ) through learned weights, so old context is retained but gradually updated or overwritten by later inputs.

## Q2. Explain how an RNN reads the sentence word by word using time steps. Example: "food was not good"

An RNN processes a sequence **one element per time step**, in order:

- **t = 1:** Input x₁ = embedding("food"). Hidden state h₁ = f(x₁, h₀), where h₀ is an initial zero vector. h₁ now summarizes "food".
- **t = 2:** Input x₂ = embedding("was"). h₂ = f(x₂, h₁). h₂ summarizes "food was".
- **t = 3:** Input x₃ = embedding("not"). h₃ = f(x₃, h₂). h₃ summarizes "food was not".
- **t = 4:** Input x₄ = embedding("good"). h₄ = f(x₄, h₃). h₄ summarizes the full sentence "food was not good".

Key points:

- The RNN **unrolls in time**: the same weights are reused at every step, so the model works for any sentence length.
- The word "not" at t = 3 modifies how "good" is interpreted at t = 4 — this is why order matters: the hidden state arriving at "good" already carries the negation, allowing the model to predict negative sentiment.

## Q3. Write the mathematical formula of SimpleRNN hidden state calculation and explain every term. hₜ = tanh(Wₓ xₜ + Wₕ hₜ₋₁ + b)

**Formula:**

```
hₜ = tanh( Wₓ xₜ + Wₕ hₜ₋₁ + b )
```

Term-by-term explanation:

- **hₜ** — hidden state at current time step *t*; the network's memory vector summarizing the sequence up to *t*.
- **tanh(·)** — hyperbolic tangent activation function; squashes values to (−1, 1) and introduces non-linearity so the network can learn complex patterns.
- **xₜ** — input vector at time step *t* (e.g., the embedding of the t-th word).
- **Wₓ** — weight matrix for the **input**; transforms the current input xₜ into the hidden space.
- **hₜ₋₁** — hidden state from the **previous** time step; carries all prior context.
- **Wₕ** — weight matrix for the **previous hidden state** (recurrent weights); this matrix is what enables memory across steps.
- **b** — bias vector; shifts the activation independently of inputs, improving flexibility of the transformation.

In words: the new memory = non-linear mix of *what is being read now* (Wₓxₜ) and *what was remembered before* (Wₕhₜ₋₁), plus a bias.

## Q4. Explain the role of input vector, previous hidden state, weights, and bias in RNN.

- **Input vector (xₜ):** Brings in *new evidence* at the current time step — e.g., the embedding of the current word. Without it, the network would have nothing new to react to.
- **Previous hidden state (hₜ₋₁):** Provides the *context* from all earlier steps. It is the only channel through which past information reaches the current step.
- **Weights (Wₓ and Wₕ):**
  - **Wₓ** decides how much importance the *current input* gets.
  - **Wₕ** decides how much *old memory* is preserved versus overwritten.
  - Both are **learned during training** (via backpropagation through time) and **shared across all time steps**, which keeps the parameter count fixed regardless of sequence length.
- **Bias (b):** An additive offset that lets the layer shift its output even when inputs are zero, giving the model flexibility to fit the data.

## Q5. Explain why sequence order matters in RNN models.

- RNNs process inputs **in the given order**, and the hidden state evolves differently depending on that order, because hₜ depends on hₜ₋₁.
- Example: "food was **not good**" vs "food was **good**, not" — or "**not good**" vs "**good not**": the same words in different orders produce different hidden-state trajectories and hence different outputs.
- Meaning depends on position: "not" must appear *before* "good" to negate it. An RNN captures this because the memory reaching "good" already contains "not" in the first sentence but not in a reordered one.
- Models that ignore order (e.g., bag-of-words averages) cannot distinguish "not good" from "good" — the RNN's recurrence is what makes order informative.

## Q6. Explain why tanh is commonly used in SimpleRNN layers.

- **Bounded output (−1, 1):** The hidden state values stay in a stable range. Without bounding, repeated addition of Wₕhₜ₋₁ across many steps could make activations explode; tanh prevents this.
- **Zero-centered:** tanh outputs are centered at 0 (unlike sigmoid, which is centered at 0.5). Zero-centered activations let gradients flow more easily during backpropagation through time.
- **Non-linear:** tanh introduces non-linearity, without which stacking steps would collapse to a single linear transformation.
- **Preserves sign:** Values can be negative or positive, allowing the hidden state to represent opposing influences (e.g., a positive sentiment being cancelled by a negation).

Note: tanh does *not* fix the vanishing gradient problem completely — for long sequences, LSTM/GRU are used — but it is stable enough for short-to-medium sequences and is the default in SimpleRNN.

## Q7. Calculate tanh output for the following values: [-2, -1, 0, 1, 2]

Formula: **tanh(x) = (eˣ − e⁻ˣ) / (eˣ + e⁻ˣ)**. tanh is an odd function: tanh(−x) = −tanh(x).

| x    | eˣ     | e⁻ˣ    | tanh(x) = (eˣ − e⁻ˣ) / (eˣ + e⁻ˣ) | Result  |
|------|--------|--------|-----------------------------------|---------|
| −2   | 0.1353 | 7.3891 | (0.1353 − 7.3891)/(0.1353 + 7.3891) = −7.2538/7.5244 | **−0.9640** |
| −1   | 0.3679 | 2.7183 | (0.3679 − 2.7183)/(0.3679 + 2.7183) = −2.3504/3.0862 | **−0.7616** |
| 0    | 1.0000 | 1.0000 | (1 − 1)/(1 + 1) = 0/2 | **0.0000** |
| 1    | 2.7183 | 0.3679 | (2.7183 − 0.3679)/(2.7183 + 0.3679) = 2.3504/3.0862 | **0.7616** |
| 2    | 7.3891 | 0.1353 | (7.3891 − 0.1353)/(7.3891 + 0.1353) = 7.2538/7.5244 | **0.9640** |

Summary: **tanh([-2, -1, 0, 1, 2]) ≈ [-0.9640, -0.7616, 0, 0.7616, 0.9640]**

## Q8. Explain why sigmoid is used in the output layer for binary sentiment analysis.

- Binary sentiment analysis has exactly two outcomes: **positive (1)** or **negative (0)**.
- The **sigmoid function, σ(x) = 1 / (1 + e⁻ˣ)**, maps any real number to the range **(0, 1)**.
- This output is directly interpretable as the **probability that the sentiment is positive**:
  - Output near 1 → strongly positive; near 0 → strongly negative; 0.5 → uncertain.
- It pairs with the **binary cross-entropy loss**, the standard loss for binary classification, which is designed to work with probability outputs.
- Contrast with tanh: tanh outputs (−1, 1), which is not a probability range, so sigmoid — not tanh — is the correct choice for the final binary prediction layer.
