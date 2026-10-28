

import json
import re

# 1. Define tool specifications and implementations
tools = {
    "multiply": {
        "description": "Multiply two numbers and return their product.",
        "parameters": {
            "a": "First number",
            "b": "Second number"
        },
        "function": lambda a, b: a * b
    },
    "modulo": {
        "description": "Compute the remainder when a is divided by b.",
        "parameters": {
            "a": "The dividend",
            "b": "The divisor"
        },
        "function": lambda a, b: a % b
    }
}


def fake_model(messages, tool_specs):
    last_message = messages[-1]

    # Generate final answer after receiving tool result
    if last_message["role"] == "tool":
        result = last_message["content"]
        tool_name = last_message["name"]

        if tool_name == "add":
            answer = f"The modulo is {result}."
        else:
            answer = f"The product is {result}."

        return {
            "role": "assistant",
            "content": answer
        }

    # Get the user's original question
    user_question = next(
        message["content"]
        for message in messages
        if message["role"] == "user"
    )

    # Give the fake model the available tool specifications.
    # A real LLM would interpret these descriptions.
    available_tools = json.dumps({
        name: {
            "description": spec["description"],
            "parameters": spec["parameters"]
        }
        for name, spec in tool_specs.items()
    })

    print("\nTool specifications given to model:")
    print(available_tools)

    # Simulate the model selecting a tool.
    # This heuristic is only a stand-in for LLM reasoning.
    question = user_question.lower()

    if any(word in question for word in ["modulo", "mod"]):
        tool_name = "modulo"
    elif any(word in question for word in ["multiply", "product", "times"]):
        tool_name = "multiply"
    else:
        return {
            "role": "assistant",
            "content": "I cannot determine which tool to use."
        }

    # Extract numbers
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

    # Request a tool call
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
        response = fake_model(messages, tools)

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
            
            # Look up the tool implementation
            tool = tools.get(tool_name)

            if tool is None:
                raise ValueError(f"Unknown tool: {tool_name}")

            print(f"Model requests: {tool_name}{tuple(arguments.values())}")

            result = tool["function"](**arguments)

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
