# Privvy Programming Language

**The Easiest Full-Stack Backend Language for Beginners!**

A beginner-friendly programming language with built-in database ORM, making backend development ridiculously simple.

## Why Privvy?

✨ **Easiest Backend Ever** - Build full backends in < 50 lines  
🗄️ **Built-in ORM** - Database operations in 1-2 lines (Prisma-inspired!)  
🚀 **Zero Configuration** - No complex setup, just start coding  
📦 **Database CLI** - Migrate, seed, and manage databases easily  
🎨 **Clean Syntax** - Readable and intuitive  
🏫 **Perfect for Learning** - Great first backend language  

## Language Features

- **Built-in Database ORM**: PostgreSQL & SQLite support out of the box
- **Database CLI Tools**: Migrate and seed with simple commands
- **Easy to Learn**: Simple, intuitive syntax inspired by modern languages
- **Clean Code**: Readable and straightforward
- **Web-Oriented**: Built with web development in mind
- **Object-Oriented**: Full support for classes, inheritance, and encapsulation

## Installation

### Homebrew (macOS - Recommended)

```bash
# Coming soon!
brew tap yourname/privvy
brew install privvy

# Create project
privvy create-project my-api
```

### Quick Install Script

```bash
# One-line install
curl -fsSL https://raw.githubusercontent.com/yourname/privvy/main/install.sh | bash

# Or download and run
git clone https://github.com/yourname/privvy.git
cd privvy
./install.sh
```

### Manual Install

```bash
git clone https://github.com/yourname/privvy.git
cd privvy
chmod +x privvy-cli.py
```

---

## Quick Start

### 🚀 Create a Project in 30 Seconds!

```bash
# 1. Create new project
python3 privvy-cli.py create-project my-api

# 2. Navigate and migrate
cd my-api
python3 privvy.py migrate.pv

# 3. Run your app
python3 privvy.py src/main.pv

# Done! You have a working backend! 🎉
```

### Or Build Manually (60 seconds)

```bash
# 1. Initialize database
python3 privvy-db.py init

# 2. Run migrations
python3 privvy.py db-migrate.pv

# 3. Seed data
python3 privvy.py db-seed.pv
```

### Running Privvy Programs

```bash
# Run a Privvy file
python3 privvy.py examples/hello.pv

# Try the database examples
python3 privvy.py examples/orm_simple.pv
python3 privvy.py examples/blog_backend_orm.pv

# Start interactive REPL
python3 privvy.py
```

### Using Privvy in VS Code

**Option 1: Quick Setup (Open the workspace)**
```bash
# Open the workspace file in VS Code
code privvy.code-workspace
```

**Option 2: Install the Extension**
```bash
cd vscode-privvy
./install.sh
# Restart VS Code
```

**Option 3: Create a New Project**
```bash
# Create a new Privvy project with full setup
./create-project.sh my-app
cd my-app
code my-app.code-workspace
```

For detailed VS Code setup, see [VSCODE_SETUP.md](VSCODE_SETUP.md)

## Database & ORM

Privvy has a **built-in ORM** that makes database programming incredibly simple!

### Define Models (2 lines!)

```privvy
let userFields = dict(["id", "INTEGER PRIMARY KEY AUTOINCREMENT", "name", "TEXT", "email", "TEXT UNIQUE"])
let User = Model("users", userFields)
```

### CRUD Operations (1 line each!)

```privvy
let db = Database("app.db")

// Create
let userId = User.create(db, dict(["name", "Alice", "email", "alice@example.com"]))

// Read
let users = User.all(db)
let user = User.find(db, 1)
let alices = User.findBy(db, "name", "Alice")

// Update
User.update(db, 1, dict(["email", "newemail@example.com"]))

// Delete
User.delete(db, 1)

db.close()
```

### Complete Backend Example

See `examples/blog_backend_orm.pv` - A complete blog backend in < 100 lines!

**Features:**
- Users, Posts, Comments
- Full CRUD operations
- Relationships
- Queries and filters

**Learn More:**
- 📖 [ORM_GUIDE.md](ORM_GUIDE.md) - Complete ORM documentation
- 📖 [DATABASE_GUIDE.md](DATABASE_GUIDE.md) - Database basics
- 📖 [CLI_GUIDE.md](CLI_GUIDE.md) - CLI tool documentation

## Language Syntax Overview

### Variables
```
let name = "World"
let age = 25
let isActive = true
```

### Functions
```
fun greet(name) {
    print("Hello, " + name)
}
```

### Classes
```
class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
    
    fun sayHello() {
        print("Hi, I'm " + this.name)
    }
}
```

### Control Flow
```
if (age > 18) {
    print("Adult")
} else {
    print("Minor")
}

while (count < 10) {
    count = count + 1
}
```

## Project Structure

```
privvy/
├── Core Language
│   ├── privvy.py          # Main entry point
│   ├── lexer.py           # Tokenizer
│   ├── parser.py          # Parser (AST builder)
│   ├── interpreter.py     # Interpreter
│   ├── ast_nodes.py       # AST node definitions
│   └── token_types.py     # Token type definitions
│
├── VS Code Integration
│   ├── vscode-privvy/     # VS Code extension
│   ├── privvy.code-workspace  # Workspace file
│   └── VSCODE_SETUP.md    # Setup guide
│
├── Examples & Templates
│   ├── examples/          # Example programs
│   ├── project-template/  # Project template
│   └── create-project.sh  # Project generator
│
└── Documentation
    ├── README.md          # This file
    ├── GETTING_STARTED.md # Beginner's guide
    └── LANGUAGE_SPEC.md   # Language specification
```

