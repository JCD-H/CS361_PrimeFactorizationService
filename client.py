import requests

# URL for the local Flask server
url = 'http://127.0.0.1:50000/receive_message'

# JSON payload with the message
payload = {"numdber": "19"}

# Send a POST request
response = requests.post(url, json=payload)

# Print the response from the server
print("Server response:", response.json(), "Status Code:", response.status_code)
