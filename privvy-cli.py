#!/usr/bin/env python3
"""
Privvy CLI - The Easiest Backend Language
Create full-stack projects with one command!

Usage:
    privvy create-project <name>
    privvy run <file>
    privvy migrate
    privvy test
"""

import sys
import os
import shutil
from pathlib import Path

VERSION = "1.0.0"

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_banner():
    print(f"{Colors.BLUE}{Colors.BOLD}")
    print("╔════════════════════════════════════════╗")
    print("║         Privvy CLI v" + VERSION + "             ║")
    print("║   The Easiest Backend Language Ever   ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.END}")

def print_success(msg):
    print(f"{Colors.GREEN}✅ {msg}{Colors.END}")

def print_error(msg):
    print(f"{Colors.RED}❌ {msg}{Colors.END}")

def print_info(msg):
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.END}")

def get_privvy_root():
    """Get the root directory of Privvy installation."""
    return Path(__file__).parent.absolute()

def create_project(project_name, template="auth"):
    """Create a new Privvy project."""
    print_info(f"Creating new Privvy project: {project_name}")
    print("")
    
    # Create project directory
    project_path = Path(project_name)
    if project_path.exists():
        print_error(f"Directory '{project_name}' already exists!")
        return False
    
    project_path.mkdir()
    print_success(f"Created directory: {project_name}")
    
    # Get Privvy root
    privvy_root = get_privvy_root()
    
    # Copy core files
    print_info("Copying Privvy runtime...")
    core_files = [
        'privvy.py',
        'lexer.py',
        'parser.py',
        'interpreter.py',
        'ast_nodes.py',
        'token_types.py'
    ]
    
    for file in core_files:
        src = privvy_root / file
        dst = project_path / file
        if src.exists():
            shutil.copy2(src, dst)
    
    print_success("Runtime copied")
    
    # Create project structure
    print_info("Setting up project structure...")
    
    (project_path / "src").mkdir()
    (project_path / "schema").mkdir()
    (project_path / "tests").mkdir()
    
    # Create schema file
    schema_content = '''// schema/schema.pv - Database Schema
// Define your models here (PostgreSQL-compatible)

let User = Model("users", dict(["id", "SERIAL PRIMARY KEY", "username", "TEXT UNIQUE NOT NULL", "email", "TEXT UNIQUE NOT NULL", "password", "TEXT NOT NULL", "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"]))

let Post = Model("posts", dict(["id", "SERIAL PRIMARY KEY", "user_id", "INTEGER NOT NULL", "title", "TEXT NOT NULL", "content", "TEXT", "published", "INTEGER DEFAULT 0", "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"]))
'''
    
    with open(project_path / "schema" / "schema.pv", "w") as f:
        f.write(schema_content)
    
    # Create main app file
    main_content = '''// src/main.pv - Main application entry point
print("🚀 Starting application...")
print("")

// Connect to database
let db = Database("app.db")
// For PostgreSQL: let db = Database("postgresql://user:pass@host:5432/dbname")

// Define models (copy from schema/schema.pv)
let User = Model("users", dict(["id", "SERIAL PRIMARY KEY", "username", "TEXT UNIQUE NOT NULL", "email", "TEXT UNIQUE NOT NULL", "password", "TEXT NOT NULL", "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"]))

// Your application code here
print("✅ Application ready!")
print("💡 Start building your backend!")
print("")

// Example: Get all users
let users = User.all(db)
print("Total users: " + str(len(users)))

db.close()
'''
    
    with open(project_path / "src" / "main.pv", "w") as f:
        f.write(main_content)
    
    # Create migrate script
    migrate_content = '''// migrate.pv - Database migrations
print("=== Running Migrations ===")
print("")

// Connect to database
let db = Database("app.db")
// For PostgreSQL: let db = Database("postgresql://user:pass@host:5432/dbname")

print("📡 Connected to database")
print("")

// Define models (copy from schema/schema.pv)
let User = Model("users", dict(["id", "SERIAL PRIMARY KEY", "username", "TEXT UNIQUE NOT NULL", "email", "TEXT UNIQUE NOT NULL", "password", "TEXT NOT NULL", "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"]))

let Post = Model("posts", dict(["id", "SERIAL PRIMARY KEY", "user_id", "INTEGER NOT NULL", "title", "TEXT NOT NULL", "content", "TEXT", "published", "INTEGER DEFAULT 0", "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"]))

// Run migrations
print("🔨 Creating tables...")
User.migrate(db)
print("  ✓ Created table: users")

Post.migrate(db)
print("  ✓ Created table: posts")

print("")
print("✅ All migrations complete!")
print("")

db.close()
'''
    
    with open(project_path / "migrate.pv", "w") as f:
        f.write(migrate_content)
    
    # Create README
    readme_content = f'''# {project_name}

A Privvy backend project

## Quick Start

### 1. Run Migrations

```bash
python3 privvy.py migrate.pv
```

### 2. Run Application

```bash
python3 privvy.py src/main.pv
```

## Project Structure

```
{project_name}/
├── schema/
│   └── schema.pv       # Database schema (source of truth)
│
├── src/
│   └── main.pv         # Main application
│
├── tests/
│   └── (your tests)
│
├── migrate.pv          # Migration script
├── app.db              # SQLite database (generated)
│
└── privvy.py           # Privvy interpreter
```

## Database

**SQLite (default):** `let db = Database("app.db")`

**PostgreSQL:** `let db = Database("postgresql://user:pass@host:5432/dbname")`

## Learn More

- [Privvy Documentation](https://github.com/yourname/privvy)
- [ORM Guide](https://github.com/yourname/privvy/blob/main/ORM_GUIDE.md)
- [Database Guide](https://github.com/yourname/privvy/blob/main/DATABASE_GUIDE.md)

---

Built with ❤️ using Privvy - The Easiest Backend Language
'''
    
    with open(project_path / "README.md", "w") as f:
        f.write(readme_content)
    
    # Create .gitignore
    gitignore_content = '''# Database
*.db
app.db

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
'''
    
    with open(project_path / ".gitignore", "w") as f:
        f.write(gitignore_content)
    
    print_success("Project structure created")
    print("")
    
    # Print success message
    print(f"{Colors.GREEN}{Colors.BOLD}✨ Project created successfully!{Colors.END}")
    print("")
    print(f"{Colors.BOLD}Next steps:{Colors.END}")
    print(f"  cd {project_name}")
    print(f"  python3 privvy.py migrate.pv")
    print(f"  python3 privvy.py src/main.pv")
    print("")
    print(f"{Colors.BLUE}Happy coding! 🚀{Colors.END}")
    
    return True

def cmd_help():
    """Show help message."""
    print(f"""
{Colors.BOLD}Usage:{Colors.END}
  privvy <command> [options]

{Colors.BOLD}Commands:{Colors.END}
  {Colors.BLUE}create-project <name>{Colors.END}    Create a new Privvy project
  {Colors.BLUE}run <file>{Colors.END}               Run a Privvy file
  {Colors.BLUE}migrate{Colors.END}                  Run database migrations
  {Colors.BLUE}test{Colors.END}                     Run tests
  {Colors.BLUE}version{Colors.END}                  Show version
  {Colors.BLUE}help{Colors.END}                     Show this help message

{Colors.BOLD}Examples:{Colors.END}
  privvy create-project my-api
  privvy run src/main.pv
  privvy migrate

{Colors.BOLD}Learn More:{Colors.END}
  https://github.com/yourname/privvy
    """)

def cmd_run(file_path):
    """Run a Privvy file."""
    if not file_path:
        print_error("Please specify a file to run")
        print_info("Usage: privvy run <file>")
        return
    
    if not os.path.exists(file_path):
        print_error(f"File not found: {file_path}")
        return
    
    print_info(f"Running {file_path}...")
    os.system(f"python3 privvy.py {file_path}")

def cmd_migrate():
    """Run database migrations."""
    if os.path.exists("migrate.pv"):
        print_info("Running migrations...")
        os.system("python3 privvy.py migrate.pv")
    else:
        print_error("migrate.pv not found!")
        print_info("Run this command from your project directory")

def cmd_test():
    """Run tests."""
    if os.path.exists("tests"):
        print_info("Running tests...")
        # Find all test files
        test_files = list(Path("tests").glob("*.pv"))
        if test_files:
            for test_file in test_files:
                print(f"\n{Colors.BOLD}Running {test_file}...{Colors.END}")
                os.system(f"python3 privvy.py {test_file}")
        else:
            print_error("No test files found in tests/")
    else:
        print_error("tests/ directory not found!")

def main():
    print_banner()
    
    if len(sys.argv) < 2:
        cmd_help()
        return
    
    command = sys.argv[1]
    
    if command == "create-project":
        if len(sys.argv) < 3:
            print_error("Please specify a project name")
            print_info("Usage: privvy create-project <name>")
            return
        
        project_name = sys.argv[2]
        create_project(project_name)
    
    elif command == "run":
        file_path = sys.argv[2] if len(sys.argv) > 2 else None
        cmd_run(file_path)
    
    elif command == "migrate":
        cmd_migrate()
    
    elif command == "test":
        cmd_test()
    
    elif command == "version":
        print(f"Privvy v{VERSION}")
    
    elif command in ["help", "--help", "-h"]:
        cmd_help()
    
    else:
        print_error(f"Unknown command: {command}")
        print_info("Run 'privvy help' for usage")

if __name__ == "__main__":
    main()

