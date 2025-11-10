# Privvy VS Code Extension

This extension provides language support for Privvy in Visual Studio Code.

## Features

- ✅ Syntax highlighting for `.pv` files
- ✅ Code snippets for common patterns
- ✅ Auto-closing brackets and quotes
- ✅ Comment toggling (Cmd+/)
- ✅ Code folding

## Installation

### Option 1: Install Locally (Recommended)

1. Open VS Code
2. Go to Extensions (Cmd+Shift+X)
3. Click the "..." menu at the top right
4. Select "Install from VSIX..."
5. Navigate to the `vscode-privvy` folder
6. Select the folder (or package it first)

### Option 2: Quick Setup (No Installation)

Copy the extension folder to your VS Code extensions directory:

```bash
# macOS/Linux
cp -r vscode-privvy ~/.vscode/extensions/privvy-lang-0.1.0

# Restart VS Code
```

### Option 3: Workspace-only Setup

1. Open the Privvy project folder in VS Code
2. The extension files are already in place
3. VS Code will automatically recognize `.pv` files

## Code Snippets

Type these prefixes and press Tab:

- `let` - Variable declaration
- `fun` - Function declaration
- `class` - Class declaration
- `if` - If statement
- `ifelse` - If-else statement
- `while` - While loop
- `for` - For loop
- `print` - Print statement
- `constructor` - Constructor
- `method` - Class method
- `new` - New instance
- `array` - Array declaration

## Syntax Highlighting

The extension provides syntax highlighting for:

- Keywords: `let`, `fun`, `class`, `if`, `else`, `while`, `for`, `return`, etc.
- Operators: `+`, `-`, `*`, `/`, `==`, `!=`, `and`, `or`, etc.
- Strings: Double and single quoted
- Numbers: Integers and floats
- Comments: `//`
- Built-in functions: `print`, `len`, `str`, `int`, `float`
- Classes and constructors

## Running Privvy Files

See the main project README for instructions on running Privvy files.

In VS Code, you can:
1. Open the integrated terminal (Ctrl+`)
2. Run: `python3 privvy.py yourfile.pv`

Or set up a build task (see workspace setup below).

## Development

To modify the extension:

1. Edit the files in `vscode-privvy/`
2. Reload VS Code to see changes
3. Press F5 to debug the extension

## Files

- `package.json` - Extension manifest
- `language-configuration.json` - Language features (brackets, comments, etc.)
- `syntaxes/privvy.tmLanguage.json` - Syntax highlighting rules
- `snippets/privvy.json` - Code snippets

