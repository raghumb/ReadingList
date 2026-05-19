# Precision vs Recall
Precision is : TP/TP + FP
 (True Positives / All Predicted Positives). 
Recall is : TP/TP + FN
 (True Positives / All Actual Positives).

When to use Precision: When the cost of a false positive is high (e.g., email spam filters, where you don't want to lose important emails).

When to use Recall: When the cost of a false negative is high (e.g., cancer detection, where you don't want to miss a positive case).

Balance: The F1-score is the harmonic mean of precision and recall, used when you need a balance between the two.


# DeepEvals


# Rag Metrics
[Metrics](https://docs.ragas.io/en/stable/concepts/metrics/answer_relevance.html)

- Faithfulness: This measures the factual consistency of the generated answer against the given context. It is calculated from answer and retrieved context
- Answer relevance: how pertinent the generated answer is to the given prompt. Mean cosine similarity of the original question to a number of artifical questions, which where generated (reverse engineered) based on the answer.

## BLEU

# ROUGE

