#!/bin/bash

# Update package lists
if [ "$(uname)" == "Darwin" ]; then
    # For macOS
    brew update
    brew install task
elif [ -n "$(command -v apt-get)" ]; then
    # For Debian-based systems
    sudo apt-get update
    sudo apt-get install -y taskwarrior
elif [ -n "$(command -v yum)" ]; then
    # For Red Hat-based systems
    sudo yum install -y task
else
    echo "Unsupported OS"
    exit 1
fi

# Install Python packages
pip install -r requirements.txt
