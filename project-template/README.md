# My Privvy Project

A project built with the Privvy programming language.

## Setup

1. Make sure you have the Privvy runtime in the `privvy-runtime/` folder
2. Install VS Code extension for syntax highlighting (optional)

## Running the Project

```bash
# Run the main application
./run.sh

# Or manually
python3 privvy-runtime/privvy.py src/main.pv
```

## Project Structure

```
.
├── src/
│   └── main.pv          # Main application file
├── privvy-runtime/       # Privvy language interpreter
├── run.sh               # Run script
└── README.md            # This file
```

## Development

### VS Code Setup

1. Open this folder in VS Code
2. Install the Privvy extension (see `../vscode-privvy/`)
3. Open any `.pv` file and enjoy syntax highlighting
4. Press `Cmd+Shift+B` to run files

### Adding New Files

Create new `.pv` files in the `src/` directory:

```bash
touch src/utils.pv
```

### Code Examples

See the `examples/` folder in the main Privvy directory.

## Language Features

- Variables and data types
- Functions with closures
- Classes with inheritance
- Control flow (if/else, loops)
- Arrays
- Built-in functions

## Next Steps

- [ ] Build your application logic
- [ ] Create classes for your domain
- [ ] Add utility functions
- [ ] Test your code in the REPL
- [ ] Deploy your application

Happy coding! 🚀

