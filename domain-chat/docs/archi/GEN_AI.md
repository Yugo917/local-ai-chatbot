### 🧠 1. Central Agent: `OptimizedAgent`

`OptimizedAgent` is the main orchestrator responsible for handling user queries. It follows an optimization strategy for language model calls based on two core tactics:

* **Reuse of validated answers** via a vector cache (`CachedAgentResponse`)
* **Query enrichment** through contextual pre-prompt generation (`PrepromptEnhancer`)

---

### 🧾 2. `PrepromptEnhancer`: Contextual Pre-prompt Generator

This module is triggered when no relevant response is found in the cache. It:

* Retrieves the original query
* Identifies the top `k` most relevant chunks (based on cosine similarity) from the `DomainCorpus`
* Structures an enriched prompt with domain-specific context

Example of prompt structure:

```plaintext
You are an expert in [domain].
Here are the relevant documents:
[chunk_1]
[chunk_2]
[chunk_3]
Question: [user_query]
Respond clearly and precisely.
```

This pre-prompt is then submitted to the selected LLM to generate an optimized response.

---

### 🗃️ 3. `CachedAgentResponse`: Validated Answer Memory

This module functions as a vector cache of previously validated responses. It:

* Searches for query similarities to reuse an existing response
* Stores newly validated responses along with their embeddings

This mechanism improves system responsiveness and avoids costly or redundant LLM calls.

---

### 🔄 4. Global Pipeline and Adaptive Intelligence

1. The user submits a query (`ask`)
2. `OptimizedAgent` checks for similar responses in `CachedAgentResponse`
3. If no satisfying match is found:

   * `PrepromptEnhancer` is activated to build an enriched prompt
   * The prompt is sent to the selected model
   * The response can be validated and saved using `validate-response`
4. Validated responses are vectorized and added to the cache for future reuse
