import requests
import os
import signal
import subprocess

def extract_repo_name(repo_url):
    """Extracts the repository name from the GitHub URL."""
    return repo_url.rstrip('/').split('/')[-1].replace('.git', '')

def send_request(repo_url):
    """Sends a request to the Flask API and handles user loop."""
    api_url = "http://127.0.0.1:8001/generate-roadmap"
    repo_name = extract_repo_name(repo_url)
    
    while True:
        input_value = input("Enter input value: ").strip()
        email = input("Enter your email: ").strip()
        
        data = {"input_value": input_value, "email": email}
        
        try:
            response = requests.post(api_url, json=data)
            print("Response from Flask app:", response.text)
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to Flask app. Make sure it's running on port 8001.")
        
        user_choice = input("Enter 1 to continue or 0 to exit: ").strip()
        
        if user_choice == "0":
            print("Terminating processes on port 8001 and deleting cloned repository...")
            terminate_port(8001)
            delete_repo_folder(repo_name)
            break

def terminate_port(port):
    """Terminates all processes running on the specified port."""
    try:
        result = subprocess.run(["lsof", "-ti", f":{port}"], stdout=subprocess.PIPE, text=True)
        pids = result.stdout.strip().split("\n")
        for pid in pids:
            if pid:
                os.kill(int(pid), signal.SIGKILL)
                print(f"Terminated process {pid} on port {port}.")
    except Exception as e:
        print(f"Error terminating processes on port {port}: {e}")

def delete_repo_folder(folder_name):
    """Deletes the cloned repository folder."""
    try:
        if os.path.exists(folder_name):
            subprocess.run(["rm", "-rf", folder_name])
            print(f"Deleted folder: {folder_name}")
        else:
            print("Folder does not exist.")
    except Exception as e:
        print(f"Error deleting folder {folder_name}: {e}")
