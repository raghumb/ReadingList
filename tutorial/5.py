

import json
import re
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

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


def call_model(messages, tool_specs):
    # Convert your tool registry into the schema expected by the API.
    api_tools = []

    for name, spec in tool_specs.items():
        properties = {
            param: {
                "type": "number",
                "description": description
            }
            for param, description in spec["parameters"].items()
        }

        api_tools.append({
            "type": "function",
            "function": {
                "name": name,
                "description": spec["description"],
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": list(spec["parameters"].keys()),
                    "additionalProperties": False
                },
                "strict": True
            }
        })

    # Call the real LLM.
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=api_tools,
        tool_choice="auto"
    )

    # Convert the model response into the dictionary format
    # already expected by your agent runtime.
    print('-----Response from model is---')
    print(response.choices[0].message)
    return response.choices[0].message.model_dump(
        exclude_none=True
    )

    
    
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
        response = call_model(messages, tools)

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
