1. Make ReAct genuine
Next

From prompted behavior to runtime-controlled behavior
Your current agent asks the model to call the health-check tool first and then inspect error logs. But the prompt alone cannot guarantee this sequence.
- Enforce one tool call per reasoning cycle.
- Track the agent's current step.
- Ensure the next decision uses the previous observation.
- Stop when the model produces a final answer.
- Add a maximum-step limit.
Learning outcome: Understand the difference between asking an LLM to behave like an agent and implementing agent behavior in the runtime.


2. Add failure handling and safety
What happens when reality doesn't cooperate?
Make the service troubleshooting example more realistic.
- Handle malformed tool arguments and unknown tools.
- Catch tool exceptions and return structured error observations.
- Handle model API failures and timeouts.
- Enforce tool permissions and argument validation.
- Prevent infinite loops and repeated failed calls.
Learning outcome: Build an agent that fails predictably rather than crashing or looping indefinitely.

3. Add conversation state and memory
From one investigation to multiple interactions
You already maintain a conversation_history list. Extend it to support:
- Multiple user questions in the same session.
- Reusing relevant information from previous turns.
- Distinguishing session history from persistent memory.
- Trimming or summarizing history when it becomes too large.
Learning outcome: Understand why conversation history is not the same thing as long-term memory.

4. Add planning and multi-step tasks
From reactive decisions to deliberate execution
Let the agent investigate a problem that requires several dependent operations. Compare:
- Pure ReAct: choose the next action after every observation.
- Plan-and-execute: create a plan, execute steps, and revise the plan when needed.
Learning outcome: Understand when planning helps and when it adds unnecessary complexity.

5. Add tracing, metrics, and evaluation
Make agent behavior observable and testable
Record model calls, tool calls, arguments, observations, latency, token usage, errors, and termination reasons. Create repeatable tests for expected behavior.
Learning outcome: Learn how to debug an agent and measure whether a change actually improves it.

6. Refactor into a reusable agent framework
Generalize only after understanding the problems
Extract reusable pieces from the code you have built:
- Model adapter
- Tool registry and executor
- Message and state management
- Agent loop and stopping conditions
- Policies, limits, and tracing
Learning outcome: Understand the architecture of a small agent framework without starting with a framework's abstractions.

