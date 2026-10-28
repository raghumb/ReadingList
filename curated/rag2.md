https://github.com/KalyanKS-NLP/RAG-Interview-Questions-and-Answers-Hub

TODO:
Maximal Marginal Relevance (MMR) 


-  Is RAG still relevant in the era of long context LLMs?
API Cost, lost in middle, latency

- What are the fundamental challenges of RAG systems?
Scalability, Latency, Hallucination Risk , Bias and Noise

-  What are effective strategies to reduce latency in RAG systems?
Caching, embedding quantization, selective query rewriting, and selective re-ranking 

- Why is re-ranking important
Re-ranking uses cross-encoder models to deeply measure the semantic relevance of query-chunk pairs and then brings relevant chunks ahead of irrelevant chunks. This reduces the noise and helps the generator LLM to generate more accurate and coherent answers.

- What is the purpose of overlap during chunking in a RAG pipeline?
chunk overlap during chunking ensures contextual continuity and prevents loss of information at the boundaries of chunks. This improves the retrieval accuracy and maintains coherence in the text fed to the LLM.

overlap of about 10-20% of the chunk size

- How do you choose the chunk size for a RAG system?
balancing granularity, context completeness, and computational efficiency. 

Smaller chunks (e.g., 100-200 tokens) allow precise retrieval but may lack sufficient context. Larger chunks (e.g., 500-1000 tokens) provide more context at the cost of increased computational load and potential noise.

smaller chunks mean that there are more chunks in the vector database, which increases storage costs and slows down the similarity search.

- What are the key hyperparameters in a RAG pipeline?
Chunk size, chunk overlap, embedding dimensionality, retrieval top-k, and retrieval threshold are some of the most important hyperparameters for retrieval in RAG. Temperature and max output length are two important hyperparameters for RAG generation.

- Explain how the HyPE technique works in RAG.
The HyPE (Hypothetical Prompt Embedding) technique improves retrieval accuracy by addressing the semantic mismatch between user queries and document chunks.

Unlike HyDE, which generates hypothetical answer documents at query time, HyPE precomputes hypothetical questions for each document chunk during the indexing phase. These questions are designed to capture the key concepts in the chunk, transforming retrieval into a "question-to-question" matching process, which reduces latency and improves retrieval.

- What are the different chunk enhancement techniques in RAG?
 HyPE, Contextual Chunk Header, and Document Augmentation.

Contextual Chunk Header adds relevant contextual information such as document titles or section headings to each chunk before embedding, helping retrieval models understand and rank chunks better when chunk text alone is ambiguous.

Document Augmentation enhances chunks by including additional metadata and enhances retrieval quality.

- What are some common chunking methods used in RAG?

Common chunking methods used in RAG are fixed-size chunking, recursive chunking, semantic chunking, and agentic chunking.

Fixed-size chunking divides text into uniform segments based on a predefined token or character length, often incorporating overlap to maintain context.

Recursive chunking iteratively splits text using natural separators like paragraphs or sentences to preserve logical boundaries. Semantic chunking groups text based on semantic similarity using embeddings, creating coherent, meaning-based chunks.

Agentic chunking leverages AI agents to dynamically segment text into task-oriented, semantically coherent chunks, often with metadata to enhance retrieval relevance.

- What are the common retrieval approaches used in RAG systems?
dense retrieval, sparse retrieval, and hybrid retrieval.

Dense retrieval uses embeddings to capture semantic similarity, enabling effective query matching to relevant document chunks. Sparse retrieval relies on traditional methods like TF-IDF or BM25, focusing on keyword-based matching for efficiency.

Hybrid retrieval combines dense and sparse methods to balance semantic understanding and computational speed. These approaches ensure relevant context is retrieved for generating accurate responses in RAG systems.

- What are some common challenges in RAG retrieval?

 ineffective query understanding, scalability issues, context fragmentation, and handling multimodal data.

 Scalability issues arise when large-scale data retrieval slows performance or overwhelms the system. Context fragmentation happens when retrieved chunks lack sufficient context, lowering response quality. Handling multimodal data is challenging due to complexities in integrating text, images, or other formats effectively.

- What are the key metrics for evaluating retrieval quality in RAG?

Key metrics for evaluating retrieval quality in RAG systems are precision, recall, Mean Reciprocal Rank (MRR), and Normalized Discounted Cumulative Gain (NDCG). Precision measures the proportion of retrieved document chunks that are relevant, while recall assesses the proportion of relevant document chunks retrieved from the total available.

MRR evaluates the ranking quality by considering the position of the first relevant document chunks, and NDCG accounts for the relevance and ranking of retrieved documents. These metrics collectively ensure the retriever effectively identifies and ranks relevant information.

- Explain the role of ANN (Approximate Nearest Neighbor) search algorithms in RAG retrieval.

 (ANN) search algorithms play a crucial role in RAG retrieval by enabling fast and scalable search of relevant document chunks within large vector databases. Approximate Nearest Neighbor (ANN) algorithms enable fast search in RAG retrieval by quickly narrowing down the search space to a small subset of candidate vectors instead of scanning all vectors.

This reduces the number of comparisons needed, significantly speeding up retrieval while maintaining good enough accuracy for relevant document chunks matching. This balance of speed and precision is crucial for real-time and large-scale RAG systems.

- Explain the step-by-step working of ANN algorithms for fast search in RAG retrieval.

ANN algorithms for fast search in RAG retrieval involve four steps namely - Encoding, Indexing, Navigating, Retrieving.

(i) Encoding: Convert document chunks and queries into vector representations.

(ii) Indexing: Organize these vectors into a specialized data structure (like graphs or hash tables) for quick lookup.

(iii) Navigating: Efficiently explore the index to find vectors close to the query without checking all data points.

(iv) Retrieving: Return the closest approximate neighbors that provide relevant information for RAG retrieval.

- What are the typical distance metrics used for similarity search in vector databases?

Euclidean distance, cosine similarity, and dot product similarity. Euclidean distance measures the straight-line distance between vectors, making it intuitive for geometric closeness. Cosine similarity evaluates the angle between vectors, focusing on their direction (meaning) rather than magnitude.

Dot product similarity considers both magnitude and direction. These metrics are selected based on the data type and the underlying embedding model to ensure effective and accurate retrieval.

Unlike Euclidean distance or dot product, cosine similarity is invariant to vector length, providing stable and interpretable similarity scores. This helps RAG systems retrieve relevant document chunks even when text lengths vary, improving accuracy and consistency in semantic search.

- How does hybrid search work in the context of RAG retrieval?
Hybrid search in RAG systems combines keyword-based retrieval and semantic vector search to leverage the strengths of both methods. It uses a weighted formula to balance keyword relevance and semantic similarity scores.

- How do you balance relevance and diversity when retrieving document chunks for RAG?

The retrieval step in RAG relies on cosine similarity to identify top-k relevant document chunks. However, one downside of this approach is that it can return highly similar document chunks, leading to redundancy.

Balancing relevance and diversity is crucial in RAG retrieval to include contextually important yet diverse document chunks, preventing redundancy and capturing a broader range of perspectives. This balance helps when dealing with complex questions, as different viewpoints or unique insights can improve the answer's quality while still being accurate.

Techniques like Maximal Marginal Relevance (MMR) help to select document chunks that are both highly relevant to the query and diverse from each other, reducing redundancy.

- How do sparse embeddings differ from dense embeddings in terms of keyword matching and retrieval interpretability?

Sparse embeddings provide interpretability and excel at exact keyword matching. These embeddings represent text as high-dimensional vectors with many zeros. In this, each dimension corresponds to a specific term or feature, making retrieval results more understandable.

In contrast, dense embeddings are low-dimensional, continuous vectors with mostly non-zero values learned from neural networks, capturing semantic relationships and context beyond exact matches. This makes dense embeddings less interpretable but more effective for retrieving semantically related content where keywords do not exactly overlap.

Thus, sparse embeddings are favored for precise keyword-based retrieval and interpretability, while dense embeddings support richer, context-aware retrieval. Hybrid approaches leverage the strengths of both sparse and dense embeddings to enhance retrieval performance.

- What advantages does quantization offer over dimensionality reduction for scaling embeddings?

Quantization offers several advantages over dimensionality reduction for scaling embeddings in RAG retrieval. It compresses embeddings by reducing the precision of numerical values (e.g., from float32 to int8 or float8), achieving up to 4x storage reduction with minimal performance loss.

Unlike dimensionality reduction, which may discard important features and degrade accuracy, quantization preserves the full dimensionality of embeddings, maintaining richer semantic information. Additionally, quantization accelerates computation on hardware optimized for lower-precision formats, improving retrieval speed.

This makes it particularly effective for large-scale RAG systems where storage and latency are critical, while dimensionality reduction risks compromising retrieval quality.

However, the trade-off is a slight drop in retrieval accuracy or relevance. Additionally, quantization effectiveness can vary depending on the embedding model.

Scalar quantization in RAG retrieval compresses embeddings by reducing the bit precision (commonly to int8), offering a moderate 4x reduction in memory usage while maintaining a good balance between retrieval accuracy and speed.

Binary quantization, on the other hand, converts embeddings to 1-bit vectors, achieving up to 32x compression and significantly faster retrieval but at the cost of greater accuracy loss.

- What are the different types of re-ranker models 

Cross-Encoder Rerankers: These models jointly encode the query and document chunk pair to produce a highly accurate relevance score, offering nuanced understanding of relationships but with medium computational cost.

Multi-Vector or Late Interaction Models: Such as ColBERT, they encode queries and document chunks separately but perform fine-grained interaction later, balancing efficiency and performance with lower cost.

Large Language Model (LLM) Rerankers: Utilize powerful LLMs to reason about query-document chunk relevance, achieving great accuracy but incurring high computational overhead.

- 