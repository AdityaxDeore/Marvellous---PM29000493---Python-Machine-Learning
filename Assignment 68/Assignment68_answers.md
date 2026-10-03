# Assignment 68 (RNN conceptual variant) — Answers (RNN Concepts)

## Q1. Explain the concept of Recurrent Neural Network. Describe why RNN is more suitable than traditional neural networks for sequential data.

**Concept of RNN:** A Recurrent Neural Network is a neural network with **loops**: the output of the hidden layer at one time step is fed back as input to itself at the next time step. Formally:

```
hₜ = tanh( Wₓ xₜ + Wₕ hₜ₋₁ + b )
```

The hidden state hₜ acts as a **memory** that carries information from earlier steps forward, so the network processes a sequence one element at a time while retaining context. The same weights are reused at every time step (parameter sharing), so the model works for sequences of any length.

**Why more suitable than traditional networks for sequential data:**

- **Traditional networks (FNNs)** take a fixed-size input and have no memory — each input is processed independently, so earlier elements cannot influence later ones. The order of inputs does not matter to them.
- **RNNs process order explicitly:** because hₜ depends on hₜ₋₁, the sequence order changes the result — essential for language, time series, and audio.
- **Variable-length handling:** an RNN unrolls over however many steps the sequence has; an FNN would need a separate fixed input size for each possible length.
- Example: "not good" vs "good not" are different inputs to an RNN (different hidden-state trajectories) but indistinguishable to a bag-of-words feedforward model.

## Q2. Differentiate between ANN, FNN, CNN, and RNN in terms of architecture and practical applications.

| Aspect | ANN (Artificial Neural Network) | FNN (Feedforward Neural Network) | CNN (Convolutional Neural Network) | RNN (Recurrent Neural Network) |
|--------|---------------------------------|----------------------------------|------------------------------------|--------------------------------|
| Architecture | General term for networks of artificial neurons; includes FNNs, CNNs, RNNs | Information flows one direction: input → hidden layers → output; no cycles | Uses convolutional filters (kernels), pooling layers; weight sharing over space | Has recurrent loops: hidden state feeds back into itself across time steps; weight sharing over time |
| Data type | Any | Fixed-size feature vectors | Grid-structured data: images, video | Sequential data: text, time series, audio |
| Memory of order | Depends on type | None — inputs are independent | Captures local spatial structure, not sequence | Has memory (hidden state) across steps |
| Typical applications | Umbrella term | Tabular prediction: loan approval, churn prediction | Image classification, object detection, medical image analysis | Sentiment analysis, machine translation, speech recognition, stock prediction |

Note: FNN is the *simplest form* of ANN. CNN and RNN are specialized ANN architectures — CNNs for spatial structure, RNNs for temporal structure.

## Q3. Explain the meaning of sequence data. Mention examples where sequence order is important.

**Sequence data** is data in which the **order of elements carries meaning** — rearranging the elements changes or destroys the information.

- The elements are indexed by position (time step 1, 2, 3, …), and the model must respect that order.

**Examples where order is important:**

- **Natural language:** "The dog bit the man" vs "The man bit the dog" — same words, opposite meanings.
- **Negation:** "The food was not good" vs "The food was good" — "not" must precede "good" to flip the sentiment.
- **Time series:** stock prices over days — tomorrow's price depends on the sequence of past prices in chronological order; shuffling destroys the trend.
- **Speech/audio:** phonemes must occur in the right order to form recognizable words ("act" vs "cat").
- **Video:** frames in order form an action; reversed frames show the action backwards.
- **DNA/protein sequences:** the order of nucleotides or amino acids determines biological function.

## Q4. Describe the architecture of a basic RNN model. Explain input layer, hidden state, recurrent connection, output layer, and activation functions.

**Architecture of a basic (Elman) RNN:**

```
        ┌─────────────────────────────────┐
        │        recurrent connection      │
        ▼                                 │
xₜ ──► [ Wₓ ] ──► (+) ──► [ tanh ] ──► hₜ ─┤
                  ▲                       │
                  b (bias)                │
                                          │
hₜ ──► [ Wᵧ ] ──► (+) ──► [ σ / softmax ] ──► yₜ
```

(One time step shown; the box unfolds into a chain h₁ → h₂ → … → h_T over time.)

- **Input layer:** Receives the input xₜ at each time step — e.g., the word embedding of the t-th word, or the t-th measurement of a time series. It does not compute anything; it passes xₜ to the hidden layer.
- **Hidden state:** The core of the RNN — a vector hₜ computed as `hₜ = tanh(Wₓxₜ + Wₕhₜ₋₁ + b)`. It is both the layer's output to the next time step and its memory of everything seen so far.
- **Recurrent connection:** The link that feeds hₜ₋₁ (previous hidden state) back into the current computation through the recurrent weight matrix Wₕ. This loop, unrolled over time, is what gives the RNN memory. Weights are shared across all time steps.
- **Output layer:** Produces the prediction. At each step (or just at the final step) it maps the hidden state through weights Wᵧ and an output activation: yₜ = activation(Wᵧhₜ + bᵧ).
- **Activation functions:**
  - **tanh** in the hidden layer: bounds the state to (−1, 1), keeping values stable across many recurrent steps; zero-centered for better gradient flow.
  - **sigmoid** in the output layer: for binary tasks (e.g., positive/negative sentiment), maps output to a (0, 1) probability.
  - **softmax** in the output layer: for multi-class tasks (e.g., next-word prediction over a vocabulary), produces a probability distribution over classes.

## Q5. Explain why memory is important in RNN models.

- **Context is what makes sequences meaningful:** the correct interpretation of an element depends on earlier elements. Memory (the hidden state) is the only mechanism that carries earlier information to later steps.
- **Resolves ambiguity:** In "The food was not good", the word "good" is positive in isolation but negative in context. Only a model that remembers "not" from step 3 can interpret "good" correctly at step 4.
- **Captures long-range dependencies:** Pronouns ("it", "they"), names, and tenses refer back to earlier words; without memory, each word would be judged in isolation and the model would lose the thread.
- **Distinguishes order:** Memory makes hₜ order-dependent, so "not good" and "good not" produce different states — a memoryless model cannot tell them apart.
- **Limitation:** In a basic RNN, memory degrades over long sequences (vanishing gradient), which is why LSTM and GRU introduce gated memory cells — but the *principle* remains the same: sequence understanding requires remembering the past.
