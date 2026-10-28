
import json


# 1. A tool that the system can execute
def multiply(a, b):
    return a * b


# 2. Fake model that simulates an LLM
def fake_model(messages):
    last_message = messages[-1]

    # If the system has returned a tool result,
    # generate the final answer.
    if last_message["role"] == "tool":
        result = last_message["content"]
        return {
            "type": "final_answer",
            "content": f"The product of 5 and 6 is {result}."
        }

    # Otherwise, request a tool call.
    return {
        "type": "tool_call",
        "tool": "multiply",
        "arguments": {"a": 5, "b": 6}
    }


# 3. Tool registry: maps tool names to Python functions
tools = {
    "multiply": multiply
}


# 4. The agent execution loop
def run_agent(user_question):
    messages = [
        {"role": "user", "content": user_question}
    ]

    while True:
        # Ask the model what to do next
        response = fake_model(messages)

        # Step 5: Model has finished answering
        if response["type"] == "final_answer":
            print("Assistant:", response["content"])
            break
        
        if response["type"] == "tool_call":

            # Step 6: Execute the requested tool
            tool_name = response["tool"]
            arguments = response["arguments"]

            print(f"Model requests: {tool_name}{tuple(arguments.values())}")

            result = tools[tool_name](**arguments)
            print("Tool result:", result)

            # Step 7: Send the tool result back to the model
            messages.append({
                "role": "tool",
                "content": str(result)
            })
            continue
        raise ValueError(f"Unknown Response from model: {response}")


# Run the example
run_agent("What is the product of 5 and 6?")
