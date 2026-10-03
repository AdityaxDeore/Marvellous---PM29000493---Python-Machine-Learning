# Assignment 70 — Answers (RNN / NLP Theory)

## Q1. Explain why RNN is widely used in Natural Language Processing.

- **Language is sequential:** Text is a sequence of words whose meaning depends on order ("not good" ≠ "good not"). RNNs are designed for sequence data, unlike fixed-size feedforward networks.
- **Handles variable length:** Sentences have different word counts. An RNN unrolls across time steps, so one model processes sentences of any length with a fixed parameter set.
- **Carries context:** The hidden state acts as memory, so when the model reads a later word it still "remembers" earlier words — essential for resolving negations, pronouns ("it", "they"), and long-range dependencies.
- **Parameter sharing:** The same weights (Wₓ, Wₕ, b) are used at every step, so the model learns *positional patterns* (e.g., "not" negates the next word) rather than separate rules per position.
- For these reasons RNNs underpin core NLP tasks: sentiment analysis, machine translation, language modeling, text generation, and named entity recognition (later extended by LSTM/GRU variants and attention).

## Q2. Describe the complete pipeline of sentiment analysis using RNN.

1. **Data collection and labeling:** Gather text samples (e.g., product reviews); label each as positive (1) or negative (0).
2. **Text preprocessing:** Lowercase the text; remove punctuation, numbers, and extra whitespace. ("Food was NOT good!!" → "food was not good")
3. **Tokenization:** Split each sentence into word tokens: ["food", "was", "not", "good"].
4. **Word indexing / vocabulary building:** Assign a unique integer ID to each word in the vocabulary: {"food": 1, "was": 2, "not": 3, "good": 4}.
5. **Sequence conversion:** Replace words with their IDs: "food was not good" → [1, 2, 3, 4].
6. **Padding/truncation:** Pad all sequences to the same length (e.g., with 0s) so they can be batched into a matrix: [1, 2, 3, 4] → [1, 2, 3, 4] (already length 4), while shorter ones get zeros appended.
7. **Embedding layer:** Convert each integer ID into a dense vector (e.g., 32 dimensions). Now the input is a matrix of shape (sequence_length × embedding_dim).
8. **RNN layer:** Feed the embedded sequence step by step into the RNN (e.g., SimpleRNN or LSTM). The final hidden state summarizes the whole sentence.
9. **Dense output layer with sigmoid:** The final hidden state passes through a dense layer with sigmoid activation, producing a value between 0 and 1 = probability of positive sentiment.
10. **Training:** Compute binary cross-entropy loss against true labels and update weights via backpropagation through time.
11. **Prediction:** For a new sentence, run the same pipeline; output ≥ 0.5 → positive, < 0.5 → negative.

## Q3. Explain tokenization with suitable example.

**Tokenization** is the process of splitting raw text into smaller units called **tokens**, which are the atomic inputs the model works with.

- Most commonly, tokens are **words**, but they can also be characters or subwords.
- Example: Sentence `"The food was not good"` tokenizes into `["The", "food", "was", "not", "good"]`.
- Tokenization is required because neural networks cannot read raw text; they need a discrete, indexable representation of each unit.
- Typically combined with preprocessing (lowercasing, punctuation removal) before tokenizing: `"The food was not good"` → `"the food was not good"` → `["the", "food", "was", "not", "good"]`.

## Q4. Explain padding and why equal sequence length is required.

- **Padding** means adding special filler tokens (usually the ID 0, representing `<PAD>`) to shorter sequences so that every sequence in a batch has the **same length**.
- Example: with maximum length 6 —
  - "food was not good" → [1, 2, 3, 4, **0, 0**]
  - "not good" → [3, 4, **0, 0, 0, 0**]
- **Why equal length is required:** Deep learning models operate on **batch tensors** — every row of the input matrix must have identical shape. Without padding, sequences of different lengths cannot be stacked into one matrix and processed in parallel.
- Longer sequences than the fixed length are **truncated** to fit.
- During training, padding tokens are typically masked (ignored) so they do not affect the hidden state or loss.

## Q5. Explain vocabulary size and how tokenizer creates word index.

- **Vocabulary** is the set of all unique words (tokens) in the training corpus.
- **Vocabulary size** is the count of unique words — e.g., 10,000 means the model knows 10,000 distinct words.
- The tokenizer builds a **word index**: a dictionary mapping each word to a unique integer ID:
  - `{"<PAD>": 0, "food": 1, "was": 2, "not": 3, "good": 4, "bad": 5, ...}`
- How it is created: the tokenizer scans the corpus, counts word frequencies, sorts words (usually by frequency), and assigns IDs — the most frequent word gets ID 1, and so on. ID 0 is reserved for padding.
- Rare words beyond a limit (e.g., the top 10,000) are mapped to a special `<OOV>` (out-of-vocabulary) token.
- The IDs are what the model actually receives as input sequences: "food was not good" → [1, 2, 3, 4].

## Q6. Explain embedding layer and why token IDs are not enough for deep learning.

- An **embedding layer** maps each integer word ID to a **dense vector** of fixed size (e.g., 32 or 100 dimensions) that is *learned* during training.
- Example: ID 1 ("food") → [0.12, −0.45, 0.88, …]; ID 3 ("not") → [−0.23, 0.91, 0.05, …].
- These vectors capture **semantic meaning**: words used in similar contexts ("good", "great") end up with similar vectors, so the model learns relationships between words.

Why raw token IDs are not enough:

- **IDs imply false ordering:** IDs are arbitrary labels (1, 2, 3, 4), but a neural network would treat them as numbers — interpreting "good" (ID 4) as *greater than* "food" (ID 1), which is meaningless.
- **No similarity information:** IDs carry no notion that "good" and "great" are related while "good" and "bad" are opposites.
- **Sparse vs. dense:** A raw ID is a single scalar; the embedding expands it into a rich, continuous representation the RNN can compute with.
- Therefore: IDs identify *which* word; embeddings represent *what the word means*.

## Q7. Differentiate between one-hot encoding and embedding vectors.

| Aspect | One-hot encoding | Embedding vector |
|--------|-----------------|------------------|
| Representation | Sparse binary vector with a single 1 at the word's position, rest 0s: [0, 1, 0, 0] | Dense real-valued vector of learned floats: [0.12, −0.45, 0.88, …] |
| Dimensionality | Equals vocabulary size (e.g., 10,000 → 10,000-dim vector) — very high | Fixed small size (e.g., 32–300) regardless of vocabulary size |
| Learning | Fixed; no parameters learned | Learned during training; improves with more data |
| Semantic meaning | None — every word is equidistant from every other word | Captures meaning — similar words have similar vectors |
| Memory/computation | Inefficient for large vocabularies | Compact and efficient |
| Usage | Sometimes used for small vocabularies; generally impractical in deep learning NLP | Standard input representation for RNNs and all modern NLP models |

## Q8. Explain how the sentence below is processed by RNN: "food was not good"

Preprocessing (assume lowercased, tokenized):

1. **Tokenize:** ["food", "was", "not", "good"]
2. **Index (IDs):** [1, 2, 3, 4] (using the vocabulary word index)
3. **Pad:** e.g., to length 6 → [1, 2, 3, 4, 0, 0]
4. **Embed:** each ID → a dense vector; input becomes a 6 × embedding_dim matrix.

Then the RNN runs **one time step per word**:

- **t=1, "food":** h₁ = tanh(Wₓ·emb("food") + Wₕ·h₀ + b). Memory now holds the subject: "food".
- **t=2, "was":** h₂ = tanh(Wₓ·emb("was") + Wₕ·h₁ + b). Memory: "food was".
- **t=3, "not":** h₃ = tanh(Wₓ·emb("not") + Wₕ·h₂ + b). Memory: "food was not" — the negation is now encoded in the state.
- **t=4, "good":** h₄ = tanh(Wₓ·emb("good") + Wₕ·h₃ + b). Because h₃ already carries "not", "good" is interpreted *in negated context* — memory: "food was not good".

Finally, h₄ (or the padding steps after it) feeds a dense + sigmoid output layer, which yields a value near 0 → **negative sentiment**. The key insight: the prediction is correct only because the recurrent hidden state let the earlier word "not" influence the interpretation of the later word "good".
