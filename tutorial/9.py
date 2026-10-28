
"""
How to test the safeguards
Try these scenarios one at a time.
Scenario	How to trigger it	Expected behavior
Tool exception	Ask about unavailable-service	Tool returns a structured error observation; the agent can try another tool.
Permission denied	Remove get_recent_errors from allowed_tools	Runtime refuses to execute it and reports permission_denied.
Malformed JSON	Simulate a tool call with arguments like {"service":	Runtime reports malformed_arguments without executing the function.
Missing argument	Simulate {} for a tool requiring service	Runtime reports argument_validation_error.
Unknown tool	Simulate a request for delete_database	Runtime reports unknown_tool without execution.
Repeated failure	Have the model request the same failing tool with the same arguments twice	Runtime stops after the second failure.
Model timeout	Simulate a timeout or temporarily make the API unavailable	Runtime retries within its configured limit, then returns a controlled message.
Too many steps	Set max_steps=2 and keep requesting tools	Runtime refuses further execution after two tool attempts.
For malformed arguments and unknown tools, the simplest way to test deterministically is to call execute_tool() directly. You do not need to persuade the LLM to generate invalid requests

print(execute_tool(
    "check_service_health",
    '{"service":',
    DEFAULT_ALLOWED_TOOLS,
))

print(execute_tool(
    "check_service_health",
    '{}',
    DEFAULT_ALLOWED_TOOLS,
))

print(execute_tool(
    "delete_database",
    '{}',
    DEFAULT_ALLOWED_TOOLS,
))

print(execute_tool(
    "get_recent_errors",
    '{"service": "order-service"}',
    {"check_service_health"},
))


Important limitations to discuss in the tutorial
This is a useful learning implementation, but a few protections need stronger treatment in production:
- Argument validation: the example validates basic types and fields. Complex schemas need recursive validation, constraints, and possibly a dedicated JSON Schema validator.
- Tool permissions: an allowlist controls which functions the agent can invoke, but it does not provide user-level authorization, resource-level access control, or isolation from dangerous side effects.
- Repeated calls: the loop detector catches identical failed calls. A model could still repeat equivalent actions with slightly different arguments, so the step limit remains essential.
- Retries: bounded retries prevent endless attempts, but production retry policies should account for HTTP status codes, rate limits, backoff, and request idempotency.
- Timeouts: the model API timeout does not automatically limit how long a tool function can run. Tools need their own timeouts and cancellation strategy.
- Tool errors: an error observation is evidence that the operation failed, not proof that retrying is safe. In particular, a timed-out write operation may have succeeded remotely despite the missing response.

"""





import os
import json
import time
from collections import defaultdict

from openai import (
    OpenAI,
    APIError,
    APIConnectionError,
    APITimeoutError,
    RateLimitError,
    InternalServerError,
)


# --------------------------------------------------
# 1. Model client
# --------------------------------------------------

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
    timeout=30.0,
    max_retries=0,  # We implement bounded retries ourselves.
)

MODEL = "openai/gpt-oss-120b"
MAX_MODEL_RETRIES = 2
RETRY_DELAY_SECONDS = 1


class ModelCallError(Exception):
    """The model could not produce a response after bounded retries."""


# --------------------------------------------------
# 2. Tools
# --------------------------------------------------

def check_service_health(service):
    print(f"\n[Executing] check_service_health({service})")

    # Simulate a tool that may fail.
    if service == "unavailable-service":
        raise ConnectionError("Simulated monitoring service failure")

    return {
        "service": service,
        "status": "unhealthy",
        "database_connections": "100/100",
        "finding": "Database connection pool exhausted",
    }


def get_recent_errors(service):
    print(f"\n[Executing] get_recent_errors({service})")

    return {
        "service": service,
        "errors": [
            "Database connection timeout",
            "Failed to acquire connection from pool",
            "Request timed out after 30 seconds",
        ],
    }


# Each tool declares its input contract.
tools = {
    "check_service_health": {
        "description": "Check service health and database metrics.",
        "parameters": {
            "service": {
                "type": "string",
                "description": "Name of the service to check",
            }
        },
        "function": check_service_health,
    },
    "get_recent_errors": {
        "description": "Retrieve recent error logs for a service.",
        "parameters": {
            "service": {
                "type": "string",
                "description": "Name of the service",
            }
        },
        "function": get_recent_errors,
    },
}


# Explicit allowlist: the runtime may execute only these tools.
DEFAULT_ALLOWED_TOOLS = {
    "check_service_health",
    "get_recent_errors",
}


# --------------------------------------------------
# 3. Build model tool specifications
# --------------------------------------------------

def build_api_tools(tool_registry):
    api_tools = []

    for name, spec in tool_registry.items():
        properties = {
            param: {
                "type": definition["type"],
                "description": definition["description"],
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
                    "additionalProperties": False,
                },
            },
        })

    return api_tools


# --------------------------------------------------
# 4. Validate tool arguments independently of the model
# --------------------------------------------------

def validate_arguments(tool_name, arguments):
    spec = tools[tool_name]
    parameters = spec["parameters"]

    if not isinstance(arguments, dict):
        raise ValueError("Tool arguments must be a JSON object.")

    expected = set(parameters)
    supplied = set(arguments)

    missing = expected - supplied
    extra = supplied - expected

    if missing:
        raise ValueError(
            f"Missing required arguments: {sorted(missing)}"
        )

    if extra:
        raise ValueError(
            f"Unexpected arguments: {sorted(extra)}"
        )

    # This example supports the types used by its tools.
    for name, definition in parameters.items():
        value = arguments[name]
        expected_type = definition["type"]

        if expected_type == "string":
            valid = isinstance(value, str) and bool(value.strip())
        elif expected_type == "integer":
            valid = isinstance(value, int) and not isinstance(value, bool)
        elif expected_type == "number":
            valid = (
                isinstance(value, (int, float))
                and not isinstance(value, bool)
            )
        elif expected_type == "boolean":
            valid = isinstance(value, bool)
        else:
            raise ValueError(
                f"Unsupported validator type: {expected_type}"
            )

        if not valid:
            raise ValueError(
                f"Argument '{name}' must be a valid {expected_type}."
            )

    return arguments


# --------------------------------------------------
# 5. Execute a tool safely
# --------------------------------------------------

def execute_tool(tool_name, raw_arguments, allowed_tools):
    # Reject unknown tool names before accessing the registry.
    if tool_name not in tools:
        return {
            "ok": False,
            "error": {
                "type": "unknown_tool",
                "message": f"Tool '{tool_name}' is not registered.",
            },
        }

    # Authorization is separate from registration.
    if tool_name not in allowed_tools:
        return {
            "ok": False,
            "error": {
                "type": "permission_denied",
                "message": f"Tool '{tool_name}' is not permitted.",
            },
        }

    # The model supplies a string containing JSON.
    try:
        arguments = json.loads(raw_arguments)
    except (json.JSONDecodeError, TypeError):
        return {
            "ok": False,
            "error": {
                "type": "malformed_arguments",
                "message": "Tool arguments are not valid JSON.",
            },
        }

    try:
        arguments = validate_arguments(tool_name, arguments)
    except ValueError as exc:
        return {
            "ok": False,
            "error": {
                "type": "argument_validation_error",
                "message": str(exc),
            },
        }

    try:
        result = tools[tool_name]["function"](**arguments)

        return {
            "ok": True,
            "data": result,
        }

    except Exception as exc:
        # Log the actual exception locally for debugging.
        print(
            f"[Tool failure] {tool_name}: "
            f"{type(exc).__name__}: {exc}"
        )

        # Give the model a controlled, structured observation.
        # Avoid exposing arbitrary exception details to the model.
        return {
            "ok": False,
            "error": {
                "type": "tool_execution_error",
                "message": (
                    "The tool failed during execution. "
                    "Consider another diagnostic approach or "
                    "explain that the evidence is unavailable."
                ),
            },
        }


# --------------------------------------------------
# 6. Prepare model messages
# --------------------------------------------------

def prepare_model_messages(history):
    system_message = {
        "role": "system",
        "content": (
            "You are a service troubleshooting assistant. "
            "Choose diagnostic tools based on the user's request "
            "and the observations already available. "
            "Inspect tool results before deciding what to do next. "
            "If a tool fails, you may try another appropriate tool "
            "or explain the limitation. Do not repeat a failed "
            "action without a good reason. "
            "Never claim a tool succeeded when it returned an error. "
            "Suggest safe next steps and do not claim to have "
            "performed actions you did not perform."
        ),
    }

    return [system_message, *history]


# --------------------------------------------------
# 7. Call the model with bounded retries
# --------------------------------------------------

def call_model(history, api_tools):
    model_messages = prepare_model_messages(history)

    for attempt in range(MAX_MODEL_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=model_messages,
                tools=api_tools,
                tool_choice="auto",
            )

            return response.choices[0].message

        except (
            APITimeoutError,
            APIConnectionError,
            RateLimitError,
            InternalServerError,
        ) as exc:
            retryable = True
            last_error = exc

        except APIError as exc:
            # Retry server-side API failures, but not ordinary
            # client errors such as invalid requests.
            retryable = (
                getattr(exc, "status_code", None) is not None
                and exc.status_code >= 500
            )
            last_error = exc

        if not retryable:
            raise ModelCallError(
                f"Non-retryable model API error: "
                f"{type(last_error).__name__}"
            ) from last_error

        if attempt < MAX_MODEL_RETRIES:
            delay = RETRY_DELAY_SECONDS * (2 ** attempt)
            print(
                f"[Model API failure] "
                f"{type(last_error).__name__}; "
                f"retrying in {delay}s "
                f"({attempt + 1}/{MAX_MODEL_RETRIES})"
            )
            time.sleep(delay)

    raise ModelCallError(
        f"Model call failed after "
        f"{MAX_MODEL_RETRIES + 1} attempts."
    ) from last_error



# --------------------------------------------------
# 8. ReAct runtime with failure and loop protection
# --------------------------------------------------

def run_react_agent(
    user_question,
    conversation_history=None,
    max_steps=5,
    allowed_tools=None,
):
    if max_steps < 1:
        raise ValueError("max_steps must be at least 1")

    if conversation_history is None:
        conversation_history = []

    if allowed_tools is None:
        allowed_tools = set(DEFAULT_ALLOWED_TOOLS)
    else:
        allowed_tools = set(allowed_tools)

    unknown_permissions = allowed_tools - set(tools)
    if unknown_permissions:
        raise ValueError(
            f"Unknown tools in allowlist: {sorted(unknown_permissions)}"
        )

    conversation_history.append({
        "role": "user",
        "content": user_question,
    })

    api_tools = build_api_tools(tools)

    # Counts every tool attempt, including invalid or denied calls.
    tool_steps = 0

    # Tracks how often the same tool action fails.
    failed_calls = defaultdict(int)

    while True:
        print("\n" + "=" * 60)
        print(f"REACT CYCLE | Tool attempts: {tool_steps}/{max_steps}")
        print("=" * 60)

        # Model API failures are handled separately from tool failures.
        try:
            message = call_model(conversation_history, api_tools)
        except ModelCallError as exc:
            print(f"\n[Agent stopped] {exc}")

            answer = (
                "I couldn't complete the investigation because the "
                "model service failed after the permitted retries. "
                "Please try again later."
            )

            conversation_history.append({
                "role": "assistant",
                "content": answer,
            })

            return answer

        tool_calls = message.tool_calls or []

        # No tool calls means the model has finished.
        if not tool_calls:
            answer = message.content or (
                "The model returned no final answer."
            )

            conversation_history.append({
                "role": "assistant",
                "content": answer,
            })

            print("\nFINAL ANSWER")
            print(answer)

            return answer

        # Enforce one tool execution per reasoning cycle.
        selected_call = tool_calls[0]

        if len(tool_calls) > 1:
            print(
                f"[Runtime policy] Model requested {len(tool_calls)} "
                "tools. Only the first will be executed."
            )

        tool_name = selected_call.function.name
        raw_arguments = selected_call.function.arguments or ""

        # Stop before executing another tool if the budget is exhausted.
        if tool_steps >= max_steps:
            answer = (
                f"Investigation stopped after reaching the limit of "
                f"{max_steps} tool attempts. The available evidence "
                "may be incomplete."
            )

            conversation_history.append({
                "role": "assistant",
                "content": answer,
            })

            print(f"\n[Agent stopped] {answer}")
            return answer

        print(f"\nACTION {tool_steps + 1}: {tool_name}")
        print("Raw arguments:", raw_arguments)

        observation = execute_tool(
            tool_name,
            raw_arguments,
            allowed_tools,
        )

        # Invalid calls count too, so they cannot bypass the step limit.
        tool_steps += 1

        print("\nOBSERVATION")
        print(json.dumps(observation, indent=2))

        # Append only the tool call that the runtime actually selected.
        conversation_history.append({
            "role": "assistant",
            "content": message.content,
            "tool_calls": [
                selected_call.model_dump(exclude_none=True)
            ],
        })

        # The next model request receives this exact observation.
        conversation_history.append({
            "role": "tool",
            "tool_call_id": selected_call.id,
            "content": json.dumps(observation),
        })

        # Detect repeated failures of the same action.
        if not observation["ok"]:
            try:
                normalized_arguments = json.dumps(
                    json.loads(raw_arguments),
                    sort_keys=True,
                )
            except (json.JSONDecodeError, TypeError):
                normalized_arguments = raw_arguments

            signature = (tool_name, normalized_arguments)
            failed_calls[signature] += 1

            if failed_calls[signature] >= 2:
                answer = (
                    f"Investigation stopped because the same tool "
                    f"action failed {failed_calls[signature]} times: "
                    f"{tool_name}. No further attempt was made."
                )

                conversation_history.append({
                    "role": "assistant",
                    "content": answer,
                })

                print(f"\n[Agent stopped] {answer}")
                return answer

        # Otherwise, continue. The model chooses its next action
        # using the observation now stored in conversation_history.


# --------------------------------------------------
# 9. Run the agent
# --------------------------------------------------

if __name__ == "__main__":
    history = []

    run_react_agent(
        user_question=(
            "Why is the order-service failing? "
            "Investigate and suggest a fix."
        ),
        conversation_history=history,
        max_steps=5,
        allowed_tools={
            "check_service_health",
            "get_recent_errors",
        },
    )
    
    # Test an invalid service
    run_react_agent(
            user_question=(
                "Why is the unavailable-service failing? "
                "Investigate and suggest a fix."
            ),
            conversation_history=history,
            max_steps=5,
            allowed_tools={
                "check_service_health",
                "get_recent_errors",
            },
        )
