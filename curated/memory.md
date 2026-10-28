
https://github.com/pguso/ai-agents-from-scratch/blob/main/examples/08_simple-agent-with-memory/CONCEPT.md

# Memory Strategies


1. Episodic Memory
Store specific events and conversations:

- "On 2025-01-15, user asked about Python"
- "User struggled with async concepts"

2. Semantic Memory
Store facts and knowledge:

- "User is a software engineer"
- "User prefers TypeScript over JavaScript"

3. Procedural Memory
Store how-to information:

- "User's workflow: design → code → test"
- "User's preferred tools: VS Code, Git"



# Challenges & Solutions
## Challenge 1: Memory Bloat
Problem: Too many memories slow down agent Solution:

Importance scoring
Periodic cleanup
Summary compression

## Challenge 2: Conflicting Information
Problem: "User likes pizza" vs "User is vegan" Solution:

Timestamps for recency
Explicit updates
Conflict resolution logic

## Challenge 3: Privacy
Problem: Sensitive information in memory Solution:

Encryption at rest
Access controls
Expiration policies
Key Concepts

# How to store


1. Persistence
Memory survives:

Application restarts
System reboots
Time gaps

2. Context Augmentation
Memories enhance system prompt:

Prompt = Base + Memories + User Input

3. Agent-Driven Storage
Agent decides what to remember:

# Evolution Path
1. Stateless → Each interaction independent
2. Session memory → Remember during conversation
3. Persistent memory → Remember across sessions
4. Distributed memory → Share across instances
5. Semantic search → Find relevant memories

Best Practices
- Structure memory: Use types (facts, preferences, events)
- Add timestamps: Know when information was saved
- Enable updates: Allow overwriting old information
- Implement search: Find relevant memories efficiently
- Monitor size: Prevent unbounded growth


