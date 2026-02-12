#!/bin/bash
set -e

# Ensure we are in the virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Please activate the virtual environment first: source venv/bin/activate"
    exit 1
fi

DATA_DIR="data"
mkdir -p $DATA_DIR

echo "Downloading dataset..."
# Dataset ID from Kaggle URL: paramaggarwal/fashion-product-images-dataset
kaggle datasets download -d paramaggarwal/fashion-product-images-dataset -p $DATA_DIR

echo "Unzipping dataset..."
unzip -q $DATA_DIR/fashion-product-images-dataset.zip -d $DATA_DIR

echo "Cleaning up zip file..."
rm $DATA_DIR/fashion-product-images-dataset.zip

echo "Download complete. Data is in $DATA_DIR"
