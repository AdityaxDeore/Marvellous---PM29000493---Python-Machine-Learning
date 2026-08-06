# Assignment 38 — Conceptual Answers

## Q4. How a Decision Tree makes decisions (Ball dataset example)

A decision tree makes decisions by asking a series of yes/no questions about the
features of an input, following the branch that matches each answer, until it
reaches a leaf node that holds the final class label.

With the Ball dataset (features: Surface, Colour; labels: Tennis, Cricket),
the trained tree works like this:

1. The tree first asks the most informative question, e.g. **"Is Surface = Smooth?"**
   (Surface is chosen first because it separates the labels best — almost all
   Rough balls are Tennis and almost all Smooth balls are Cricket).
2. If the answer is **No** (Surface = Rough), the tree follows the left branch
   and predicts **Tennis**.
3. If the answer is **Yes** (Surface = Smooth), it may ask one more question,
   e.g. **"Is Colour = Red?"**, and predict **Cricket** or **Tennis** from the
   leaf reached.

So a decision tree classifies by **splitting the data into smaller and smaller
groups at each node** using the feature that best separates the classes, and the
prediction for a new ball is simply the majority class of the training balls in
the leaf it lands on.

## Q5. Root node, internal node, and leaf node

| Node type     | Definition |
|---------------|------------|
| **Root node** | The very first node at the top of the tree. It represents the entire training dataset and applies the first splitting question (in our example, the test on Surface). |
| **Internal node** | Any node that is neither the root nor a leaf. It represents a subset of the data and applies one more yes/no question (a further split) on one feature, e.g. the test on Colour. |
| **Leaf node** | A terminal node at the bottom with no further splits. It represents a pure (or mostly pure) group of samples and carries the final prediction — e.g. "Tennis" or "Cricket". |

In the ball example: **Root** = question on Surface; **Internal** = question on
Colour under the Smooth branch; **Leaves** = final labels Tennis / Cricket.

## Q10. Conclusion

In this Decision Tree example I learned how a machine learning model can learn
simple rules directly from data. I learned that categorical features like
Surface and Colour must first be converted into numbers using Label Encoding
before the model can use them, and that the data is split into training and
testing sets so the model's accuracy can be measured on unseen samples. I also
learned that the tree picks the most informative feature (Surface) for the
first split, that its structure can be visualised with plot_tree, and that even
a very small dataset is enough to demonstrate training, prediction, and
accuracy evaluation — the same workflow used for much larger real-world
problems.
