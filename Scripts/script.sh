#!/bin/bash

# Get inputs from Python script
repo_url=$1
subdir=$2
env_file_path=$3

# Extract repository name from the URL
repo_name=$(basename "$repo_url" .git)

# Clone the repository
echo "Cloning $repo_url..."
git clone "$repo_url"

# Check if cloning was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to clone repository."
    exit 1
fi

# Navigate into the cloned repository
cd "$repo_name" || { echo "Error: Repository directory not found."; exit 1; }

# Navigate into subdirectory if provided
if [ -n "$subdir" ]; then
    cd "$subdir" || { echo "Error: Subdirectory not found."; exit 1; }
fi

# Move .env file into the correct directory
if [ -f "../$env_file_path" ]; then
    mv "../$env_file_path" .env
    echo "Moved .env file to $(pwd)"
else
    echo "Warning: .env file not found."
fi

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found, skipping dependency installation."
fi

# Check if app.py exists
if [ -f "app.py" ]; then
    echo "Running app.py..."
    python3 app.py
else
    echo "Error: app.py not found in the specified location."
    exit 1
fi
