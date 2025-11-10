#!/usr/bin/env python3
"""
Privvy Programming Language
Main entry point for running Privvy programs.
"""

import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def run_file(filepath: str):
    """Run a Privvy source file."""
    try:
        with open(filepath, 'r') as f:
            source = f.read()
        
        run(source)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def run(source: str):
    """Run Privvy source code."""
    try:
        # Tokenize
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Parse
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Interpret
        interpreter = Interpreter()
        interpreter.interpret(ast)
        
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Runtime Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def run_repl():
    """Run the interactive REPL (Read-Eval-Print Loop)."""
    print("Privvy Programming Language v0.1.0")
    print("Type 'exit' or 'quit' to exit")
    print()
    
    interpreter = Interpreter()
    
    while True:
        try:
            line = input(">>> ")
            
            if line.strip() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            if not line.strip():
                continue
            
            # Tokenize
            lexer = Lexer(line)
            tokens = lexer.tokenize()
            
            # Parse
            parser = Parser(tokens)
            ast = parser.parse()
            
            # Interpret
            for statement in ast.statements:
                result = interpreter.execute(statement)
                # Print non-None expression results
                if result is not None and not line.strip().startswith(('let', 'fun', 'class', 'if', 'while', 'for')):
                    print(result)
        
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            break
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        # Run file
        run_file(sys.argv[1])
    else:
        # Run REPL
        run_repl()


if __name__ == "__main__":
    main()

