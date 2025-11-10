#!/bin/bash
# Create a new Privvy project

if [ -z "$1" ]; then
    echo "Usage: ./create-project.sh <project-name>"
    echo "Example: ./create-project.sh my-web-app"
    exit 1
fi

PROJECT_NAME=$1
PROJECT_DIR="$PROJECT_NAME"

echo "Creating Privvy project: $PROJECT_NAME"
echo "========================================"
echo ""

# Create project structure
mkdir -p "$PROJECT_DIR/src"
mkdir -p "$PROJECT_DIR/privvy-runtime"

# Copy runtime files
echo "Installing Privvy runtime..."
cp privvy.py "$PROJECT_DIR/privvy-runtime/"
cp lexer.py "$PROJECT_DIR/privvy-runtime/"
cp parser.py "$PROJECT_DIR/privvy-runtime/"
cp interpreter.py "$PROJECT_DIR/privvy-runtime/"
cp ast_nodes.py "$PROJECT_DIR/privvy-runtime/"
cp token_types.py "$PROJECT_DIR/privvy-runtime/"

# Copy template files
echo "Creating project files..."
cp project-template/src/main.pv "$PROJECT_DIR/src/"
cp project-template/run.sh "$PROJECT_DIR/"
cp project-template/README.md "$PROJECT_DIR/"
chmod +x "$PROJECT_DIR/run.sh"

# Create workspace file
cat > "$PROJECT_DIR/$PROJECT_NAME.code-workspace" << EOF
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "files.associations": {
      "*.pv": "privvy"
    },
    "editor.tabSize": 4,
    "editor.insertSpaces": true
  },
  "tasks": {
    "version": "2.0.0",
    "tasks": [
      {
        "label": "Run Privvy App",
        "type": "shell",
        "command": "./run.sh",
        "problemMatcher": [],
        "group": {
          "kind": "build",
          "isDefault": true
        }
      }
    ]
  }
}
EOF

echo ""
echo "✅ Project created successfully!"
echo ""
echo "Next steps:"
echo "  cd $PROJECT_DIR"
echo "  ./run.sh                          # Run the app"
echo "  code $PROJECT_NAME.code-workspace # Open in VS Code"
echo ""
echo "Happy coding! 🎉"

