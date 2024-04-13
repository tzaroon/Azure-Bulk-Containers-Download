#!/bin/bash
account_name="<ETNER STORAGE NAME>" # Replace this with your storage Account Name
account_key="ENTER STORAGE ACCOUNT KEY" # Replace with Storage Account Key
local_directory="<ENTER DIRECTORY>" # Define the local directory where data will be downloaded (./ for same folder as python file)

# Creating Environment in python
python3 -m venv path/to/venv

# Define the path to your virtual environment
VENV_PATH="path/to/venv"

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Install dependencies
python3 -m pip install -r requirements.txt  # Adjust requirements.txt as needed

# Run the Python script with arguments
python3 azure_storage.py "$account_name" "$account_key" "$local_directory"

# Deactivate the virtual environment
deactivate
