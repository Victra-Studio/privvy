# Homebrew Formula for Privvy
# Install with: brew install privvy

class Privvy < Formula
  desc "The Easiest Backend Programming Language with Built-in ORM"
  homepage "https://github.com/yourname/privvy"
  url "https://github.com/yourname/privvy/archive/v1.0.0.tar.gz"
  sha256 "YOUR_SHA256_HERE"  # Generate with: shasum -a 256 privvy-1.0.0.tar.gz
  license "MIT"
  version "1.0.0"

  # Dependencies
  depends_on "python@3.11"

  def install
    # Install Python files to libexec
    libexec.install "privvy.py", "lexer.py", "parser.py", "interpreter.py", "ast_nodes.py", "token_types.py"
    
    # Install CLI scripts
    libexec.install "privvy-cli.py", "privvy-db.py"
    
    # Install documentation
    doc.install "README.md", "QUICK_START.md", "ORM_GUIDE.md", "DATABASE_GUIDE.md", "CLI_GUIDE.md"
    
    # Install examples
    (share/"privvy/examples").install Dir["examples/*"]
    (share/"privvy/vscode-privvy").install Dir["vscode-privvy/*"]
    (share/"privvy/project-template").install Dir["project-template/*"]
    
    # Create wrapper scripts
    (bin/"privvy").write_env_script(libexec/"privvy-cli.py", Language::Python.prepend_path_for_pip_install("python@3.11"))
    (bin/"privvy-db").write_env_script(libexec/"privvy-db.py", Language::Python.prepend_path_for_pip_install("python@3.11"))
  end

  def caveats
    <<~EOS
      🎉 Privvy has been installed!

      Quick Start:
        privvy create-project my-api
        cd my-api
        python3 privvy.py migrate.pv
        python3 privvy.py src/main.pv

      Commands:
        privvy create-project <name>  # Create new project
        privvy run <file>              # Run a file
        privvy migrate                 # Run migrations
        privvy-db init                 # Initialize database

      Documentation:
        #{doc}

      Examples:
        #{share}/privvy/examples/

      Learn more:
        privvy help
        cat #{doc}/QUICK_START.md
    EOS
  end

  test do
    system "#{bin}/privvy", "version"
    system "#{bin}/privvy", "help"
  end
end

