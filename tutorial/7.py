
import os
import json
from openai import OpenAI


# --------------------------------------------------
# 1. Configure Groq client
# --------------------------------------------------

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)


# --------------------------------------------------
# 2. Define tool implementations and specifications
# --------------------------------------------------

def check_service_health(service: str):
    print(f"\n[Executing tool] check_service_health({service})")

    # Simulated monitoring result
    return {
        "service": service,
        "status": "unhealthy",
        "database_connections": "100/100",
        "finding": "Database connection pool exhausted"
    }


def get_recent_errors(service: str):
    print(f"\n[Executing tool] get_recent_errors({service})")

    # Simulated log results
    return {
        "service": service,
        "errors": [
            "Database connection timeout",
            "Failed to acquire connection from pool",
            "Request timed out after 30 seconds"
        ]
    }


# Tool descriptions are provided to the model.
# Python functions are executed by the runtime.
tools = {
    "check_service_health": {
        "description": (
            "Check service health and database connection metrics."
        ),
        "parameters": {
            "service": {
                "type": "string",
                "description": "Name of the service to check"
            }
        },
        "function": check_service_health
    },
    "get_recent_errors": {
        "description": (
            "Retrieve recent error logs for a service."
        ),
        "parameters": {
            "service": {
                "type": "string",
                "description": "Name of the service"
            }
        },
        "function": get_recent_errors
    }
}


# --------------------------------------------------
# 3. Prepare model messages
# --------------------------------------------------

def prepare_model_messages(messages):
    system_message = {
        "role": "system",
        "content": (
            "You are a service troubleshooting assistant. "
            "Investigate the user's problem using the available tools. "
            "First call check_service_health. "
            "Inspect its observation before deciding what to do next. "
            "If the service is unhealthy, call get_recent_errors "
            "in a subsequent model turn. Do not call both tools "
            "in the same turn. Use the observations to explain "
            "the likely cause and suggest safe next steps. "
            "Do not claim to have performed actions you did not perform."
        )
    }

    return [system_message, *messages]


# --------------------------------------------------
# 4. Call the real LLM
# --------------------------------------------------

def call_model(messages, tool_specs):
    # Convert our tool registry into API tool definitions.
    api_tools = []

    for name, spec in tool_specs.items():
        properties = {
            param: {
                "type": definition["type"],
                "description": definition["description"]
            }
            for param, definition in spec["parameters"].items()
        }

        api_tools.append({
            "type": "function",
            "function": {
                "name": name,
                "description": spec["description"],
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": list(properties.keys()),
                    "additionalProperties": False
                },
                "strict": True
            }
        })

    model_messages = prepare_model_messages(messages)

    print("\n" + "=" * 60)
    print("CONVERSATION HISTORY SENT TO MODEL")
    print("=" * 60)
    print(json.dumps(model_messages, indent=2))

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=model_messages,
        tools=api_tools,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message
    result = assistant_message.model_dump(exclude_none=True)

    print("\nMODEL RESPONSE")
    print(json.dumps(result, indent=2))

    return result


# --------------------------------------------------
# 5. ReAct agent runtime
# --------------------------------------------------

def run_react_agent(user_question, conversation_history, max_steps=5):
    conversation_history.append({
        "role": "user",
        "content": user_question
    })

    for step in range(max_steps):
        print(f"\n{'#' * 60}")
        print(f"REACT STEP {step + 1}")
        print(f"{'#' * 60}")

        # REASON: ask the model what to do next.
        response = call_model(conversation_history, tools)

        # Record the complete assistant response.
        conversation_history.append(response)

        tool_calls = response.get("tool_calls")

        # No action requested: the model has finished.
        if not tool_calls:
            answer = response.get("content") or ""
            print("\nFINAL ANSWER")
            print(answer)
            return answer

        # ACT: execute the requested tools.
        for tool_call in tool_calls:
            tool_name = tool_call["function"]["name"]
            arguments = json.loads(
                tool_call["function"]["arguments"]
            )

            tool = tools.get(tool_name)

            if tool is None:
                raise ValueError(f"Unknown tool: {tool_name}")

            print(f"\nACTION: {tool_name}")
            print("Arguments:", arguments)

            observation = tool["function"](**arguments)

            # OBSERVE: return the result to the model.
            print("OBSERVATION:")
            print(json.dumps(observation, indent=2))

            conversation_history.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "content": json.dumps(observation)
            })

        # Continue the loop. The next model call receives
        # the tool result and can choose its next action.

    raise RuntimeError(
        f"ReAct agent exceeded max steps: {max_steps}"
    )


# --------------------------------------------------
# 6. Run the agent
# --------------------------------------------------

if __name__ == "__main__":
    conversation_history = []

    run_react_agent(
        "Why is the order-service failing? Investigate and "
        "suggest a fix.",
        conversation_history
    )
