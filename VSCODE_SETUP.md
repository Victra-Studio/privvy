# Setting Up Privvy in VS Code

This guide will help you set up the Privvy language in Visual Studio Code for a seamless development experience.

## Quick Setup (5 Minutes)

### Step 1: Install the Extension

Choose one of these methods:

#### Method A: Install to VS Code Extensions (Recommended)

```bash
# Copy the extension to VS Code extensions folder
cp -r vscode-privvy ~/.vscode/extensions/privvy-lang-0.1.0

# Restart VS Code
```

#### Method B: Use the Workspace File (Simplest)

1. Double-click `privvy.code-workspace` to open the project
2. VS Code will recognize `.pv` files automatically

### Step 2: Verify Installation

1. Open any `.pv` file in the `examples/` folder
2. You should see syntax highlighting
3. Try typing `fun` and press Tab - a snippet should appear

### Step 3: Test Running Code

1. Open `examples/hello.pv`
2. Press `Cmd+Shift+B` (Mac) or `Ctrl+Shift+B` (Windows/Linux)
3. Select "Run Privvy File"
4. The output should appear in the terminal

## Features You Get

### 1. Syntax Highlighting

All Privvy keywords, operators, and syntax are beautifully highlighted:
- Keywords in purple
- Strings in orange
- Comments in green
- Functions in yellow
- Numbers in light green

### 2. Code Snippets

Type these and press Tab:

| Snippet | Description |
|---------|-------------|
| `let` | Variable declaration |
| `fun` | Function declaration |
| `class` | Full class with constructor and method |
| `if` | If statement |
| `ifelse` | If-else statement |
| `while` | While loop |
| `for` | For loop |
| `print` | Print statement |
| `new` | Create new instance |

### 3. Auto-Formatting Features

- Auto-close brackets: `{`, `[`, `(`
- Auto-close quotes: `"`, `'`
- Toggle comments with `Cmd+/` or `Ctrl+/`
- Code folding for functions and classes

### 4. Tasks (Keyboard Shortcuts)

Press `Cmd+Shift+B` (or `Ctrl+Shift+B`) and choose:

- **Run Privvy File** - Run the current file
- **Run Privvy REPL** - Start interactive shell
- **Run All Examples** - Test all example files

## Creating a New Privvy Project

### 1. Create Project Folder

```bash
mkdir my-privvy-project
cd my-privvy-project
```

### 2. Copy the Privvy Runtime

```bash
# Copy the interpreter files
cp /Users/apple/Desktop/privvy/privvy.py .
cp /Users/apple/Desktop/privvy/lexer.py .
cp /Users/apple/Desktop/privvy/parser.py .
cp /Users/apple/Desktop/privvy/interpreter.py .
cp /Users/apple/Desktop/privvy/ast_nodes.py .
cp /Users/apple/Desktop/privvy/token_types.py .
```

### 3. Create Your First File

Create `main.pv`:

```privvy
// My Privvy Application
print("Welcome to my app!")

class App {
    constructor(name) {
        this.name = name
    }
    
    fun run() {
        print("Running " + this.name)
    }
}

let myApp = new App("MyApp")
myApp.run()
```

### 4. Run It

```bash
python3 privvy.py main.pv
```

## Advanced VS Code Setup

### Custom Color Theme

Add to your `settings.json`:

```json
{
  "editor.tokenColorCustomizations": {
    "textMateRules": [
      {
        "scope": "keyword.control.privvy",
        "settings": {
          "foreground": "#C586C0"
        }
      },
      {
        "scope": "entity.name.function.privvy",
        "settings": {
          "foreground": "#DCDCAA"
        }
      },
      {
        "scope": "entity.name.type.class.privvy",
        "settings": {
          "foreground": "#4EC9B0"
        }
      }
    ]
  }
}
```

### Keybindings

Add to your `keybindings.json`:

```json
{
  "key": "cmd+r",
  "command": "workbench.action.tasks.runTask",
  "args": "Run Privvy File",
  "when": "editorLangId == privvy"
}
```

Now press `Cmd+R` to run the current Privvy file!

### Debug Configuration

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run Privvy File",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/privvy.py",
      "args": ["${file}"],
      "console": "integratedTerminal"
    }
  ]
}
```

## File Associations

VS Code will automatically recognize `.pv` files as Privvy files. You can also manually set this:

1. Open a `.pv` file
2. Click the language indicator in the bottom right
3. Select "Configure File Association for '.pv'..."
4. Choose "Privvy"

## Troubleshooting

### Syntax Highlighting Not Working

1. Check that the extension is installed
2. Verify the file has a `.pv` extension
3. Try reloading VS Code (Cmd+Shift+P → "Reload Window")
4. Open the workspace file: `privvy.code-workspace`

### Snippets Not Working

1. Make sure you're in a `.pv` file
2. Type the snippet prefix exactly (e.g., `fun`)
3. Press Tab (not Enter)
4. Check IntelliSense is enabled in settings

### Can't Run Files

1. Make sure Python 3 is installed: `python3 --version`
2. Check you're in the correct directory
3. Try running manually: `python3 privvy.py yourfile.pv`

## Building Standalone Projects

Want to share your Privvy project? Create a distributable package:

### Structure

```
my-project/
├── src/
│   ├── main.pv
│   └── utils.pv
├── privvy-runtime/
│   ├── privvy.py
│   ├── lexer.py
│   ├── parser.py
│   ├── interpreter.py
│   ├── ast_nodes.py
│   └── token_types.py
├── run.sh
└── README.md
```

### run.sh

```bash
#!/bin/bash
cd "$(dirname "$0")"
python3 privvy-runtime/privvy.py src/main.pv
```

Make it executable:
```bash
chmod +x run.sh
./run.sh
```

## Tips for Productive Development

1. **Use the REPL** - Quick testing: `python3 privvy.py`
2. **Leverage snippets** - Type shortcuts instead of full code
3. **Split editor** - View multiple `.pv` files side by side
4. **Use terminal** - Keep integrated terminal open
5. **File watchers** - Use VS Code's auto-save feature

## Next Steps

- Create your first project
- Explore the example files
- Customize your VS Code theme
- Share your Privvy code!

Happy coding! 🚀

