#!/usr/bin/env bash

set -e  

export PATH=$PATH:"$(pwd)"

if [ -d "./venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf ./venv
fi

echo "Upgrading pip and setting up virtual environment..."
pip install --upgrade pip --user
python -m venv venv

source ./venv/Scripts/activate

echo "Installing the package..."
pip3 install .

echo "Setup complete. Virtual environment is ready."