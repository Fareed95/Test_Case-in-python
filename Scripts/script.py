import subprocess
import os
import time
import requests

# Ask for GitHub repository URL
repo_url = input("Enter the GitHub repository URL: ").strip()

# Ask for subdirectory (optional)
subdir = input("Enter the subdirectory where app.py is located (leave empty if in root): ").strip()

# Path of existing .env file
env_file_path = "temp_env.env"

# Check if .env file exists
if not os.path.exists(env_file_path):
    print(f"Error: {env_file_path} not found in the script directory.")
    exit(1)

print(f"Using existing {env_file_path} file.")

# Call the shell script and pass repo URL, subdir name
subprocess.Popen(["./script.sh", repo_url, subdir, env_file_path])

# Wait for the Flask app to start
time.sleep(300)  # Adjust this delay if needed

# Send POST request to Flask app
api_url = "http://127.0.0.1:8001/generate-roadmap"
data = {"input_value": "i want to learn python"}

try:
    response = requests.post(api_url, json=data)
    print("Response from Flask app:", response.text)
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to Flask app. Make sure it's running on port 8001.")
