#!/bin/bash
# Privvy Installation Script
# Usage: ./install.sh (from the privvy directory after git clone)

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

# Check if we're in the privvy directory
if [ ! -f "privvy.py" ] || [ ! -f "interpreter.py" ]; then
    echo -e "${RED}❌ Error: privvy.py not found${NC}"
    echo ""
    echo "Please run this script from the privvy directory:"
    echo ""
    echo -e "${BLUE}  git clone https://github.com/Victra-Studio/privvy.git${NC}"
    echo -e "${BLUE}  cd privvy${NC}"
    echo -e "${BLUE}  ./install.sh${NC}"
    echo ""
    exit 1
fi

# Check for required tools
echo -e "${BLUE}Checking requirements...${NC}"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is required but not installed.${NC}"
    echo "Install Python from https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✅ Python $PYTHON_VERSION found${NC}"

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

# Install Privvy files
echo -e "${BLUE}Installing Privvy core files...${NC}"
$SUDO cp privvy.py lexer.py parser.py interpreter.py ast_nodes.py token_types.py "$PRIVVY_DIR/"

echo -e "${BLUE}Installing CLI tools...${NC}"
$SUDO cp privvy-cli.py privvy-db.py "$PRIVVY_DIR/"

# Install examples and templates
if [ -d "examples" ]; then
    echo -e "${BLUE}Installing examples...${NC}"
    $SUDO cp -r examples "$SHARE_DIR/"
fi

if [ -d "vscode-privvy" ]; then
    echo -e "${BLUE}Installing VSCode extension...${NC}"
    $SUDO cp -r vscode-privvy "$SHARE_DIR/"
fi

if [ -d "project-template" ]; then
    echo -e "${BLUE}Installing project templates...${NC}"
    $SUDO cp -r project-template "$SHARE_DIR/"
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

# Test installation
echo -e "${BLUE}Testing installation...${NC}"
if command -v privvy &> /dev/null; then
    echo -e "${GREEN}✅ privvy command is available${NC}"
else
    echo -e "${YELLOW}⚠️  privvy command not found in PATH${NC}"
fi

# Installation complete
echo ""
echo -e "${GREEN}╔════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   ✨ Privvy installed successfully!   ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}Quick Start:${NC}"
echo "  privvy create-project my-api"
echo "  cd my-api"
echo "  privvy run migrate.pv"
echo "  privvy run src/main.pv"
echo ""
echo -e "${BLUE}Commands:${NC}"
echo "  privvy help            # Show all commands"
echo "  privvy version         # Show version"
echo "  privvy create-project  # Create new project"
echo "  privvy-db init         # Initialize database"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo "  cat $SHARE_DIR/../doc/privvy/QUICK_START.md"
echo ""
echo -e "${GREEN}Happy coding! 🚀${NC}"
