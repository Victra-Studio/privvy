# Homebrew Installation Guide

Install Privvy globally with Homebrew! 🍺

---

## For Users (Installing Privvy)

### Install from Homebrew Tap (Recommended)

```bash
# Add the Privvy tap
brew tap yourname/privvy

# Install Privvy
brew install privvy

# Test installation
privvy version
privvy help
```

### Create Your First Project

```bash
# Create project
privvy create-project my-api

# Navigate and run
cd my-api
python3 privvy.py migrate.pv
python3 privvy.py src/main.pv
```

**Done!** Privvy is now globally available! 🎉

---

## For Maintainers (Publishing to Homebrew)

### Option 1: Personal Tap (Easy!)

Create your own Homebrew tap:

```bash
# 1. Create a tap repository on GitHub
# Name it: homebrew-privvy (important naming!)

# 2. Clone it
git clone https://github.com/yourname/homebrew-privvy.git
cd homebrew-privvy

# 3. Copy the formula
cp /path/to/privvy/privvy.rb Formula/privvy.rb

# 4. Commit and push
git add Formula/privvy.rb
git commit -m "Add Privvy formula"
git push origin main
```

**Now anyone can install with:**
```bash
brew tap yourname/privvy
brew install privvy
```

### Option 2: Official Homebrew (Advanced)

Submit to the official Homebrew repository:

```bash
# 1. Fork homebrew-core
# https://github.com/Homebrew/homebrew-core

# 2. Add your formula
cp privvy.rb Formula/privvy.rb

# 3. Test it
brew install --build-from-source Formula/privvy.rb
brew test privvy
brew audit --strict privvy

# 4. Submit PR to homebrew-core
```

---

## Creating a Release

### Step 1: Tag Your Release

```bash
cd privvy
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### Step 2: Create GitHub Release

1. Go to https://github.com/yourname/privvy/releases
2. Click "Create a new release"
3. Select tag `v1.0.0`
4. Add release notes
5. Publish release

### Step 3: Generate SHA256

```bash
# Download the release tarball
curl -L https://github.com/yourname/privvy/archive/v1.0.0.tar.gz -o privvy-1.0.0.tar.gz

# Generate SHA256
shasum -a 256 privvy-1.0.0.tar.gz

# Copy the hash and update privvy.rb
```

### Step 4: Update Formula

Edit `privvy.rb`:

```ruby
url "https://github.com/yourname/privvy/archive/v1.0.0.tar.gz"
sha256 "PASTE_YOUR_SHA256_HERE"
version "1.0.0"
```

### Step 5: Test Formula

```bash
# Install from local formula
brew install --build-from-source ./privvy.rb

# Test it
privvy version
privvy create-project test-project

# Uninstall
brew uninstall privvy
```

### Step 6: Publish

```bash
# Push formula to your tap
cd homebrew-privvy
cp /path/to/privvy.rb Formula/privvy.rb
git add Formula/privvy.rb
git commit -m "Update Privvy to v1.0.0"
git push origin main
```

---

## Formula Details

### What Gets Installed

```
/opt/homebrew/bin/privvy         # Main CLI
/opt/homebrew/bin/privvy-db      # Database CLI
/opt/homebrew/share/privvy/      # Examples and templates
/opt/homebrew/share/doc/privvy/  # Documentation
```

### Updating the Formula

When you release a new version:

1. Create new git tag
2. Generate new SHA256
3. Update `version` and `sha256` in formula
4. Push to tap repository

Users can then:
```bash
brew update
brew upgrade privvy
```

---

## Testing the Formula

### Local Testing

```bash
# Install from local formula
brew install --build-from-source ./privvy.rb

# Run tests
brew test privvy

# Check for issues
brew audit --strict privvy

# Uninstall
brew uninstall privvy
```

### Common Issues

**Issue:** `SHA256 mismatch`
**Fix:** Regenerate SHA256 from the actual release tarball

**Issue:** `Python not found`
**Fix:** Make sure `depends_on "python@3.11"` is in formula

**Issue:** `Permission denied`
**Fix:** Check that scripts are executable with `chmod +x`

---

## Alternative: Install Script

If Homebrew doesn't work, provide an install script:

```bash
#!/bin/bash
# install-privvy.sh

# Install Privvy globally
PREFIX="${PREFIX:-/usr/local}"

echo "Installing Privvy to $PREFIX..."

# Create directories
sudo mkdir -p "$PREFIX/lib/privvy"
sudo mkdir -p "$PREFIX/bin"
sudo mkdir -p "$PREFIX/share/privvy"

# Copy files
sudo cp privvy.py lexer.py parser.py interpreter.py ast_nodes.py token_types.py "$PREFIX/lib/privvy/"
sudo cp privvy-cli.py privvy-db.py "$PREFIX/lib/privvy/"

# Create symlinks
sudo ln -sf "$PREFIX/lib/privvy/privvy-cli.py" "$PREFIX/bin/privvy"
sudo ln -sf "$PREFIX/lib/privvy/privvy-db.py" "$PREFIX/bin/privvy-db"

# Make executable
sudo chmod +x "$PREFIX/bin/privvy"
sudo chmod +x "$PREFIX/bin/privvy-db"

# Copy examples
sudo cp -r examples "$PREFIX/share/privvy/"
sudo cp -r vscode-privvy "$PREFIX/share/privvy/"

echo "✅ Privvy installed successfully!"
echo ""
echo "Try: privvy help"
```

---

## Distribution Options

### 1. Homebrew Tap (Recommended)
- ✅ Easy to install
- ✅ Auto updates
- ✅ Professional
- ✅ Works on macOS

### 2. PyPI (Python Package Index)
```bash
pip install privvy-lang
privvy create-project my-api
```

### 3. npm (Node Package Manager)
```bash
npm install -g privvy-lang
privvy create-project my-api
```

### 4. Direct Download
```bash
curl -fsSL https://raw.githubusercontent.com/yourname/privvy/main/install.sh | bash
```

---

## Quick Command Reference

**After Homebrew Install:**

```bash
# Create project
privvy create-project my-api

# Run file
privvy run src/main.pv

# Database commands
privvy-db init
privvy-db migrate
privvy-db seed

# Get help
privvy help
privvy-db help

# Check version
privvy version
```

---

## Uninstall

### Homebrew
```bash
brew uninstall privvy
brew untap yourname/privvy
```

### Manual
```bash
sudo rm /usr/local/bin/privvy
sudo rm /usr/local/bin/privvy-db
sudo rm -rf /usr/local/lib/privvy
sudo rm -rf /usr/local/share/privvy
```

---

## Next Steps

1. ✅ Create GitHub repository
2. ✅ Create release (v1.0.0)
3. ✅ Generate SHA256 hash
4. ✅ Update formula with correct URL and SHA256
5. ✅ Create homebrew-privvy tap repository
6. ✅ Push formula to tap
7. ✅ Test installation
8. 🎉 Share with friends!

---

**Questions?** Check the main [README.md](README.md) or [INSTALL.md](INSTALL.md)

