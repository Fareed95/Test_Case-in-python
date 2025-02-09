import subprocess
import os
import time
import requests
from requests_url import send_request

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
subprocess.run(["./building.sh", repo_url, subdir, env_file_path], check=True)

# Run the app in another terminal
process = subprocess.Popen(["./running.sh", repo_url, subdir], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()

send_request(repo_url=repo_url)