#!/bin/bash

# Install python3.8 and virtual environment
sudo apt-get install python3.8 python3.8-venv

# Create a virtual environment
python3.8 -m venv ~/.pyenv3_8

# Activate the virtual environment
source ~/.pyenv3_8/bin/activate

# Update pip
pip install --upgrade pip

# Install the pip package in requirements.txt
pip install -r requirements.txt

# Compile the document
build-docs build

# Exit the virtual environment
deactivate
