
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
# 3. Convert our tool registry into model tool specs
# --------------------------------------------------

def build_api_tools(tool_registry):
    api_tools = []

    for name, spec in tool_registry.items():
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
                }
            }
        })

    return api_tools


# --------------------------------------------------
# 4. System instructions
# --------------------------------------------------

def prepare_model_messages(history):
    system_message = {
        "role": "system",
        "content": (
            "You are a service troubleshooting assistant. "
            "Investigate problems using the available tools. "
            "Inspect each tool observation before choosing "
            "your next action. Use the observations to explain "
            "the likely cause and suggest safe next steps. "
            "Do not claim to have performed actions you did not perform."
        )
    }

    return [system_message, *history]


# --------------------------------------------------
# 5. Call the model
# --------------------------------------------------

def call_model(history, api_tools):
    model_messages = prepare_model_messages(history)

    print("\nMESSAGES SENT TO MODEL")
    print(json.dumps(model_messages, indent=2))

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=model_messages,
        tools=api_tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    print("\nMODEL RESPONSE")
    print(message.model_dump_json(indent=2))

    return message


# --------------------------------------------------
# 6. ReAct runtime
# --------------------------------------------------

def run_react_agent(user_question, conversation_history=None, max_steps=5):
    if max_steps < 1:
        raise ValueError("max_steps must be at least 1")

    if conversation_history is None:
        conversation_history = []

    conversation_history.append({
        "role": "user",
        "content": user_question
    })

    api_tools = build_api_tools(tools)

    # Runtime state: number of tools actually executed.
    tool_steps = 0

    # Runtime policy: the first tool must be the health check.
    first_tool = "check_service_health"

    while True:
        print("\n" + "=" * 60)
        print(f"REACT CYCLE | Tool steps used: {tool_steps}/{max_steps}")
        print("=" * 60)

        message = call_model(
            conversation_history,
            api_tools,
        )

        tool_calls = message.tool_calls or []

        # No tool call means the model has produced its final answer.
        if not tool_calls:
            if tool_steps == 0:
                raise RuntimeError(
                    "Model did not request the required initial health check."
                )

            answer = message.content or ""

            conversation_history.append({
                "role": "assistant",
                "content": answer
            })

            print("\nFINAL ANSWER")
            print(answer)

            return answer

        # Enforce one tool call per reasoning cycle.
        # If the model returns multiple calls, execute only the first.
        selected_call = tool_calls[0]

        if len(tool_calls) > 1:
            print(
                f"\nRuntime policy: model requested {len(tool_calls)} "
                "tools; executing only the first."
            )

        tool_name = selected_call.function.name
        tool_call_id = selected_call.id

        # Validate the tool name before executing it.
        if tool_name not in tools:
            raise ValueError(f"Unknown tool requested: {tool_name}")

        # Enforce the maximum number of tool executions.
        if tool_steps >= max_steps:
            raise RuntimeError(
                f"Maximum tool steps reached: {max_steps}"
            )

        # Parse and execute exactly one tool.
        arguments = json.loads(selected_call.function.arguments)

        print(f"\nACTION {tool_steps + 1}: {tool_name}")
        print("Arguments:", arguments)

        observation = tools[tool_name]["function"](**arguments)

        tool_steps += 1

        print("\nOBSERVATION")
        print(json.dumps(observation, indent=2))

        # Add only the selected tool call to the conversation.
        # This keeps the assistant/tool-call history consistent.
        conversation_history.append({
            "role": "assistant",
            "content": message.content,
            "tool_calls": [
                selected_call.model_dump(exclude_none=True)
            ]
        })

        # The observation is now available to the next model call.
        conversation_history.append({
            "role": "tool",
            "tool_call_id": tool_call_id,
            "content": json.dumps(observation)
        })

        # Loop back to the model. It sees the previous observation
        # and decides what to do next.


# --------------------------------------------------
# 7. Run the agent
# --------------------------------------------------

if __name__ == "__main__":
    history = []

    run_react_agent(
        user_question=(
            "Why is the order-service failing? "
            "Investigate and suggest a fix."
        ),
        conversation_history=history,
        max_steps=5
    )
