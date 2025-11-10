#!/bin/bash
# Share Privvy with Friends!
# This script creates a distributable package

echo "📦 Creating Privvy distribution package..."
echo ""

# Create distribution directory
mkdir -p dist
cd dist
rm -rf privvy 2>/dev/null

# Copy Privvy
echo "Copying files..."
cp -r ../ privvy/

# Remove unnecessary files
cd privvy
rm -rf .git __pycache__ *.pyc demo-api test-project
rm -rf */app.db */*.db
rm -rf dist

echo ""
echo "✅ Package created in dist/privvy/"
echo ""
echo "📤 To share with friends:"
echo ""
echo "  Option 1: Zip it"
echo "    cd dist"
echo "    zip -r privvy.zip privvy/"
echo "    # Share privvy.zip"
echo ""
echo "  Option 2: GitHub"
echo "    git push"
echo "    # Friends clone the repo"
echo ""
echo "  Option 3: Direct copy"
echo "    cp -r dist/privvy /path/to/share/"
echo ""
echo "📖 Friends can then:"
echo "    cd privvy"
echo "    python3 privvy-cli.py create-project my-api"
echo ""
echo "🎉 Done!"

