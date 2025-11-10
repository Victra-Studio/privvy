#!/bin/bash
# Privvy Installation Script
# Quick install: curl -fsSL https://raw.githubusercontent.com/yourname/privvy/main/install.sh | bash

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
VERSION="1.0.0"
PREFIX="${PREFIX:-/usr/local}"
PRIVVY_DIR="$PREFIX/lib/privvy"
BIN_DIR="$PREFIX/bin"
SHARE_DIR="$PREFIX/share/privvy"

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║    Privvy Installer v$VERSION          ║${NC}"
echo -e "${BLUE}║  The Easiest Backend Language Ever    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# Check for required tools
echo -e "${BLUE}Checking requirements...${NC}"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is required but not installed.${NC}"
    echo "Install Python from https://www.python.org/downloads/"
    exit 1
fi

echo -e "${GREEN}✅ Python 3 found${NC}"

# Check for sudo access
if [ "$EUID" -ne 0 ] && [ ! -w "$PREFIX" ]; then
    SUDO="sudo"
    echo -e "${YELLOW}⚠️  Installation requires sudo access${NC}"
else
    SUDO=""
fi

# Create directories
echo -e "${BLUE}Creating directories...${NC}"
$SUDO mkdir -p "$PRIVVY_DIR"
$SUDO mkdir -p "$BIN_DIR"
$SUDO mkdir -p "$SHARE_DIR"

# Download or copy Privvy files
echo -e "${BLUE}Installing Privvy...${NC}"

if [ -d "$(pwd)/privvy.py" ]; then
    # Local installation
    echo "Installing from local directory..."
    $SUDO cp privvy.py lexer.py parser.py interpreter.py ast_nodes.py token_types.py "$PRIVVY_DIR/"
    $SUDO cp privvy-cli.py privvy-db.py "$PRIVVY_DIR/"
    
    if [ -d "examples" ]; then
        $SUDO cp -r examples "$SHARE_DIR/"
    fi
    
    if [ -d "vscode-privvy" ]; then
        $SUDO cp -r vscode-privvy "$SHARE_DIR/"
    fi
else
    # Remote installation
    echo "Downloading from GitHub..."
    REPO_URL="https://github.com/yourname/privvy/archive/refs/tags/v$VERSION.tar.gz"
    
    TMP_DIR=$(mktemp -d)
    cd "$TMP_DIR"
    
    curl -fsSL "$REPO_URL" -o privvy.tar.gz
    tar -xzf privvy.tar.gz
    cd "privvy-$VERSION"
    
    $SUDO cp privvy.py lexer.py parser.py interpreter.py ast_nodes.py token_types.py "$PRIVVY_DIR/"
    $SUDO cp privvy-cli.py privvy-db.py "$PRIVVY_DIR/"
    $SUDO cp -r examples "$SHARE_DIR/" 2>/dev/null || true
    $SUDO cp -r vscode-privvy "$SHARE_DIR/" 2>/dev/null || true
    
    cd /
    rm -rf "$TMP_DIR"
fi

echo -e "${GREEN}✅ Files installed${NC}"

# Create wrapper scripts
echo -e "${BLUE}Creating command-line tools...${NC}"

# Privvy CLI wrapper
cat << 'EOF' | $SUDO tee "$BIN_DIR/privvy" > /dev/null
#!/bin/bash
PRIVVY_LIB="$(dirname "$0")/../lib/privvy"
exec python3 "$PRIVVY_LIB/privvy-cli.py" "$@"
EOF

# Privvy DB wrapper
cat << 'EOF' | $SUDO tee "$BIN_DIR/privvy-db" > /dev/null
#!/bin/bash
PRIVVY_LIB="$(dirname "$0")/../lib/privvy"
exec python3 "$PRIVVY_LIB/privvy-db.py" "$@"
EOF

# Make executable
$SUDO chmod +x "$BIN_DIR/privvy"
$SUDO chmod +x "$BIN_DIR/privvy-db"
$SUDO chmod +x "$PRIVVY_DIR/privvy-cli.py"
$SUDO chmod +x "$PRIVVY_DIR/privvy-db.py"

echo -e "${GREEN}✅ Commands created${NC}"

# Check if bin directory is in PATH
echo ""
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo -e "${YELLOW}⚠️  $BIN_DIR is not in your PATH${NC}"
    echo "Add it to your PATH by running:"
    echo ""
    echo "  echo 'export PATH=\"\$PATH:$BIN_DIR\"' >> ~/.zshrc"
    echo "  source ~/.zshrc"
    echo ""
fi

# Installation complete
echo -e "${GREEN}${BOLD}✨ Privvy installed successfully!${NC}"
echo ""
echo -e "${BLUE}Quick Start:${NC}"
echo "  privvy create-project my-api"
echo "  cd my-api"
echo "  python3 privvy.py migrate.pv"
echo "  python3 privvy.py src/main.pv"
echo ""
echo -e "${BLUE}Commands:${NC}"
echo "  privvy help            # Show all commands"
echo "  privvy version         # Show version"
echo "  privvy-db init         # Initialize database"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo "  $SHARE_DIR/examples/"
echo ""
echo -e "${GREEN}Happy coding! 🚀${NC}"

