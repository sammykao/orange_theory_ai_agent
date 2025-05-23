import requests
import uuid
import json

url = "http://localhost:10000/"

payload = {
    "jsonrpc": "2.0",
    "id": str(uuid.uuid4()),
    "method": "tasks/send",
    "params": {
        "id": str(uuid.uuid4()),  # Unique task ID
        "message": {
            "role": "user",
            "parts": [
                {   
                    "type": "text",
                    "text": "What are my some classes I can book at the Manhattan-West Village studio?"
                }
            ]
        }
    }
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print("Status Code:", response.status_code)
print("Response:", json.dumps(response.json(), indent=2))
