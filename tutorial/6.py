

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
    
    print("\n" + "=" * 60)
    print("CONVERSATION HISTORY SENT TO MODEL")
    print("=" * 60)
    print(json.dumps(messages, indent=2, ensure_ascii=False))
    print("=" * 60)
    
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

    print("\nTOOLS SENT TO MODEL:")
    print(json.dumps(api_tools, indent=2))
    
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

def run_agent(user_question, conversation_history, max_steps=5):
    conversation_history.append({
        "role": "user",
        "content": user_question
    })

    for _ in range(max_steps):
        response = call_model(conversation_history, tools)

        conversation_history.append(response)

        if not response.get("tool_calls"):
            return response["content"]

        for tool_call in response["tool_calls"]:
            tool_name = tool_call["function"]["name"]
            arguments = json.loads(
                tool_call["function"]["arguments"]
            )

            tool = tools.get(tool_name)
            if tool is None:
                raise ValueError(f"Unknown tool: {tool_name}")

            result = tool["function"](**arguments)

            conversation_history.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "content": str(result)
            })

    raise RuntimeError(
        f"Agent exceeded max steps: {max_steps}"
    )


# Create conversation state once and reuse it
conversation_history = []

# 5. Run the agent
'''print(run_agent(
    "What is the sum of 5 and ?",
    conversation_history
))'''

print(run_agent(
    "What is the modulo of 12 and 7?",
    conversation_history
))

print(run_agent(
    "Now multiply that result by 3.",
    conversation_history
))


