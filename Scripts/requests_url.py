# Send POST request to Flask app
import requests


api_url = "http://127.0.0.1:8001/generate-roadmap"
data = {"input_value": "i want to learn python","email":"fareedsayed95@gmail.com"}

try:
    response = requests.post(api_url, json=data)
    print("Response from Flask app:", response.text)
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to Flask app. Make sure it's running on port 8001.")
