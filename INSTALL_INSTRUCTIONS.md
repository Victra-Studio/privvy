# Install Privvy - Simple Guide

## 🚀 Quick Install (3 commands!)

```bash
# 1. Clone the repository
git clone https://github.com/Victra-Studio/privvy.git

# 2. Go into directory
cd privvy

# 3. Run installer
./install.sh
```

That's it! Now you can use `privvy` anywhere! 🎉

---

## After Installation

### Create Your First Project

```bash
# Create new project
privvy create-project my-api

# Navigate to it
cd my-api

# Run migrations
privvy run migrate.pv

# Run the app
privvy run src/main.pv
```

**Done! You have a working backend!** 🚀

---

## Verification

Test that Privvy is installed:

```bash
# Check version
privvy version

# Get help
privvy help

# Create test project
privvy create-project test-app
```

---

## Troubleshooting

### Command not found: privvy

Add `/usr/local/bin` to your PATH:

```bash
echo 'export PATH="$PATH:/usr/local/bin"' >> ~/.zshrc
source ~/.zshrc
```

### Permission denied

Run with sudo:

```bash
sudo ./install.sh
```

### Python not found

Install Python 3:

```bash
# macOS (Homebrew)
brew install python3

# Ubuntu/Debian
sudo apt install python3

# Check version
python3 --version
```

---

## Manual Installation (No sudo needed)

If you don't want to install globally:

```bash
# Clone repo
git clone https://github.com/Victra-Studio/privvy.git
cd privvy

# Use directly (no installation)
python3 privvy-cli.py create-project my-api
cd my-api
python3 ../privvy.py migrate.pv
python3 ../privvy.py src/main.pv
```

---

## Uninstall

Remove Privvy from your system:

```bash
sudo rm /usr/local/bin/privvy
sudo rm /usr/local/bin/privvy-db
sudo rm -rf /usr/local/lib/privvy
sudo rm -rf /usr/local/share/privvy
```

---

## Next Steps

After installation:

1. Read `QUICK_START.md` for a tutorial
2. Check `examples/` for working code
3. Read `ORM_GUIDE.md` for database operations
4. Build something awesome!

---

## Share with Friends

Send them this:

```
Install Privvy in 3 commands:

git clone https://github.com/Victra-Studio/privvy.git
cd privvy
./install.sh

Then create your first backend:

privvy create-project my-api
cd my-api
privvy run src/main.pv

That's it! 🚀
```

---

**Questions?** Check the main [README.md](README.md) or open an issue on GitHub!

