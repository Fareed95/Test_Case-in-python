#!/bin/bash

# Get inputs from Python script
repo_url=$1
subdir=$2

# Extract repository name from the URL
repo_name=$(basename "$repo_url" .git)

# Navigate into the cloned repository
cd "$repo_name" || { echo "No"; exit 1; }

# Navigate into subdirectory if provided
if [ -n "$subdir" ]; then
    cd "$subdir" || { echo "No"; exit 1; }
fi

if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Error: Virtual environment not found."
    echo "No"
    exit 1
fi
# Run app.py in a new terminal
if [ -f "app.py" ]; then
    echo "Running app.py..."
    
    # Open in a new terminal based on OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        gnome-terminal -- bash -c "python3 app.py; exec bash"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        osascript -e 'tell application "Terminal" to do script "python3 app.py"'
    elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        start cmd /k "python app.py"
    else
        echo "Unsupported OS"
        exit 1
    fi

    echo "Yes"
else
    echo "No"
    exit 1
fi
