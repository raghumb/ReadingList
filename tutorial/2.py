

import json
import re


# 1. Define the tool
def multiply(a, b):
    return a * b


# 2. Register available tools
tools = {
    "multiply": multiply
}


# 3. Fake model that simulates an LLM
def fake_model(messages):
    last_message = messages[-1]

    # If the last message is a tool result,
    # return the final answer.
    if last_message["role"] == "tool":
        result = last_message["content"]

        return {
            "role": "assistant",
            "content": f"The The answer is {result}."
        }
    # Extract the user's original question
    user_question = next(
        message["content"]
        for message in messages
        if message["role"] == "user"
    )

    # Extract numbers using regex
    numbers = re.findall(r"-?\d+(?:\.\d+)?", user_question)

    if len(numbers) < 2:
        return {
            "role": "assistant",
            "content": "Please provide two numbers to multiply."
        }

    a, b = map(float, numbers[:2])

    # Return integers as integers, not floats
    a = int(a) if a.is_integer() else a
    b = int(b) if b.is_integer() else b

    # Otherwise, request a tool call.
    return {
        "role": "assistant",
        "tool_calls": [
            {
                "id": "call_123",
                "type": "function",
                "function": {
                    "name": "multiply",
                    "arguments": json.dumps({
                        "a": 5,
                        "b": 6
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
                "content": str(result)
            })
        
    raise RuntimeError(f"Agent exceeded max steps: {max_steps}")


# 5. Run the agent
print(run_agent("What is the product of 5 and ?"))
print(run_agent("What is the product of 5 and 6?"))
