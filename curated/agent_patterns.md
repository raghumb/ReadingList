References:
https://github.com/pguso/ai-agents-from-scratch/blob/main/examples/05_batch/CODE.md




1. ReAct (Reason + Act)


User → LLM → Think → Act → Observe
       ↑      ↓      ↓      ↓
   System  Reason  Tool   Result
   Prompt         Use
       ↑           ↓       ↓
       └───────────Iterate──┘


ReAct operates on the principle that reasoning and acting should be interleaved rather than treated as separate processes. It forces the LLM to "think out loud" before taking an action, grounding its reasoning in external realities.

Implementation:
The agent runs in a continuous while loop, prompted to generate a specific sequence:

Thought: The model analyzes the current state and decides what to do next.

Action: The model outputs a specific tool call (e.g., Search("Apple stock price")).

Observation: The external tool returns raw data back to the LLM.

Loop repeats until the model generates a final "Answer."

Use Case:
Ideal for open-ended research, question answering, and tasks requiring interaction with dynamic environments (like browsing a web store or querying an API) where the next step strictly depends on the result of the previous step.

Trade-offs:
Pros: 
- Highly resilient to hallucinations because the "Thoughts" are immediately grounded by real "Observations". Highly interpretable decision traces.   
Cons: 
-Greedy and short-sighted. Because it evaluates one step at a time, it often takes inefficient "detours". For long-horizon tasks, the context window fills up quickly with iterative loops, leading to token exhaustion and getting "stuck" in repetitive actions. 


2. Plan-and-Execute (Plan-and-Solve)

To fix ReAct's short-sightedness, the Plan-and-Execute architecture (rooted in Wang et al.'s 2023 "Plan-and-Solve Prompting") splits the task into two distinct cognitive phases. It trades reactive agility for global strategy.

Implementation:
- Phase 1 (The Planner): Given a user prompt, a "Planner" LLM acts from a bird's-eye view, breaking the problem down into an ordered list of concrete, dependent steps without executing any tools.   
- Phase 2 (The Executor): An "Executor" LLM takes the plan and runs through each step sequentially. The context and output from Step 1 are injected into Step 2, and so on.   

Use Case:
Complex, multi-step structured tasks with clear dependencies, such as writing software, complex data analysis, or booking a multi-leg travel itinerary.   

Trade-offs:
Pros: 
Vastly reduces cognitive overload for the LLM by separating planning from execution. Eliminates the local-optima detours common in ReAct.   

Cons: 
- Slower time-to-first-action (higher latency). Furthermore, if the initial plan is flawed, the executor will blindly fail unless a robust "Replanner" is built into the loop to rewrite the roadmap. It can also "over-plan" simple tasks, wasting tokens. 

3. Reflection (Reflexion)
Introduced by Shinn et al. (2023), Reflexion gives agents a mechanism for verbal reinforcement learning. Instead of just failing and stopping, the agent critiques its own past failures and writes a "lesson learned" to use on its next attempt.

Implementation:

Actor: The LLM attempts the task and generates a trajectory/output.

Evaluator: An internal LLM (or external compiler/rule engine) scores the output.

Self-Reflection: If the task failed, the LLM analyzes the trajectory to diagnose why it failed, generating a textual summary (e.g., "I failed because I used the wrong variable name in line 4").

Retry: The Actor restarts the task, but this time the verbal reflection is appended to its working memory prompt, guiding it away from the same mistake.

Use Case:
Software engineering (where compiler errors serve as perfect Evaluator signals), complex creative writing (editing drafts), and environments where trial-and-error is safe and cheap.

Trade-offs:

Pros: 
- Dramatically improves success rates on highly complex reasoning and coding tasks by mimicking human trial-and-error.

Cons: 
- Exceptionally expensive and slow. Running multiple failed passes, generating critiques, and retrying consumes massive amounts of tokens. Furthermore, it heavily relies on the LLM being smart enough to self-critique accurately; if the LLM suffers from confirmation bias, it might write a hallucinated reflection and double down on its mistake.

In modern engineering, these are not mutually exclusive. The most robust AI systems layer them together. A common architecture uses Plan-and-Execute to draft the global roadmap, ReAct sub-agents to handle the tool-calling within each individual step, and Reflection to recover if a step fundamentally fails.

Feature.  | 	  ReAct |	Plan-and-Execute|	Reflection (Reflexion)	
Core Paradigm	| Interleaved thinking & doing	| Map out the whole journey, then walk	| Try, fail, diagnose, retry	
Optimization |	Local (Step-by-step)|	Global (End-to-end)	| Iterative (Pass-by-pass)	
Latency & Speed	| Fast to start, but can get bogged down in loops|	Slow to start, predictable execution	| Extremely slow (requires full failures)	
Error Recovery|		Immediate (reacts to the last observation)|		Poor (requires building a Replanner module)|		Excellent (diagnoses root causes of failure)	
Best For...	| QA, browsing, dynamic environments |	Coding an app, deep research|	Fixing code, optimizing writing		

# Reflexion 

evaluation:
- Human evaluation
- Deterministic checks
- LLM as Judge
- 

for attempt in range(max_attempts):
    result = run_agent(task, memory)

    if evaluate(result):
        break

    reflection = reflect_on_failure(task, result)
    memory.append(reflection)