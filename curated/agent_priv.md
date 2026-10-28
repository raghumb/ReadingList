
# Levels

- T0 - untrusted input/observation. Summarization, prompt based outputs
- T1 - Read only Agents
- T2 - Controlled execution / modification
- T3 - Privileged or high-impact action


For a production-ready architecture, I would specify these requirements:
1. Least privilege: grant each agent only the permissions required for its task.
2. Explicit delegation: pass a bounded task, permitted tools, resource scope, and expiration to each sub-agent.
3. No implicit privilege escalation: a child agent cannot inherit broader authority than the delegation policy permits.
4. Untrusted-data handling: retrieved documents, tool results, and agent-generated text must not become trusted instructions merely because another agent forwards them.
5. Independent enforcement: the tool gateway must validate authorization even if the agent or orchestrator claims an action is safe.
6. Approval for high-impact actions: require human approval where the risk policy demands it.
7. Auditability: record who initiated an action, which agent executed it, what permissions applied, and which approval authorized it.
8. Revocation and containment: suspend an agent or revoke its credentials when suspicious behavior is detected.

