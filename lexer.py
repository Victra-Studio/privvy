"""
Lexer/Tokenizer for the Privvy programming language.
Converts source code into a stream of tokens.
"""

from token_types import Token, TokenType


class Lexer:
    """Tokenizes Privvy source code."""
    
    KEYWORDS = {
        'let': TokenType.LET,
        'fun': TokenType.FUN,
        'class': TokenType.CLASS,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'while': TokenType.WHILE,
        'for': TokenType.FOR,
        'return': TokenType.RETURN,
        'this': TokenType.THIS,
        'constructor': TokenType.CONSTRUCTOR,
        'new': TokenType.NEW,
        'extends': TokenType.EXTENDS,
        'true': TokenType.TRUE,
        'false': TokenType.FALSE,
        'null': TokenType.NULL,
        'and': TokenType.AND,
        'or': TokenType.OR,
        'not': TokenType.NOT,
        'import': TokenType.IMPORT,
        'export': TokenType.EXPORT,
    }
    
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []
    
    def error(self, message: str):
        raise SyntaxError(f"Lexer error at {self.line}:{self.column}: {message}")
    
    def peek(self, offset: int = 0) -> str:
        """Look ahead at character without consuming it."""
        pos = self.pos + offset
        if pos < len(self.source):
            return self.source[pos]
        return '\0'
    
    def advance(self) -> str:
        """Consume and return current character."""
        if self.pos >= len(self.source):
            return '\0'
        
        char = self.source[self.pos]
        self.pos += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        
        return char
    
    def skip_whitespace(self):
        """Skip whitespace except newlines (they can be significant)."""
        while self.peek() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        """Skip single-line comments starting with //"""
        if self.peek() == '/' and self.peek(1) == '/':
            while self.peek() not in '\n\0':
                self.advance()
    
    def read_number(self) -> Token:
        """Read a number literal."""
        start_line = self.line
        start_column = self.column
        num_str = ''
        
        while self.peek().isdigit() or self.peek() == '.':
            num_str += self.advance()
        
        # Convert to appropriate type
        if '.' in num_str:
            value = float(num_str)
        else:
            value = int(num_str)
        
        return Token(TokenType.NUMBER, value, start_line, start_column)
    
    def read_string(self) -> Token:
        """Read a string literal."""
        start_line = self.line
        start_column = self.column
        quote_char = self.advance()  # Consume opening quote
        string_value = ''
        
        while self.peek() != quote_char and self.peek() != '\0':
            if self.peek() == '\\':
                self.advance()  # Consume backslash
                next_char = self.advance()
                # Handle escape sequences
                escape_map = {
                    'n': '\n',
                    't': '\t',
                    'r': '\r',
                    '\\': '\\',
                    '"': '"',
                    "'": "'"
                }
                string_value += escape_map.get(next_char, next_char)
            else:
                string_value += self.advance()
        
        if self.peek() == '\0':
            self.error("Unterminated string")
        
        self.advance()  # Consume closing quote
        return Token(TokenType.STRING, string_value, start_line, start_column)
    
    def read_identifier(self) -> Token:
        """Read an identifier or keyword."""
        start_line = self.line
        start_column = self.column
        identifier = ''
        
        while self.peek().isalnum() or self.peek() == '_':
            identifier += self.advance()
        
        # Check if it's a keyword
        token_type = self.KEYWORDS.get(identifier, TokenType.IDENTIFIER)
        
        # For boolean and null keywords, set appropriate values
        if token_type == TokenType.TRUE:
            value = True
        elif token_type == TokenType.FALSE:
            value = False
        elif token_type == TokenType.NULL:
            value = None
        else:
            value = identifier
        
        return Token(token_type, value, start_line, start_column)
    
    def tokenize(self) -> list[Token]:
        """Tokenize the entire source code."""
        while self.pos < len(self.source):
            self.skip_whitespace()
            self.skip_comment()
            
            if self.pos >= len(self.source):
                break
            
            char = self.peek()
            start_line = self.line
            start_column = self.column
            
            # Numbers
            if char.isdigit():
                self.tokens.append(self.read_number())
            
            # Strings
            elif char in '"\'':
                self.tokens.append(self.read_string())
            
            # Identifiers and keywords
            elif char.isalpha() or char == '_':
                self.tokens.append(self.read_identifier())
            
            # Operators and punctuation
            elif char == '+':
                self.advance()
                self.tokens.append(Token(TokenType.PLUS, '+', start_line, start_column))
            
            elif char == '-':
                self.advance()
                if self.peek() == '>':
                    self.advance()
                    self.tokens.append(Token(TokenType.ARROW, '->', start_line, start_column))
                else:
                    self.tokens.append(Token(TokenType.MINUS, '-', start_line, start_column))
            
            elif char == '*':
                self.advance()
                self.tokens.append(Token(TokenType.MULTIPLY, '*', start_line, start_column))
            
            elif char == '/':
                self.advance()
                self.tokens.append(Token(TokenType.DIVIDE, '/', start_line, start_column))
            
            elif char == '%':
                self.advance()
                self.tokens.append(Token(TokenType.MODULO, '%', start_line, start_column))
            
            elif char == '=':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.EQUAL, '==', start_line, start_column))
                else:
                    self.tokens.append(Token(TokenType.ASSIGN, '=', start_line, start_column))
            
            elif char == '!':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.NOT_EQUAL, '!=', start_line, start_column))
                else:
                    self.tokens.append(Token(TokenType.NOT, '!', start_line, start_column))
            
            elif char == '<':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.LESS_EQUAL, '<=', start_line, start_column))
                else:
                    self.tokens.append(Token(TokenType.LESS_THAN, '<', start_line, start_column))
            
            elif char == '>':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    self.tokens.append(Token(TokenType.GREATER_EQUAL, '>=', start_line, start_column))
                else:
                    self.tokens.append(Token(TokenType.GREATER_THAN, '>', start_line, start_column))
            
            elif char == '(':
                self.advance()
                self.tokens.append(Token(TokenType.LEFT_PAREN, '(', start_line, start_column))
            
            elif char == ')':
                self.advance()
                self.tokens.append(Token(TokenType.RIGHT_PAREN, ')', start_line, start_column))
            
            elif char == '{':
                self.advance()
                self.tokens.append(Token(TokenType.LEFT_BRACE, '{', start_line, start_column))
            
            elif char == '}':
                self.advance()
                self.tokens.append(Token(TokenType.RIGHT_BRACE, '}', start_line, start_column))
            
            elif char == '[':
                self.advance()
                self.tokens.append(Token(TokenType.LEFT_BRACKET, '[', start_line, start_column))
            
            elif char == ']':
                self.advance()
                self.tokens.append(Token(TokenType.RIGHT_BRACKET, ']', start_line, start_column))
            
            elif char == ',':
                self.advance()
                self.tokens.append(Token(TokenType.COMMA, ',', start_line, start_column))
            
            elif char == '.':
                self.advance()
                self.tokens.append(Token(TokenType.DOT, '.', start_line, start_column))
            
            elif char == ';':
                self.advance()
                self.tokens.append(Token(TokenType.SEMICOLON, ';', start_line, start_column))
            
            elif char == ':':
                self.advance()
                self.tokens.append(Token(TokenType.COLON, ':', start_line, start_column))
            
            elif char == '\n':
                self.advance()
                self.tokens.append(Token(TokenType.NEWLINE, '\n', start_line, start_column))
            
            else:
                self.error(f"Unexpected character: {char}")
        
        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens

