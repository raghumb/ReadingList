For RAG, evaluations (evals) are tests that tell you whether your system retrieves the right evidence and generates an accurate, grounded answer from it.
The most important principle is to evaluate retrieval and generation separately. If the final answer is wrong, you need to know whether the retriever failed to find the right document, or the LLM failed to use the retrieved evidence correctly.
1. The main categories of RAG evals

A. Retrieval evals
Did the system find the correct documents or chunks?
Recall@K, Precision@K, MRR, nDCG, context relevance


B. Generation evals
Did the LLM answer correctly using the retrieved evidence?
Faithfulness, answer correctness, answer relevance, completeness


C. Citation and safety evals
Are the claims supported by their cited sources, and is the user allowed to see them?
Citation precision, citation coverage, access control, prompt-injection resistance

D. Operational evals
Is the pipeline fast, reliable, and cost-effective?
Latency, cost per query, cache hit rate, failure rate, freshness


2. Retrieval evals — did we find the right information?
Imagine the knowledge base contains these chunks:
- D1: Payment API requirements
- D2: Security requirements
- D3: Database backup policy
- D4: API performance requirement
- D5: User interface design
User query: "What is the latency requirement for the payment API?"
The known relevant document is D4.
Suppose the retriever returns [D1, D3, D4].
Eval 1: Recall@K
Measures how many of the known relevant documents were retrieved within the top K results.
\[
\text{Recall@K} =
\frac{\text{Relevant documents in top K}}
{\text{All relevant documents}}
\]

Recall@K measures how many of the relevant documents your RAG system successfully retrieves within its top K results.

Precision@K measures how many of the top K documents retrieved by your RAG system are actually relevant to the user's question.
Recall@K asks, “Did we find the relevant information?” Precision@K asks, “How much of what we found is relevant?”

recall = relevant chunks retrieved in top K/total relevant chunks
precision = relevant chunks retrieved in top K/total chunks in top K

- Low recall: The system misses useful information.
- Low precision: The system returns too much irrelevant information.
In RAG, low precision can fill the LLM's context window with distracting material, potentially hurting answer quality and increasing token costs.

If there is one relevant document and it appears in the top 3, Recall@3 = 1.0, or 100%.
Why it matters: The relevant evidence must be retrieved before the LLM can use it.
Eval 2: Precision@K
Measures the proportion of retrieved documents that are relevant.
\[
\text{Precision@K} =
\frac{\text{Relevant documents in top K}}{K}
\]

If 1 out of 3 retrieved chunks is relevant, Precision@3 = 33.3%.
Why it matters: Low precision means irrelevant context can waste tokens or distract the generator.
Eval 3: Mean Reciprocal Rank (MRR)
Measures how highly the first relevant result appears.
\[
\text{MRR} = \frac{1}{N}\sum_{i=1}^{N}\frac{1}{r_i}
\]

Here, \(r_i\) is the rank of the first relevant result for query \(i\).
If the first relevant result is ranked third, its reciprocal rank is \(1/3\). If ranked first, it is 1.
Why it matters: The most useful evidence should appear near the top, especially when you only pass a few chunks to the LLM.
Eval 4: nDCG@K
Measures ranking quality while accounting for graded relevance: highly relevant results should rank above partially relevant results.
Why it matters: A chunk that directly states a requirement should generally rank above one that merely discusses the same topic.
Eval 5: Context relevance
Evaluates whether the retrieved context actually addresses the question. This can use human labels or an LLM judge.
Example:
- Query: "What is the payment API latency target?"
- Retrieved chunk: "The payment API must have p95 latency below 500 ms." — highly relevant.
- Retrieved chunk: "Payments must use encrypted connections." — related to payments, but irrelevant to latency.
This differs from Recall@K: context relevance can be assessed without a complete inventory of all relevant documents, although human-labelled datasets make the evaluation more reliable.
3. Generation evals — did the LLM produce a good answer?
Now suppose the retriever successfully finds this chunk:
Payment API: p95 response latency must be below 500 ms.

The LLM generates:
The payment API must maintain p95 latency below 500 ms.

This is a good answer. But what if it says "below 200 ms"? Retrieval could be perfect while generation is wrong.
Eval 6: Faithfulness (groundedness)
Checks whether claims in the answer are supported by the retrieved context.
Answer	Result
"p95 latency must be below 500 ms."	Faithful
"p95 latency must be below 200 ms."	Unsupported
"The API uses encryption."	Unsupported by this chunk
This evaluates support from the supplied evidence, not whether the evidence itself is true or current.
Eval 7: Answer correctness
Compares the generated answer with a trusted reference answer or independently verified facts.
Reference: "The payment API p95 latency target is below 500 ms."
Generated answer: "The target is below 200 ms."
Result: Incorrect.
Faithfulness and correctness are different. An answer can faithfully repeat an incorrect source, so you need both checks for important applications.
Eval 8: Answer relevance
Checks whether the answer addresses the user's actual question.
Query: "What is the payment API latency target?"
Answer: "The system uses encrypted connections."
That answer might be factually correct according to another document, but it does not answer the question.
Eval 9: Completeness
Checks whether the answer includes all required information.
Suppose the reference requires both:
- p95 latency below 500 ms.
- The target applies under the specified normal operating load.
An answer that mentions only the latency threshold might be partially correct but incomplete.
Eval 10: Citation correctness
Checks whether citations exist and support the claims attached to them.
For example:
p95 latency must be below 500 ms. [Payment API Requirements, section 4.2]

The evaluator checks that the cited section really supports the threshold, rather than merely mentioning the payment API.
For high-quality RAG, evaluate citation support at the claim level, not just whether the answer contains a citation.
4. Safety and production evals
These are easy to overlook when focusing only on answer quality.
Eval	What it tests	Example failure
No-answer / abstention	Does the system admit when evidence is insufficient?	Invents a latency target when none exists
Access-control correctness	Are unauthorized chunks excluded?	User receives a confidential document
Prompt-injection resistance	Does retrieved text improperly override system instructions?	A document instructs the model to reveal secrets
Freshness	Does the answer use the latest applicable source?	Returns a superseded policy
Contradiction handling	Does it detect conflicting sources?	Silently combines incompatible requirements
Latency	How long does the full pipeline take?	p95 response time exceeds the service objective
Cost	What is the cost per query or successful answer?	Excessive reranking and generation costs
For enterprise RAG, access control, freshness, and abstention are correctness requirements, not just optional optimizations.
5. Build a small RAG evaluation dataset
Before choosing frameworks, create a small dataset with known questions, relevant documents, and reference answers.
Here is an example for your AI governance / Coherent use case.
Query	Expected relevant evidence	Expected answer
What is the payment API latency requirement?	NFR-001	p95 latency below 500 ms
Which acceptance criteria apply to FR-001?	AC records linked to FR-001	List the linked acceptance criteria
Which baseline is approved?	Approved baseline record	Latest approved baseline ID
What happens when two requirements contradict each other?	Governance rules for contradictions	Describe the defined conflict-handling process
What is the database retention period?	Retention policy, if available	Answer only if the policy specifies it
What is the production API's maximum throughput?	Relevant NFR or architecture record	Abstain if no supporting evidence exists
The last two cases are particularly useful: they test whether RAG can distinguish missing evidence from evidence that actually answers the question.
A more complete test record could look like this:
{
  "query": "What is the payment API latency requirement?",
  "relevant_chunk_ids": ["NFR-001"],
  "reference_answer": "p95 latency must be below 500 ms",
  "expected_behavior": "answer_with_citation"
}


Run every query through your pipeline, collect the retrieved chunks and generated answer, and compare the outputs against the dataset.
6. Which evals should you implement first?
I recommend starting with these six.
1. Recall@K
Did retrieval find the required evidence?


2. MRR or nDCG@K
Did the most relevant evidence rank highly?


3. Faithfulness
Are answer claims supported by retrieved evidence?


4. Answer correctness
Does the answer match trusted facts?


5. Citation correctness
Do citations support the claims they accompany?


6. Abstention correctness
Does the system avoid answering when evidence is insufficient?



Add access-control, freshness, latency, and cost evaluations before using the system with sensitive or production data.
7. How do you automate these evals?
You can build a simple evaluation runner in Python or use an existing RAG evaluation framework such as Ragas or DeepEval.
A practical architecture is:
Evaluation dataset
Questions · Relevant chunk IDs · Reference answers

Run the RAG pipeline
Capture retrieval results, context, answer, and citations

Deterministic evals
Recall, ranking, citations, permissions


Model-assisted evals
Faithfulness, relevance, completeness



Evaluation report
Scores · Failures · Regression comparisons


Use deterministic checks whenever possible. Model-assisted judges are useful for semantic assessments, but their judgments can be inconsistent and should themselves be validated against human-labelled examples.
One more important distinction
If you later optimize your RAG system with query rewriting, hybrid retrieval, reranking, or caching, keep the same evaluation dataset and compare before and after each change.
For example:
- Baseline dense retrieval: Recall@5 = 0.72.
- Hybrid retrieval: Recall@5 = 0.88.
- Hybrid retrieval plus reranking: nDCG@5 improves from 0.69 to 0.84.
Those numbers are illustrative, not measured results. The point is that every added technique should demonstrate a measurable improvement in retrieval or answer quality without unacceptable increases in latency and cost.
That is how you turn RAG evaluation into an engineering discipline rather than relying on a few impressive example answers.


# Normalized Discounted Cumulative Gain (NDCG)
NDCG is a ranking metric used to evaluate how good a search engine or RAG system is at ordering its results.

It checks two things:
1. Relevance: Are the retrieved documents useful?
2. Ranking: Are the most relevant documents appearing near the top?
NDCG is especially useful in evaluating search engines, recommendation systems, and RAG retrieval and reranking.
1. Understand with a simple example
Suppose a user asks a question, and your RAG system retrieves five documents.

The relevance score for each document is rated from 0 to 3:
- 3 = Highly relevant
- 2 = Relevant
- 1 = Slightly relevant
- 0 = Not relevant

NDCG measures "How relevant the results are, giving higher positions more weight"

NDCG has three main steps.
Step 1: Calculate DCG
DCG stands for Discounted Cumulative Gain.

It adds up the relevance of retrieved documents while applying a penalty to documents that appear lower in the ranking.

The common formula is:

Step 2: Calculate ideal DCG (IDCG)
IDCG is the best possible DCG for those same documents.

To calculate it, sort the relevance scores from highest to lowest, then apply the same DCG formula.

This creates a perfect ranking against which your actual ranking can be compared.
Step 3: Normalize DCG
Divide the actual DCG by the ideal DCG.





