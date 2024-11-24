import requests

# URL for the local Flask server
url = 'http://127.0.0.1:50000/receive_message'

# JSON payload with the number to receive prime factorization for
payload = {"number": "26"}

# Send an http POST request and receive the response - i.e. an example call
response = requests.post(url, json=payload)

# Do something with the response
print("Server response:", response.json(), "Status Code:", response.status_code)
