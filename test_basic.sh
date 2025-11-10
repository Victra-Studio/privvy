#!/bin/bash
# Quick test script to verify all examples work

echo "Testing Privvy Programming Language..."
echo "======================================"
echo ""

for file in examples/*.pv; do
    echo "Running: $file"
    python3 privvy.py "$file"
    echo ""
done

echo "All tests completed!"

