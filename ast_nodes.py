"""
Abstract Syntax Tree node definitions for Privvy.
"""

from dataclasses import dataclass
from typing import Any, List, Optional, Union


# Base node
@dataclass
class ASTNode:
    """Base class for all AST nodes."""
    pass


# Literals
@dataclass
class NumberLiteral(ASTNode):
    value: Union[float, int]


@dataclass
class StringLiteral(ASTNode):
    value: str


@dataclass
class BooleanLiteral(ASTNode):
    value: bool


@dataclass
class NullLiteral(ASTNode):
    pass


# Identifiers
@dataclass
class Identifier(ASTNode):
    name: str


# Binary operations
@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode


# Unary operations
@dataclass
class UnaryOp(ASTNode):
    operator: str
    operand: ASTNode


# Variable declaration
@dataclass
class VarDeclaration(ASTNode):
    name: str
    initializer: Optional[ASTNode] = None


# Assignment
@dataclass
class Assignment(ASTNode):
    target: ASTNode  # Can be Identifier or MemberAccess
    value: ASTNode


# Function call
@dataclass
class FunctionCall(ASTNode):
    callee: ASTNode
    arguments: List[ASTNode]


# Member access (e.g., obj.property)
@dataclass
class MemberAccess(ASTNode):
    object: ASTNode
    property: str


# Array literal
@dataclass
class ArrayLiteral(ASTNode):
    elements: List[ASTNode]


# Array access (e.g., arr[0])
@dataclass
class ArrayAccess(ASTNode):
    array: ASTNode
    index: ASTNode


# Function declaration
@dataclass
class FunctionDeclaration(ASTNode):
    name: str
    parameters: List[str]
    body: List[ASTNode]


# Class declaration
@dataclass
class ClassDeclaration(ASTNode):
    name: str
    superclass: Optional[str]
    constructor: Optional['FunctionDeclaration']
    methods: List[FunctionDeclaration]


# If statement
@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    then_branch: List[ASTNode]
    else_branch: Optional[List[ASTNode]] = None


# While loop
@dataclass
class WhileStatement(ASTNode):
    condition: ASTNode
    body: List[ASTNode]


# For loop
@dataclass
class ForStatement(ASTNode):
    initializer: Optional[ASTNode]
    condition: Optional[ASTNode]
    increment: Optional[ASTNode]
    body: List[ASTNode]


# Return statement
@dataclass
class ReturnStatement(ASTNode):
    value: Optional[ASTNode] = None


# This expression
@dataclass
class ThisExpression(ASTNode):
    pass


# New expression (object instantiation)
@dataclass
class NewExpression(ASTNode):
    class_name: str
    arguments: List[ASTNode]


# Program (root node)
@dataclass
class Program(ASTNode):
    statements: List[ASTNode]

