# Privvy Installation Guide

Install Privvy and start building backends in minutes!

---

## Quick Install (Recommended)

### Method 1: Direct Install (Easy!)

```bash
# Clone the repository
git clone https://github.com/yourname/privvy.git
cd privvy

# Make CLI executable
chmod +x privvy-cli.py

# Add to PATH (optional but recommended)
echo 'export PATH="$PATH:'$(pwd)'"' >> ~/.zshrc
source ~/.zshrc

# Test installation
python3 privvy-cli.py help
```

### Method 2: Global Install (For sharing with friends)

```bash
# Install globally
cd privvy
sudo pip3 install -e .

# Now use anywhere!
privvy help
privvy create-project my-api
```

---

## Create Your First Project

```bash
# Create a new project
python3 privvy-cli.py create-project my-api
# Or if installed globally: privvy create-project my-api

# Navigate to project
cd my-api

# Run migrations
python3 privvy.py migrate.pv

# Run your app
python3 privvy.py src/main.pv
```

**That's it!** You have a working backend! 🎉

---

## Installation for Friends

Share Privvy with your friends! Here are 3 easy ways:

### Option 1: GitHub (Recommended)

```bash
# Clone and run
git clone https://github.com/yourname/privvy.git
cd privvy
python3 privvy-cli.py create-project my-project
```

### Option 2: Zip File

```bash
# Download privvy.zip
unzip privvy.zip
cd privvy
python3 privvy-cli.py create-project my-project
```

### Option 3: pip (Coming Soon!)

```bash
# Future: Install from PyPI
pip install privvy-lang

# Create project
privvy create-project my-api
```

---

## Requirements

**Minimum:**
- Python 3.7 or higher
- pip (Python package manager)

**Optional (for PostgreSQL):**
```bash
pip install psycopg2-binary
```

**Check your installation:**
```bash
python3 --version  # Should be 3.7+
pip3 --version     # Should be installed
```

---

## Platform-Specific Setup

### macOS

```bash
# Install Python (if not installed)
brew install python3

# Clone Privvy
git clone https://github.com/yourname/privvy.git
cd privvy

# Make executable
chmod +x privvy-cli.py

# Add alias (optional)
echo 'alias privvy="python3 $(pwd)/privvy-cli.py"' >> ~/.zshrc
source ~/.zshrc

# Test
privvy help
```

### Linux (Ubuntu/Debian)

```bash
# Install Python
sudo apt update
sudo apt install python3 python3-pip

# Clone Privvy
git clone https://github.com/yourname/privvy.git
cd privvy

# Make executable
chmod +x privvy-cli.py

# Add to PATH
echo 'export PATH="$PATH:'$(pwd)'"' >> ~/.bashrc
source ~/.bashrc

# Test
python3 privvy-cli.py help
```

### Windows

```powershell
# Install Python from python.org

# Clone Privvy
git clone https://github.com/yourname/privvy.git
cd privvy

# Test
python privvy-cli.py help

# Create project
python privvy-cli.py create-project my-api
```

---

## Verify Installation

```bash
# Check Privvy CLI
python3 privvy-cli.py version

# Create test project
python3 privvy-cli.py create-project test-app
cd test-app

# Run migrations
python3 privvy.py migrate.pv

# Run app
python3 privvy.py src/main.pv

# Should see: "✅ Application ready!"
```

---

## IDE Setup (VS Code / Cursor)

### Install Syntax Highlighting

```bash
cd privvy/vscode-privvy
./install.sh

# Restart VS Code/Cursor
```

### Features You Get:
- ✅ Syntax highlighting for `.pv` files
- ✅ Code snippets (type `fun` + Tab)
- ✅ Auto-closing brackets and quotes
- ✅ Code folding
- ✅ Comment toggling (Cmd+/)

---

## Uninstall

```bash
# If installed globally
pip3 uninstall privvy-lang

# Remove directory
rm -rf privvy

# Remove from PATH (if added)
# Edit ~/.zshrc or ~/.bashrc and remove the PATH line
```

---

## Troubleshooting

### "python3: command not found"

**Solution:** Install Python 3

```bash
# macOS
brew install python3

# Linux
sudo apt install python3

# Windows: Download from python.org
```

### "No module named 'psycopg2'"

**Solution:** Install PostgreSQL driver

```bash
pip3 install psycopg2-binary
```

### "Permission denied" when running privvy-cli.py

**Solution:** Make it executable

```bash
chmod +x privvy-cli.py
```

### Can't find privvy command

**Solution:** Use full path or add to PATH

```bash
# Option 1: Use full path
python3 /path/to/privvy/privvy-cli.py help

# Option 2: Add to PATH
echo 'export PATH="$PATH:/path/to/privvy"' >> ~/.zshrc
source ~/.zshrc
```

---

## Distribution for Friends

### Create Distributable Package

```bash
cd privvy

# Create zip file
zip -r privvy-v1.0.0.zip . -x "*.git*" -x "*__pycache__*" -x "*.pyc"

# Share with friends!
# They can: unzip privvy-v1.0.0.zip && cd privvy
```

### Share via GitHub

1. Push to GitHub
2. Friends clone:
   ```bash
   git clone https://github.com/yourname/privvy.git
   cd privvy
   python3 privvy-cli.py create-project my-app
   ```

---

## Next Steps

✅ Installed Privvy  
✅ Created first project  
✅ Ran migrations  

**Now:**
1. Read [ORM_GUIDE.md](ORM_GUIDE.md) - Database operations
2. Check [DATABASE_GUIDE.md](DATABASE_GUIDE.md) - Database basics
3. See [CLI_GUIDE.md](CLI_GUIDE.md) - CLI commands
4. Build something awesome! 🚀

---

## Get Help

- 📖 [Documentation](https://github.com/yourname/privvy)
- 💬 [Issues](https://github.com/yourname/privvy/issues)
- 🌟 [Examples](https://github.com/yourname/privvy/tree/main/examples)

---

**Welcome to Privvy! The easiest backend language ever! 🎉**

