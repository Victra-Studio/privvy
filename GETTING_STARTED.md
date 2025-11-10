# Getting Started with Privvy

Welcome to Privvy! This guide will help you get started with your new programming language.

## Installation

No installation required! Privvy runs on Python 3.7+, which is likely already installed on your system.

### Check Python Version

```bash
python3 --version
```

## Running Privvy Programs

### Method 1: Run a File

```bash
python3 privvy.py script.pv
```

Or make it executable:

```bash
chmod +x privvy.py
./privvy.py script.pv
```

### Method 2: Interactive REPL

Start the interactive shell:

```bash
python3 privvy.py
```

This opens the Privvy REPL where you can type code line by line:

```
Privvy Programming Language v0.1.0
Type 'exit' or 'quit' to exit

>>> let name = "World"
>>> print("Hello, " + name)
Hello, World
>>> 
```

## Try the Examples

We've included several example programs:

```bash
# Hello World
python3 privvy.py examples/hello.pv

# Variables
python3 privvy.py examples/variables.pv

# Functions
python3 privvy.py examples/functions.pv

# Classes and OOP
python3 privvy.py examples/classes.pv

# Loops
python3 privvy.py examples/loops.pv

# Conditionals
python3 privvy.py examples/conditionals.pv

# Arrays
python3 privvy.py examples/arrays.pv

# Calculator Demo
python3 privvy.py examples/calculator.pv
```

## Your First Privvy Program

Create a file called `myprogram.pv`:

```privvy
// My First Privvy Program
let name = "Alice"
print("Hello, " + name + "!")

fun greet(person) {
    print("Nice to meet you, " + person)
}

greet(name)
```

Run it:

```bash
python3 privvy.py myprogram.pv
```

## Language Features

### ✅ Currently Implemented

- **Variables**: `let` declarations and assignments
- **Data Types**: Numbers, strings, booleans, null, arrays
- **Operators**: Arithmetic (+, -, *, /, %), comparison (==, !=, <, >, <=, >=), logical (and, or, not)
- **Control Flow**: if/else, while loops, for loops
- **Functions**: First-class functions with parameters and return values
- **Classes**: Full OOP support with constructors, methods, and inheritance
- **Arrays**: Zero-indexed arrays with indexing
- **Built-in Functions**: print, len, str, int, float
- **REPL**: Interactive programming environment

### 🚀 Coming Soon

These features could be added in future versions:

- String interpolation
- Object literals
- Arrow functions
- Destructuring
- Module system (import/export)
- Error handling (try/catch)
- Async/await
- Standard library expansion
- Web API bindings

## Project Structure

```
privvy/
├── privvy.py          # Main entry point
├── lexer.py           # Tokenizer
├── parser.py          # Parser (AST builder)
├── interpreter.py     # Interpreter (executes AST)
├── ast_nodes.py       # AST node definitions
├── token_types.py     # Token type definitions
├── examples/          # Example programs
├── README.md          # Project overview
├── LANGUAGE_SPEC.md   # Language specification
└── GETTING_STARTED.md # This file
```

## Need Help?

- Read the full language specification: `LANGUAGE_SPEC.md`
- Check out the examples in the `examples/` directory
- Experiment in the REPL

## Tips for Learning Privvy

1. **Start with the REPL**: It's great for experimenting with syntax
2. **Read the examples**: They demonstrate best practices
3. **Start simple**: Begin with variables and functions, then move to classes
4. **Experiment**: The language is designed to be intuitive - try things!

## Common Patterns

### Creating a Class

```privvy
class User {
    constructor(username, email) {
        this.username = username
        this.email = email
        this.loggedIn = false
    }
    
    fun login() {
        this.loggedIn = true
        print(this.username + " logged in")
    }
    
    fun logout() {
        this.loggedIn = false
        print(this.username + " logged out")
    }
}

let user = new User("alice", "alice@example.com")
user.login()
```

### Working with Arrays

```privvy
let numbers = [1, 2, 3, 4, 5]

// Iterate with for loop
for (let i = 0; i < len(numbers); i = i + 1) {
    print("Number:", numbers[i])
}

// Modify elements
numbers[0] = 10
print(numbers)
```

### Recursive Functions

```privvy
fun fibonacci(n) {
    if (n <= 1) {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

print(fibonacci(10))
```

Happy coding with Privvy! 🎉

