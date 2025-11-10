#!/bin/bash
# Run the Privvy application

cd "$(dirname "$0")"

if [ ! -d "privvy-runtime" ]; then
    echo "Error: privvy-runtime directory not found!"
    echo "Please copy the Privvy runtime files to privvy-runtime/"
    exit 1
fi

python3 privvy-runtime/privvy.py src/main.pv

