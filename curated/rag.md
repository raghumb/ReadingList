# Retreival Techniques - Query transformation
## Why?
user questions may be poorly worded for retrieval

### How?
- Query rewriting: Make queries more specific and detailed, improving the probability of retrieving the most relevant information
- Step-back prompting: Generate broader and more general queries that can help retrieve relevant background information
- Sub-query decomposition: Break down complex queries into simpler sub-queries for more comprehensive information retrieval.

All of these use LLMs to generate queries.

# Ranking
Reciprocal Rank fusion to reorder documents.

# Metadata filtering
Filter based on metadata like time, category etc, before retreiving.

# Multi-Vector Retriever
(Langchain Multi Vector retriever)[https://www.langchain.com/blog/semi-structured-multi-modal-rag?_gl=1*glfzmk*_gcl_au*MTQ3OTc4ODk0Mi4xNzcwNjk4NzEz*_ga*MjA5MjA2ODM0Mi4xNzM0OTU0ODI3*_ga_47WX3HKKY2*czE3NzYzOTg3MDMkbzE2JGcwJHQxNzc2Mzk4NzAzJGo2MCRsMCRoMA..]
Decouple documents, which we want to use for answer synthesis, from a reference, which we want to use for retriever. As a simple example, we can create a summary of a verbose document optimized to vector-based similarity search, but still pass the full document into the LLM to ensure no context is lost during answer synthesis.

For example, Unstructured will partition PDF files by first removing all embedded image blocks. Then it will use a layout model (YOLOX) to get bounding boxes (for tables) as well as titles, which are candidate sub-sections of the document (e.g., Introduction, etc). It will then perform post processing to aggregate text that falls under each title and perform further chunking into text blocks for downstream processing based on user-specific flags (e.g., min chunk size, etc).

# HyDE RAG (Hypothetical Document Embeddings) 
(HYDE Rag)[https://medium.com/aingineer/a-complete-guide-to-implementing-hyde-rag-82492551f3d8]

Before querying the actual corpus, the system generates a hypothetical document — a guess at what a good answer might look like — and uses that hypothesized text’s embedding as a query vector.