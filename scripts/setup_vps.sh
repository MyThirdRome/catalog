#!/bin/bash
set -e

echo "Updating system..."
sudo apt-get update && sudo apt-get upgrade -y

echo "Installing Python and dependencies..."
sudo apt-get install -y python3 python3-pip python3-venv unzip

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing Python libraries..."
pip install kaggle pandas flask

echo "Setup complete! Don't forget to configure your kaggle.json"
