import requests
import uuid
import os

AGENT_URL = os.environ.get("AGENT_URL", "http://localhost:10000/")

def query_agent(query: str) -> str:
    """
    Queries the actual AI agent by replicating the request structure
    from the ai-agent-nextjs project.
    """
    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "tasks/send",
        "params": {
            "id": str(uuid.uuid4()),
            "message": {
                "role": "user",
                "parts": [{"type": "text", "text": query}],
            },
        },
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(AGENT_URL, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        data = response.json()

        parts = data.get("result", {}).get("artifacts", [{}])[0].get("parts", [])
        if parts and parts[0].get("type") == "text":
            return parts[0].get("text", "Agent response did not contain text.")
        else:
            return "Agent returned a response I couldn't understand."

    except requests.exceptions.Timeout:
        print(f"Request to agent at {AGENT_URL} timed out.")
        return "Sorry, the request to the agent timed out."
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to agent at {AGENT_URL}: {e}")
        return "Sorry, I'm having trouble connecting to the agent right now."
    except Exception as e:
        print(f"An unexpected error occurred while querying the agent: {e}")
        return "An unexpected error occurred."

# Encoding fix 