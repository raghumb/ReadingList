Agents fail in more ways than regular apps because they orchestrate multiple unreliable steps:

- LLM calls (timeouts, resource constraints, malformed outputs, runtime exceptions)
- Tool execution (network failures, invalid inputs, unavailable services)
- Workflow logic (policy guards, partial completion, dependency chains across tools)

1) Standardized error taxonomy
Use a small set of error classes with stable codes and consistent fields:

ValidationError: user input is missing/invalid (fail fast; usually not retryable)
LLMCallError: LLM provider/model call failed or returned unusable output (often retryable)
ToolExecutionError: a tool failed (sometimes retryable, sometimes not)
AgentWorkflowError: orchestration-level failure - the multi-step run cannot complete as designed.

2) Classification and recovery strategies
Normalize, then classify. normalizeUnknownError turns arbitrary thrown values into an AppError. classifyError adds retryable and type (error.code) so retries, logs, and user messaging share one pipeline instead of repeating instanceof trees.

Recovery strategies (typical ladder), as shown with a real local LLM via node-llama-cpp:

Timeout: bound how long any step can stall
Retry: only when classifyError says retryable (with backoff and jitter)
Fallback: if the primary tool fails in a transient way, run a safer alternative that returns a degraded but useful answer
Degraded mode: if the LLM path fails, delegate to runDegradedProfileResolution - deterministic extraction of a u_<digits> id and the same primary → fallback tool model, without embedding that logic inline in a huge catch
Graceful failure: if recovery isn’t possible, return formatUserFacingError plus a correlation id
When both primary (after retries) and fallback fail in degraded mode, the example promotes that outcome to AgentWorkflowError: the user still sees one clear message, while cause retains the underlying tool failure for debugging.


