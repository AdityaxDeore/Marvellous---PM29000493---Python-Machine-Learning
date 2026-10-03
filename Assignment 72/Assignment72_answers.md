# Marvellous Infosystems — Deep Learning Assignment 72 (RNN & LSTM)

## Q1. Explain the basic architecture of RNN with diagram.

An RNN is a neural network designed for sequential data. Unlike a feedforward network, it has a **recurrent connection** that loops the hidden state from one time step back into the network at the next time step, letting the network process one element of a sequence at a time while carrying context forward.

### Components

- **Input layer** — receives one element xₜ of the sequence at time step t (e.g. one word embedding of a sentence).
- **Hidden state (hₜ)** — the "memory" of the network. At each step it is computed from the current input **and** the previous hidden state hₜ₋₁.
- **Recurrent connection** — the weight matrix Wₕₕ that feeds hₜ₋₁ into the computation of hₜ. This is the defining feature: the same weights are shared across all time steps.
- **Output layer** — produces one output yₜ per time step from the hidden state (many-to-many), or a single output from the final hidden state (many-to-one).

### Forward equations

```
hₜ = tanh(Wₓₕ · xₜ + Wₕₕ · hₜ₋₁ + bₕ)
yₜ = softmax(Wₕᵧ · hₜ + bᵧ)        (for classification)
```

### Unfolded architecture (across time steps)

```
         y₁            y₂            y₃
          ↑             ↑             ↑
     ┌────────┐  ┌────────┐  ┌────────┐
     │  Wₕᵧ   │  │  Wₕᵧ   │  │  Wₕᵧ   │
     └────────┘  └────────┘  └────────┘
          ↑             ↑             ↑
         h₁            h₂            h₃        ← hidden states
          ↑             ↑             ↑
     ┌────────┐  ┌────────┐  ┌────────┐
     │  tanh  │  │  tanh  │  │  tanh  │
     └────────┘  └────────┘  └────────┘
          ↑             ↑             ↑
          x₁            x₂            x₃        ← inputs at each time step
               ↘─────↗       ↘─────↗
                  Wₕₕ            Wₕₕ
          recurrent connections (same weights, shared across steps)
```

### Flow of information

1. x₁ arrives; h₁ = tanh(Wₓₕx₁ + Wₕₕh₀ + bₕ), where h₀ is usually a zero vector.
2. h₁ is passed forward (to compute y₁) and *backward in time* (as input to step 2).
3. At step 2: h₂ = tanh(Wₓₕx₂ + Wₕₕh₁ + bₕ) — so h₂ contains information from **both** x₁ and x₂.
4. This repeats until the final step; the last hidden state encodes the entire sequence.

---

## Q2. Why do we use RNN instead of traditional neural networks for sequential data?

Traditional networks (feedforward MLP, CNN) make two assumptions that break for sequential data:

1. **Fixed-size input** — an MLP needs every input at once and a fixed dimension; a sentence of 5 words vs 15 words cannot be fed to the same MLP without padding/truncation hacks.
2. **Independence of inputs** — each example is treated as unrelated to the others. Word order carries the meaning ("dog bites man" ≠ "man bites dog"), but an MLP fed a bag of word vectors cannot tell the difference.

**Why RNN works instead:**

- **Weight sharing across time** — one set of weights handles any sequence length; the model generalizes across positions.
- **Order-aware processing** — elements are processed in sequence, so order is inherently encoded.
- **Variable-length input/output** — handles many-to-one, one-to-many, and many-to-many mappings.

### Examples

- **Sentence processing (sentiment analysis):** The sentence "The movie was not great, actually it was terrible" — an MLP sees all words simultaneously and the negation "not" gets averaged away. An RNN reads word-by-word, updating its hidden state so that "not" modifies the meaning of everything after it.
- **Time-series prediction (stock prices):** Prices are a temporal sequence where xₜ depends on xₜ₋₁, xₜ₋₂, ... An MLP treats yesterday's and today's prices as unrelated features; an RNN naturally models the time dependency and can forecast xₜ₊₁ from the history.

---

## Q3. Explain how the hidden state works in RNN. How does previous information get transferred to the next step?

The hidden state hₜ is a fixed-size vector that acts as the network's running summary of everything seen so far in the sequence.

**The update mechanism:**

```
hₜ = tanh(Wₓₕ · xₜ + Wₕₕ · hₜ₋₁ + bₕ)
```

Two contributions combine at each step:

1. **Current input term (Wₓₕ · xₜ)** — new information from the present element.
2. **Recurrent term (Wₕₕ · hₜ₋₁)** — the previous hidden state, multiplied by the recurrent weight matrix Wₕₕ, then added.

Because hₜ is a function of hₜ₋₁, and hₜ₋₁ was a function of hₜ₋₂, **every hidden state implicitly contains traces of all previous inputs**. This is the transfer mechanism: the recurrent weight matrix Wₕₕ routes old information forward.

**Walkthrough:** For the sentence "I love this movie":

- h₁ = f(x("I"), h₀) — encodes "I".
- h₂ = f(x("love"), h₁) — encodes "I" + "love".
- h₃ = f(x("this"), h₂), h₄ = f(x("movie"), h₃) — h₄ encodes the whole sentence.

The final hidden state h₄ is what a classifier uses for sentiment prediction (many-to-one). Note the bottleneck: hₜ is fixed-size, so long sequences get compressed — early information decays, which is exactly the vanishing gradient problem (Q5) that LSTM (Q9) fixes.

---

## Q4. What is meant by "memory" in RNN? How does RNN remember previous inputs?

**"Memory" in an RNN = the hidden state vector hₜ.** It is not a separate memory bank; it is the activation of the hidden layer that persists and is carried across time steps.

**How previous inputs are remembered:**

1. At step t, the network computes hₜ from (xₜ, hₜ₋₁). The old hidden state hₜ₋₁ is multiplied by the recurrent matrix Wₕₕ and mixed into the new state.
2. Unfolding the recurrence: hₜ depends on hₜ₋₁, which depends on hₜ₋₂, ..., which depends on x₁. So x₁ influences hₜ through t−1 repeated applications of Wₕₕ and tanh.
3. The output at any step, yₜ = g(Wₕᵧhₜ + bᵧ), therefore depends on the current and all past inputs.

**Key limitation:** this memory is **short-term and lossy**. Each time step applies tanh (squashes values to (−1, 1)) and multiplies by Wₕₕ. Information from many steps back is attenuated — like a message passed through many noisy copies. Empirically, plain RNNs only "remember" ~5–10 steps back reliably. The hidden state is also a single fixed-size vector forced to compress arbitrarily long history — an information bottleneck. LSTMs solve both problems by adding an explicit, gated cell state (Q9–Q12).

---

## Q5. Explain the Vanishing Gradient Problem in RNN. Why does it occur? What problems does it create during training?

**The problem:** During training, gradients become exponentially small as they are backpropagated through many time steps, so the network stops learning long-range dependencies — earlier layers (which handle distant past inputs) barely update.

**Why it occurs (mechanism):**

Training uses **Backpropagation Through Time (BPTT)**: the network is unfolded across T steps and treated like a T-layer feedforward net. The gradient of the loss w.r.t. an early hidden state involves a long product of Jacobians:

```
∂L/∂h₁ = ∂L/∂hₜ · Π (∂hₖ/∂hₖ₋₁)   for k = 2..t
∂hₖ/∂hₖ₋₁ = diag(tanh′(·)) · Wₕₕ
```

Two facts combine:

1. **tanh′ ≤ 1** (derivative of tanh is at most 1, and usually much less than 1 in saturated regions).
2. If the largest singular value of Wₕₕ is < 1, each multiplication shrinks the gradient.

So the gradient gets multiplied by a factor < 1 at **every time step** — over 50–100 steps it collapses toward zero (exponential decay). (The symmetric case — Wₕₕ's eigenvalues > 1 — causes the **exploding gradient**, usually tamed with gradient clipping.)

**Consequences during training:**

- The network can only learn dependencies within a short window (~5–10 steps); distant context is effectively ignored.
- Example: in "The keys to the old wooden cabinet … are on the table", an RNN cannot learn the plural agreement between "keys" and "are" because the gradient from "are" never reaches "keys".
- Training stalls: early time-step weights receive near-zero updates, so the model behaves as if it has no memory of the distant past.

---

## Q6. Differentiate between Feed Forward Neural Network and CNN.

| Aspect | Feed Forward Neural Network (MLP) | Convolutional Neural Network (CNN) |
|---|---|---|
| **Data handling** | Takes a fixed-size 1-D vector; each input feature is independent. Flattening an image destroys spatial structure. | Takes grid-structured data (images, spectrograms). Convolutional filters preserve spatial locality and share weights across positions. |
| **Connectivity** | Fully connected layers — every neuron connects to every neuron in the next layer; parameter count explodes with input size. | Sparse connectivity (local receptive fields) + weight sharing; far fewer parameters for image-sized inputs. |
| **Invariance** | None built in — a shifted input looks like a completely new input. | Translation invariance via convolution + pooling: a cat detected anywhere in the image. |
| **Use cases** | Tabular data, simple classification/regression, function approximation where features are independent. | Image classification (ResNet), object detection (YOLO), image segmentation, any task with spatial/local structure. |
| **Sequence data** | Cannot model order or variable length. | 1-D CNNs can model local patterns in sequences, but have a fixed receptive field, not true recurrence. |

---

## Q8. Give real-world applications of RNN (at least 5, with technical details).

1. **Machine translation (seq2seq)** — Encoder RNN reads the source sentence into a final hidden state (context vector); decoder RNN generates the target sentence one token at a time, conditioned on that context and its own previous output. Attention later replaced the single context vector, but the RNN backbone defined the architecture.

2. **Speech recognition** — Audio is a sequence of acoustic frames (e.g. MFCC features every 10 ms). An RNN (often bidirectional LSTM) maps the frame sequence to phoneme/character probabilities per frame; **CTC loss** aligns the unsegmented audio to the transcript without frame-level labels.

3. **Language modelling / text generation** — Trained many-to-many: given tokens w₁..wₜ, predict wₜ₊₁ (cross-entropy loss). The trained model generates text autoregressively — feed its own prediction back as the next input. This is the principle behind all modern generative text models (transformers replaced RNNs, but the task formulation is identical).

4. **Time-series forecasting (energy demand, weather)** — Past sensor readings form the input sequence; the RNN's final hidden state feeds a regression head predicting the next value(s). LSTM variants dominate here because demand/weather patterns span days to seasons — long-term dependencies plain RNNs cannot hold.

5. **Sentiment analysis** — Many-to-one: the RNN consumes the review token-by-token; the final hidden state passes through a dense + softmax layer to output positive/negative. Bidirectional RNNs read both directions so each word's representation includes left and right context.

6. **Video activity recognition** — A CNN extracts per-frame features; an RNN over the frame sequence models temporal dynamics (e.g. distinguishing "sitting down" from "standing up", which look identical in a single frame).

---

## Q9. Why was LSTM introduced? What limitations of RNN does it solve?

LSTM (Long Short-Term Memory, Hochreiter & Schmidhuber, 1997) was introduced because plain RNNs **cannot learn long-term dependencies** — the vanishing gradient problem (Q5) makes information from more than ~10 steps back unreachable during training.

**Limitations of RNN that LSTM solves:**

1. **Vanishing gradients / short memory** — In an RNN, memory must survive repeated tanh squashing and multiplication by Wₕₕ at every step. LSTM adds a separate **cell state Cₜ** that flows down the time axis with only element-wise operations (no repeated matrix multiplication or squashing), so gradients flow back largely unchanged — the "constant error carousel".

2. **Information bottleneck** — An RNN forces all history through one hidden vector that is overwritten every step. LSTM's cell state is explicitly *added to* rather than overwritten, and **gates** decide what to keep, add, or discard.

3. **No selective forgetting** — An RNN cannot deliberately drop irrelevant old information; it decays everything uniformly. The **forget gate** lets the network learn to erase what is no longer useful (e.g. forgetting the subject of a previous sentence when a new one begins).

In short: LSTM replaces the RNN's single fragile hidden state with a gated memory system (cell state + three gates) that can preserve information over hundreds of time steps and learn *what* is worth remembering.

---

## Q10. Explain the complete architecture of LSTM.

An LSTM cell maintains **two** state vectors across time: the hidden state hₜ (short-term, output to the next layer) and the **cell state Cₜ** (long-term memory conveyor). Three sigmoid gates regulate information flow.

### Components

- **Cell state (Cₜ)** — the long-term memory. It runs straight down the time axis with only minor linear interactions (element-wise × and +), so information and gradients travel long distances without decay.

- **Forget gate (fₜ)** — decides what to erase from the old cell state. Output in (0, 1) per element: 0 = "forget completely", 1 = "keep completely".

- **Input gate (iₜ)** — decides which new information to write into the cell state. Works together with a **candidate vector** C̃ₜ (tanh, in (−1, 1)) holding the new candidate content.

- **Output gate (oₜ)** — decides what part of the cell state to expose as the hidden state hₜ (the cell's output to the next time step / layer).

### Data flow through one cell (time step t)

```
        Cₜ₋₁ ──→ [× fₜ] ──→ [+] ──→ Cₜ ──→ [tanh] ──→ [× oₜ] ──→ hₜ
                     ↑        ↑                                     ↑
                  forget   input gate                          output gate
                   gate    × C̃ₜ (candidate)
                     ↑        ↑
                  hₜ₋₁, xₜ  hₜ₋₁, xₜ
```

1. **Forget:** Cₜ₋₁ is scaled by fₜ (erase/keep old memory).
2. **Write:** candidate C̃ₜ is scaled by iₜ and added (store new memory).
3. **Read:** Cₜ is squashed by tanh and scaled by oₜ to produce hₜ.

Full equations in Q12.

---

## Q11. Explain the role of the Forget Gate in LSTM. Why is forgetting important in deep learning?

**Role:** The forget gate computes

```
fₜ = σ(W_f · [hₜ�₁, xₜ] + b_f)     → values in (0, 1)
Cₜ = fₜ ⊙ Cₜ₋₁ + iₜ ⊙ C̃ₜ
```

Each element of fₜ multiplies the corresponding element of the old cell state. Near 0 → that memory slot is erased; near 1 → it is preserved. The gate is **learned**: the network discovers from data which past information stays relevant.

**Why forgetting matters:**

1. **Finite capacity** — the cell state has fixed size. Without forgetting, it fills with stale, irrelevant information and new inputs get drowned out. Forgetting frees capacity for what matters now.

2. **Context boundaries** — in language, when a new sentence or topic starts, the old subject/tense is usually irrelevant. The forget gate learns to reset: e.g. after a full stop, old grammatical context is dropped.

3. **Noise rejection** — in sensor/financial time series, old readings become misleading as regimes change (market crash, sensor drift). Learned forgetting adapts the memory horizon to the data instead of decaying everything uniformly like an RNN.

4. **Gradient health** — controlled forgetting (values near 1 for important content) is what keeps the gradient path open over long distances; indiscriminate decay is precisely the RNN failure mode.

Exam line: *the forget gate is what turns the cell state from a passive accumulator into an actively managed memory.*

---

## Q12. Explain mathematically how LSTM updates memory.

### Activation functions

- **Sigmoid:** σ(z) = 1 / (1 + e^(−z)), output ∈ (0, 1). Used for gates → acts as a soft on/off switch (how much passes).
- **Tanh:** tanh(z) = (e^z − e^(−z)) / (e^z + e^(−z)), output ∈ (−1, 1). Used for candidate values and cell-state scaling → zero-centred, keeps values bounded.

Notation: [hₜ₋₁, xₜ] = concatenation of previous hidden state and current input; ⊙ = element-wise multiplication; W, b are learned parameters (separate per gate).

### Gate calculations (step t)

1. **Forget gate** — what to discard from Cₜ₋₁:
   ```
   fₜ = σ(W_f · [hₜ₋₁, xₜ] + b_f)
   ```

2. **Input gate** — what new information to store, plus the candidate:
   ```
   iₜ  = σ(W_i · [hₜ₋₁, xₜ] + b_i)      (gate: how much to write)
   C̃ₜ = tanh(W_C · [hₜ₋₁, xₜ] + b_C)    (candidate: what to write)
   ```

3. **Cell state update** — the memory write:
   ```
   Cₜ = fₜ ⊙ Cₜ₋₁  +  iₜ ⊙ C̃ₜ
        └─ erase ─┘    └─ add new ─┘
   ```
   Note this is **additive**, not a squashed overwrite — the key to gradient flow. ∂Cₜ/∂Cₜ₋₁ = fₜ, which the network can learn to keep near 1, so gradients pass back through time almost intact.

4. **Output gate** — what to emit as hₜ:
   ```
   oₜ = σ(W_o · [hₜ₋₁, xₜ] + b_o)
   hₜ = oₜ ⊙ tanh(Cₜ)
   ```

### Why this fixes vanishing gradients

In a plain RNN, ∂hₜ/∂hₜ₋₁ = diag(tanh′)·Wₕₕ — a matrix product that compounds < 1 every step. In an LSTM, the memory path gives ∂Cₜ/∂Cₜ₋₁ = fₜ (a diagonal, element-wise scale). When the forget gate stays near 1, the gradient propagates across hundreds of steps with almost no decay — the **constant error carousel**.

---

## Q13. Differentiate between RNN and LSTM (Complexity, Performance, Memory handling).

| Aspect | RNN (vanilla) | LSTM |
|---|---|---|
| **Complexity** | 1 weight set per step (Wₓₕ, Wₕₕ, Wₕᵧ): ~3 parameter matrices. Fast to train, few parameters. | 4 gate computations per step (forget, input, candidate, output): ~4× the parameters of a vanilla RNN. Slower to train, more memory per step. |
| **Performance (short sequences)** | Competitive — simpler model trains faster and is less prone to overfitting on small data. | Comparable; the extra capacity is unnecessary and can overfit small datasets. |
| **Performance (long sequences)** | Poor — vanishing gradients; effectively no learning beyond ~10 steps. | Strong — designed for long-range dependencies; standard choice for long sequences. |
| **Memory handling** | Single hidden state hₜ, overwritten every step via tanh; memory decays uniformly, no selective keep/forget. | Separate cell state Cₜ (long-term) + hidden state hₜ (short-term); gates learn what to keep (fₜ), write (iₜ), and read (oₜ). Explicit, controllable memory. |

**Rule of thumb:** short sequences or tiny datasets → vanilla RNN is fine and cheaper; anything needing memory over dozens+ of steps → LSTM.

---

## Q14. Explain a practical project where LSTM can be used — stock prediction. Complete workflow.

**Goal:** predict the next-day closing price of a stock (e.g. RELIANCE) from historical OHLCV data.

### 1. Data collection
- Source: Yahoo Finance API (`yfinance`) or NSE data — daily Open, High, Low, Close, Volume for 5–10 years (~1,250–2,500 rows).
- Target: next-day Close (regression) or price direction up/down (classification).

### 2. Preprocessing
- **Feature engineering:** add technical indicators — 20/50-day moving averages, RSI, MACD, daily returns, volatility. These give the model engineered trend/momentum signals.
- **Normalization:** MinMax-scale features to (0, 1) — LSTMs are sensitive to feature scale; fit the scaler on training data only.
- **Sequencing:** sliding window — input = last 60 days of features (shape: 60 × n_features), label = day-61 Close. This turns the series into supervised samples.
- **Split:** chronological 80/10/10 train/validation/test — never shuffle time series (no look-ahead leakage).

### 3. Model architecture
```
Input (60, n_features)
 → LSTM(64, return_sequences=True) → Dropout(0.2)
 → LSTM(32) → Dropout(0.2)
 → Dense(1)                        (linear output for price)
```
Two stacked LSTM layers capture multi-scale temporal patterns; dropout regularizes.

### 4. Training
- Loss: MSE (or MAE); optimizer: Adam (lr ≈ 0.001).
- EarlyStopping on validation loss (patience ~10) + ReduceLROnPlateau to avoid overfitting the noisy series.
- Batch size 32, up to ~100 epochs. Walk-forward validation (retrain on expanding windows) gives a more honest estimate than a single split.

### 5. Evaluation
- Metrics: RMSE, MAE, MAPE on the test set; directional accuracy (% of days the up/down move was correct) — often more useful than price error for trading.
- Baseline comparison: beat naive "tomorrow = today" (persistence) and a moving-average model, or the LSTM adds nothing.
- Plot predicted vs actual prices; check residuals for regime bias (e.g. consistently wrong after earnings).

### 6. Deployment
- Retrain on a schedule (e.g. nightly) with the latest data; serve via a FastAPI endpoint returning the next-day forecast + confidence interval.
- Monitor live RMSE vs backtest; trigger retraining when drift exceeds a threshold. Disclaimer: markets are non-stationary and news-driven — an LSTM models historical patterns, not future shocks; use as a signal, not a standalone trading system.

---

## Q15. Why is LSTM better for long-term dependencies?

Three architectural reasons, all stemming from the cell state + gates design:

1. **Additive memory path (constant error carousel):** The cell state updates as Cₜ = fₜ ⊙ Cₜ₋₁ + iₜ ⊙ C̃ₜ. The old memory is *added to*, not passed through a squashing nonlinearity and matrix multiply. The gradient along this path is ∂Cₜ/∂Cₜ₋₁ = fₜ, which the network learns to hold near 1 for important information — so error signals travel back hundreds of steps almost undecayed, versus the exponential decay in a vanilla RNN (Q5).

2. **Learned, selective retention:** The forget gate decides per-element what survives and the input gate decides what enters. Important distant context (e.g. the subject "keys" 20 words back) is protected at fₜ ≈ 1, while irrelevant filler is erased — instead of the RNN's uniform decay of everything.

3. **Decoupled storage and output:** The cell state stores long-term content while the output gate controls what the rest of the network sees (hₜ = oₜ ⊙ tanh(Cₜ)). A memory can be *kept* without being *emitted* at every step — e.g. holding a sentence's topic silently until the final classification. In a vanilla RNN the single hidden state must simultaneously remember and output, which corrupts stored information.

Net effect: where a vanilla RNN reliably spans ~5–10 steps, LSTMs routinely learn dependencies across hundreds of time steps — which is why they became the default for language modelling, speech, and long-horizon forecasting before transformers.
