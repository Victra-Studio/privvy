"""
Parser for the Privvy programming language.
Converts tokens into an Abstract Syntax Tree (AST).
"""

from typing import List, Optional
from token_types import Token, TokenType
from ast_nodes import *


class Parser:
    """Parses tokens into an Abstract Syntax Tree."""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def error(self, message: str):
        current = self.current()
        raise SyntaxError(f"Parser error at {current.line}:{current.column}: {message}")
    
    def current(self) -> Token:
        """Get current token without consuming it."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]  # EOF
    
    def peek(self, offset: int = 1) -> Token:
        """Look ahead at token."""
        pos = self.pos + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return self.tokens[-1]  # EOF
    
    def advance(self) -> Token:
        """Consume and return current token."""
        token = self.current()
        if token.type != TokenType.EOF:
            self.pos += 1
        return token
    
    def match(self, *types: TokenType) -> bool:
        """Check if current token matches any of the given types."""
        return self.current().type in types
    
    def consume(self, token_type: TokenType, message: str) -> Token:
        """Consume token of expected type or raise error."""
        if self.current().type == token_type:
            return self.advance()
        self.error(message)
    
    def skip_newlines(self):
        """Skip any newline tokens."""
        while self.match(TokenType.NEWLINE):
            self.advance()
    
    def parse(self) -> Program:
        """Parse tokens into a Program AST node."""
        statements = []
        
        while not self.match(TokenType.EOF):
            self.skip_newlines()
            if not self.match(TokenType.EOF):
                statements.append(self.parse_statement())
            self.skip_newlines()
        
        return Program(statements)
    
    def parse_statement(self) -> ASTNode:
        """Parse a single statement."""
        self.skip_newlines()
        
        # Variable declaration
        if self.match(TokenType.LET):
            return self.parse_var_declaration()
        
        # Function declaration
        if self.match(TokenType.FUN):
            return self.parse_function_declaration()
        
        # Class declaration
        if self.match(TokenType.CLASS):
            return self.parse_class_declaration()
        
        # If statement
        if self.match(TokenType.IF):
            return self.parse_if_statement()
        
        # While loop
        if self.match(TokenType.WHILE):
            return self.parse_while_statement()
        
        # For loop
        if self.match(TokenType.FOR):
            return self.parse_for_statement()
        
        # Return statement
        if self.match(TokenType.RETURN):
            return self.parse_return_statement()
        
        # Expression statement
        return self.parse_expression_statement()
    
    def parse_var_declaration(self) -> VarDeclaration:
        """Parse variable declaration: let name = value"""
        self.consume(TokenType.LET, "Expected 'let'")
        
        name_token = self.consume(TokenType.IDENTIFIER, "Expected variable name")
        name = name_token.value
        
        initializer = None
        if self.match(TokenType.ASSIGN):
            self.advance()
            initializer = self.parse_expression()
        
        return VarDeclaration(name, initializer)
    
    def parse_function_declaration(self) -> FunctionDeclaration:
        """Parse function declaration: fun name(params) { body }"""
        self.consume(TokenType.FUN, "Expected 'fun'")
        
        name_token = self.consume(TokenType.IDENTIFIER, "Expected function name")
        name = name_token.value
        
        self.consume(TokenType.LEFT_PAREN, "Expected '(' after function name")
        
        parameters = []
        if not self.match(TokenType.RIGHT_PAREN):
            param_token = self.consume(TokenType.IDENTIFIER, "Expected parameter name")
            parameters.append(param_token.value)
            
            while self.match(TokenType.COMMA):
                self.advance()
                param_token = self.consume(TokenType.IDENTIFIER, "Expected parameter name")
                parameters.append(param_token.value)
        
        self.consume(TokenType.RIGHT_PAREN, "Expected ')' after parameters")
        
        self.skip_newlines()
        self.consume(TokenType.LEFT_BRACE, "Expected '{' before function body")
        
        body = self.parse_block()
        
        return FunctionDeclaration(name, parameters, body)
    
    def parse_class_declaration(self) -> ClassDeclaration:
        """Parse class declaration: class Name { ... }"""
        self.consume(TokenType.CLASS, "Expected 'class'")
        
        name_token = self.consume(TokenType.IDENTIFIER, "Expected class name")
        name = name_token.value
        
        superclass = None
        if self.match(TokenType.EXTENDS):
            self.advance()
            superclass_token = self.consume(TokenType.IDENTIFIER, "Expected superclass name")
            superclass = superclass_token.value
        
        self.skip_newlines()
        self.consume(TokenType.LEFT_BRACE, "Expected '{' before class body")
        self.skip_newlines()
        
        constructor = None
        methods = []
        
        while not self.match(TokenType.RIGHT_BRACE) and not self.match(TokenType.EOF):
            self.skip_newlines()
            
            if self.match(TokenType.CONSTRUCTOR):
                self.advance()
                self.consume(TokenType.LEFT_PAREN, "Expected '(' after constructor")
                
                parameters = []
                if not self.match(TokenType.RIGHT_PAREN):
                    param_token = self.consume(TokenType.IDENTIFIER, "Expected parameter name")
                    parameters.append(param_token.value)
                    
                    while self.match(TokenType.COMMA):
                        self.advance()
                        param_token = self.consume(TokenType.IDENTIFIER, "Expected parameter name")
                        parameters.append(param_token.value)
                
                self.consume(TokenType.RIGHT_PAREN, "Expected ')' after parameters")
                self.skip_newlines()
                self.consume(TokenType.LEFT_BRACE, "Expected '{' before constructor body")
                
                body = self.parse_block()
                constructor = FunctionDeclaration("constructor", parameters, body)
            
            elif self.match(TokenType.FUN):
                methods.append(self.parse_function_declaration())
            
            self.skip_newlines()
        
        self.consume(TokenType.RIGHT_BRACE, "Expected '}' after class body")
        
        return ClassDeclaration(name, superclass, constructor, methods)
    
    def parse_if_statement(self) -> IfStatement:
        """Parse if statement: if (condition) { ... } else { ... }"""
        self.consume(TokenType.IF, "Expected 'if'")
        self.consume(TokenType.LEFT_PAREN, "Expected '(' after 'if'")
        
        condition = self.parse_expression()
        
        self.consume(TokenType.RIGHT_PAREN, "Expected ')' after condition")
        self.skip_newlines()
        self.consume(TokenType.LEFT_BRACE, "Expected '{' before if body")
        
        then_branch = self.parse_block()
        
        else_branch = None
        if self.match(TokenType.ELSE):
            self.advance()
            self.skip_newlines()
            self.consume(TokenType.LEFT_BRACE, "Expected '{' before else body")
            else_branch = self.parse_block()
        
        return IfStatement(condition, then_branch, else_branch)
    
    def parse_while_statement(self) -> WhileStatement:
        """Parse while loop: while (condition) { ... }"""
        self.consume(TokenType.WHILE, "Expected 'while'")
        self.consume(TokenType.LEFT_PAREN, "Expected '(' after 'while'")
        
        condition = self.parse_expression()
        
        self.consume(TokenType.RIGHT_PAREN, "Expected ')' after condition")
        self.skip_newlines()
        self.consume(TokenType.LEFT_BRACE, "Expected '{' before while body")
        
        body = self.parse_block()
        
        return WhileStatement(condition, body)
    
    def parse_for_statement(self) -> ForStatement:
        """Parse for loop: for (init; condition; increment) { ... }"""
        self.consume(TokenType.FOR, "Expected 'for'")
        self.consume(TokenType.LEFT_PAREN, "Expected '(' after 'for'")
        
        # Initializer
        initializer = None
        if not self.match(TokenType.SEMICOLON):
            if self.match(TokenType.LET):
                initializer = self.parse_var_declaration()
            else:
                initializer = self.parse_expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after for initializer")
        
        # Condition
        condition = None
        if not self.match(TokenType.SEMICOLON):
            condition = self.parse_expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after for condition")
        
        # Increment
        increment = None
        if not self.match(TokenType.RIGHT_PAREN):
            increment = self.parse_expression()
        
        self.consume(TokenType.RIGHT_PAREN, "Expected ')' after for clauses")
        self.skip_newlines()
        self.consume(TokenType.LEFT_BRACE, "Expected '{' before for body")
        
        body = self.parse_block()
        
        return ForStatement(initializer, condition, increment, body)
    
    def parse_return_statement(self) -> ReturnStatement:
        """Parse return statement: return value"""
        self.consume(TokenType.RETURN, "Expected 'return'")
        
        value = None
        if not self.match(TokenType.NEWLINE, TokenType.RIGHT_BRACE, TokenType.EOF):
            value = self.parse_expression()
        
        return ReturnStatement(value)
    
    def parse_block(self) -> List[ASTNode]:
        """Parse a block of statements between { }."""
        statements = []
        self.skip_newlines()
        
        while not self.match(TokenType.RIGHT_BRACE) and not self.match(TokenType.EOF):
            statements.append(self.parse_statement())
            self.skip_newlines()
        
        self.consume(TokenType.RIGHT_BRACE, "Expected '}' after block")
        
        return statements
    
    def parse_expression_statement(self) -> ASTNode:
        """Parse an expression as a statement."""
        return self.parse_expression()
    
    def parse_expression(self) -> ASTNode:
        """Parse an expression."""
        return self.parse_assignment()
    
    def parse_assignment(self) -> ASTNode:
        """Parse assignment expression."""
        expr = self.parse_or()
        
        if self.match(TokenType.ASSIGN):
            self.advance()
            value = self.parse_assignment()
            return Assignment(expr, value)
        
        return expr
    
    def parse_or(self) -> ASTNode:
        """Parse logical OR expression."""
        left = self.parse_and()
        
        while self.match(TokenType.OR):
            op = self.advance().value
            right = self.parse_and()
            left = BinaryOp(left, 'or', right)
        
        return left
    
    def parse_and(self) -> ASTNode:
        """Parse logical AND expression."""
        left = self.parse_equality()
        
        while self.match(TokenType.AND):
            op = self.advance().value
            right = self.parse_equality()
            left = BinaryOp(left, 'and', right)
        
        return left
    
    def parse_equality(self) -> ASTNode:
        """Parse equality operators: == !="""
        left = self.parse_comparison()
        
        while self.match(TokenType.EQUAL, TokenType.NOT_EQUAL):
            op = self.advance().value
            right = self.parse_comparison()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_comparison(self) -> ASTNode:
        """Parse comparison operators: < <= > >="""
        left = self.parse_addition()
        
        while self.match(TokenType.LESS_THAN, TokenType.LESS_EQUAL, 
                         TokenType.GREATER_THAN, TokenType.GREATER_EQUAL):
            op = self.advance().value
            right = self.parse_addition()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_addition(self) -> ASTNode:
        """Parse addition and subtraction: + -"""
        left = self.parse_multiplication()
        
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = self.advance().value
            right = self.parse_multiplication()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_multiplication(self) -> ASTNode:
        """Parse multiplication, division, modulo: * / %"""
        left = self.parse_unary()
        
        while self.match(TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            op = self.advance().value
            right = self.parse_unary()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_unary(self) -> ASTNode:
        """Parse unary operators: - !"""
        if self.match(TokenType.MINUS, TokenType.NOT):
            op = self.advance().value
            operand = self.parse_unary()
            return UnaryOp(op, operand)
        
        return self.parse_call()
    
    def parse_call(self) -> ASTNode:
        """Parse function calls and member access."""
        expr = self.parse_primary()
        
        while True:
            if self.match(TokenType.LEFT_PAREN):
                self.advance()
                arguments = []
                
                if not self.match(TokenType.RIGHT_PAREN):
                    arguments.append(self.parse_expression())
                    
                    while self.match(TokenType.COMMA):
                        self.advance()
                        arguments.append(self.parse_expression())
                
                self.consume(TokenType.RIGHT_PAREN, "Expected ')' after arguments")
                expr = FunctionCall(expr, arguments)
            
            elif self.match(TokenType.DOT):
                self.advance()
                property_token = self.consume(TokenType.IDENTIFIER, "Expected property name after '.'")
                expr = MemberAccess(expr, property_token.value)
            
            elif self.match(TokenType.LEFT_BRACKET):
                self.advance()
                index = self.parse_expression()
                self.consume(TokenType.RIGHT_BRACKET, "Expected ']' after array index")
                expr = ArrayAccess(expr, index)
            
            else:
                break
        
        return expr
    
    def parse_primary(self) -> ASTNode:
        """Parse primary expressions (literals, identifiers, etc.)."""
        # Numbers
        if self.match(TokenType.NUMBER):
            return NumberLiteral(self.advance().value)
        
        # Strings
        if self.match(TokenType.STRING):
            return StringLiteral(self.advance().value)
        
        # Booleans
        if self.match(TokenType.TRUE, TokenType.FALSE):
            return BooleanLiteral(self.advance().value)
        
        # Null
        if self.match(TokenType.NULL):
            self.advance()
            return NullLiteral()
        
        # This
        if self.match(TokenType.THIS):
            self.advance()
            return ThisExpression()
        
        # New expression
        if self.match(TokenType.NEW):
            self.advance()
            class_name_token = self.consume(TokenType.IDENTIFIER, "Expected class name after 'new'")
            class_name = class_name_token.value
            
            self.consume(TokenType.LEFT_PAREN, "Expected '(' after class name")
            arguments = []
            
            if not self.match(TokenType.RIGHT_PAREN):
                arguments.append(self.parse_expression())
                
                while self.match(TokenType.COMMA):
                    self.advance()
                    arguments.append(self.parse_expression())
            
            self.consume(TokenType.RIGHT_PAREN, "Expected ')' after arguments")
            return NewExpression(class_name, arguments)
        
        # Identifiers
        if self.match(TokenType.IDENTIFIER):
            return Identifier(self.advance().value)
        
        # Grouped expressions
        if self.match(TokenType.LEFT_PAREN):
            self.advance()
            expr = self.parse_expression()
            self.consume(TokenType.RIGHT_PAREN, "Expected ')' after expression")
            return expr
        
        # Array literals
        if self.match(TokenType.LEFT_BRACKET):
            self.advance()
            elements = []
            
            if not self.match(TokenType.RIGHT_BRACKET):
                elements.append(self.parse_expression())
                
                while self.match(TokenType.COMMA):
                    self.advance()
                    elements.append(self.parse_expression())
            
            self.consume(TokenType.RIGHT_BRACKET, "Expected ']' after array elements")
            return ArrayLiteral(elements)
        
        self.error(f"Unexpected token: {self.current()}")

