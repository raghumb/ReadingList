

import json
import re


# 1. Define the tools
def modulo(a, b):
    return a % b

def multiply(a, b):
    return a * b


# 2. Register available tools
tools = {
    "multiply": multiply,
    "modulo": modulo
}


# 3. Fake model that simulates an LLM
def fake_model(messages):
    last_message = messages[-1]

    # Generate final answer after receiving tool result
    if last_message["role"] == "tool":
        result = last_message["content"]
        tool_name = last_message["name"]

        if tool_name == "modulo":
            answer = f"The modulo is {result}."
        else:
            answer = f"The product is {result}."

        return {
            "role": "assistant",
            "content": answer
        }

    # Get user's original question
    user_question = next(
        message["content"]
        for message in messages
        if message["role"] == "user"
    )

    # Decide which tool to call
    question = user_question.lower()
    
    
    # naive checking for deciding which tool to use
    if "mod" in question or "modulo" in question:
        tool_name = "modulo"
    else:
        tool_name = "multiply"

    # Extract numbers using regex
    numbers = re.findall(r"-?\d+(?:\.\d+)?", user_question)

    if len(numbers) < 2:
        return {
            "role": "assistant",
            "content": "Please provide two numbers."
        }

    a, b = map(float, numbers[:2])

    # Keep integers as integers
    a = int(a) if a.is_integer() else a
    b = int(b) if b.is_integer() else b

    # Request tool call
    return {
        "role": "assistant",
        "tool_calls": [
            {
                "id": "call_123",
                "type": "function",
                "function": {
                    "name": tool_name,
                    "arguments": json.dumps({
                        "a": a,
                        "b": b
                    })
                }
            }
        ]
    }
    
    
# 4. Agent runtime
def run_agent(user_question, max_steps=5):
    messages = [
        {
            "role": "user",
            "content": user_question
        }
    ]

    for _ in range(max_steps):
        # Ask the model for its next response
        response = fake_model(messages)

        # Record the assistant response
        messages.append(response)

        # If there are no tool calls, the model is done
        if "tool_calls" not in response:
            return response["content"]

        # Execute each requested tool
        for tool_call in response["tool_calls"]:
            tool_name = tool_call["function"]["name"]
            arguments = json.loads(
                tool_call["function"]["arguments"]
            )

            print(f"Model requests: {tool_name}{tuple(arguments.values())}")

            result = tools[tool_name](**arguments)

            print("Tool result:", result)

            # Return the result using the tool-call ID
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "name": tool_name,
                "content": str(result)
            })
        
    raise RuntimeError(f"Agent exceeded max steps: {max_steps}")


# 5. Run the agent
print(run_agent("What is the product of 5 and ?"))
print(run_agent("What is the product of 5 and 6?"))

print(run_agent("What is the modulo of 12 and 7?"))
