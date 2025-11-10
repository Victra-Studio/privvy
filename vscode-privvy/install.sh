#!/bin/bash
# Install Privvy extension for VS Code and Cursor

echo "Installing Privvy Language Extension..."
echo "========================================"
echo ""

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Extension directory name
EXT_NAME="privvy-lang-0.1.0"

# Install to VS Code
VSCODE_EXT_DIR="$HOME/.vscode/extensions"
if [ -d "$HOME/.vscode" ] || command -v code &> /dev/null; then
    mkdir -p "$VSCODE_EXT_DIR"
    if [ -d "$VSCODE_EXT_DIR/$EXT_NAME" ]; then
        echo "Removing old VS Code extension..."
        rm -rf "$VSCODE_EXT_DIR/$EXT_NAME"
    fi
    echo "Installing to VS Code: $VSCODE_EXT_DIR/$EXT_NAME"
    cp -r "$SCRIPT_DIR" "$VSCODE_EXT_DIR/$EXT_NAME"
    echo "✅ Installed to VS Code"
fi

# Install to Cursor
CURSOR_EXT_DIR="$HOME/.cursor/extensions"
if [ -d "$HOME/.cursor" ] || command -v cursor &> /dev/null; then
    mkdir -p "$CURSOR_EXT_DIR"
    if [ -d "$CURSOR_EXT_DIR/$EXT_NAME" ]; then
        echo "Removing old Cursor extension..."
        rm -rf "$CURSOR_EXT_DIR/$EXT_NAME"
    fi
    echo "Installing to Cursor: $CURSOR_EXT_DIR/$EXT_NAME"
    cp -r "$SCRIPT_DIR" "$CURSOR_EXT_DIR/$EXT_NAME"
    echo "✅ Installed to Cursor"
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "Next steps:"
echo "1. Reload your editor (Cmd+Shift+P → 'Developer: Reload Window')"
echo "2. Open a .pv file to see syntax highlighting"
echo "3. Type 'fun' and press Tab to try a snippet"
echo ""
echo "Enjoy coding with Privvy!"

