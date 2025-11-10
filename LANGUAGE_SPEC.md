# Privvy Language Specification

## Overview

Privvy is a beginner-friendly, web-oriented programming language with clean syntax and object-oriented features. It's designed to be easy to learn while providing powerful features for modern web development.

## Design Philosophy

1. **Easy to Learn**: Simple, intuitive syntax that's approachable for beginners
2. **Clean Code**: Readable and straightforward with minimal boilerplate
3. **Web-Oriented**: Built with web development in mind
4. **Object-Oriented**: Full support for classes, inheritance, and encapsulation

## Basic Syntax

### Comments

```
// Single-line comment
```

### Variables

Variables are declared using the `let` keyword:

```
let name = "Alice"
let age = 25
let isActive = true
let price = 19.99
```

Variables can be reassigned:

```
age = 26
```

### Data Types

#### Primitive Types

- **Number**: Integer or floating-point numbers
  - `42`, `3.14`, `-10`, `0.5`
  
- **String**: Text enclosed in single or double quotes
  - `"hello"`, `'world'`
  - Escape sequences: `\n`, `\t`, `\\`, `\"`, `\'`
  
- **Boolean**: Logical values
  - `true`, `false`
  
- **Null**: Represents no value
  - `null`

#### Composite Types

- **Array**: Ordered collection of values
  - `[1, 2, 3, 4, 5]`
  - `["apple", "banana", "orange"]`
  - Nested arrays: `[[1, 2], [3, 4]]`

### Operators

#### Arithmetic Operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulo

#### Comparison Operators

- `==` Equal to
- `!=` Not equal to
- `<` Less than
- `<=` Less than or equal to
- `>` Greater than
- `>=` Greater than or equal to

#### Logical Operators

- `and` Logical AND
- `or` Logical OR
- `not` or `!` Logical NOT

#### Assignment Operator

- `=` Assignment

### Control Flow

#### If Statement

```
if (condition) {
    // code
} else {
    // code
}
```

#### While Loop

```
while (condition) {
    // code
}
```

#### For Loop

```
for (let i = 0; i < 10; i = i + 1) {
    // code
}
```

### Functions

Functions are declared using the `fun` keyword:

```
fun functionName(param1, param2) {
    // code
    return value
}
```

Functions are first-class values and can be:
- Assigned to variables
- Passed as arguments
- Returned from other functions

Example:

```
fun greet(name) {
    print("Hello, " + name)
}

fun add(a, b) {
    return a + b
}
```

### Classes

Classes provide object-oriented programming capabilities:

```
class ClassName {
    constructor(param1, param2) {
        this.property1 = param1
        this.property2 = param2
    }
    
    fun methodName() {
        // code
    }
}
```

#### Creating Instances

```
let obj = new ClassName(arg1, arg2)
```

#### Accessing Properties and Methods

```
obj.property1
obj.methodName()
```

#### The `this` Keyword

Inside class methods, `this` refers to the current instance:

```
class Person {
    constructor(name) {
        this.name = name
    }
    
    fun greet() {
        print("Hi, I'm " + this.name)
    }
}
```

#### Inheritance

Classes can extend other classes:

```
class Animal {
    constructor(name) {
        this.name = name
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        // Note: super() not yet implemented in this version
        this.name = name
        this.breed = breed
    }
}
```

### Arrays

Arrays are zero-indexed collections:

```
let arr = [1, 2, 3, 4, 5]

// Access elements
let first = arr[0]  // 1

// Modify elements
arr[0] = 10

// Get length
let length = len(arr)
```

### Built-in Functions

#### `print(...args)`
Prints values to the console:

```
print("Hello")
print("Value:", 42)
```

#### `len(collection)`
Returns the length of a collection:

```
len([1, 2, 3])  // 3
len("hello")    // 5
```

#### `str(value)`
Converts a value to a string:

```
str(42)    // "42"
str(true)  // "True"
```

#### `int(value)`
Converts a value to an integer:

```
int("42")   // 42
int(3.14)   // 3
```

#### `float(value)`
Converts a value to a floating-point number:

```
float("3.14")  // 3.14
float(42)      // 42.0
```

## Program Structure

A Privvy program consists of a sequence of statements. Each statement can be:

- Variable declaration
- Function declaration
- Class declaration
- Expression statement
- Control flow statement (if, while, for)
- Return statement

## Scoping Rules

Privvy uses lexical scoping:

1. Variables are scoped to the block they're declared in
2. Inner scopes can access outer scope variables
3. Functions capture their enclosing scope (closures)
4. Class methods have access to instance properties via `this`

## Type System

Privvy is dynamically typed:

- Variables don't have declared types
- Types are determined at runtime
- Type errors are caught during execution

## Error Handling

Errors are reported with:
- Error type (SyntaxError, RuntimeError, etc.)
- Line and column numbers (when available)
- Descriptive error message

## Future Enhancements

Potential features for future versions:

1. **String interpolation**: `"Hello, ${name}"`
2. **Arrow functions**: `(x, y) -> x + y`
3. **Object literals**: `{ name: "Alice", age: 25 }`
4. **Destructuring**: `let [a, b] = [1, 2]`
5. **Spread operator**: `...array`
6. **Module system**: `import`, `export`
7. **Async/await**: For asynchronous operations
8. **Pattern matching**: `match` expressions
9. **Type hints**: Optional static typing
10. **Standard library**: String, Math, Array utilities
11. **Web API bindings**: DOM manipulation, fetch, etc.
12. **Error handling**: `try`, `catch`, `throw`

## Grammar Reference

```
program         → statement* EOF

statement       → varDecl
                | funDecl
                | classDecl
                | ifStmt
                | whileStmt
                | forStmt
                | returnStmt
                | exprStmt

varDecl         → "let" IDENTIFIER ( "=" expression )? 
funDecl         → "fun" IDENTIFIER "(" parameters? ")" block
classDecl       → "class" IDENTIFIER ( "extends" IDENTIFIER )? "{" constructor? method* "}"
constructor     → "constructor" "(" parameters? ")" block
method          → "fun" IDENTIFIER "(" parameters? ")" block

ifStmt          → "if" "(" expression ")" block ( "else" block )?
whileStmt       → "while" "(" expression ")" block
forStmt         → "for" "(" ( varDecl | exprStmt )? ";" expression? ";" expression? ")" block
returnStmt      → "return" expression?

block           → "{" statement* "}"

expression      → assignment
assignment      → ( identifier | memberAccess | arrayAccess ) "=" assignment
                | logic_or
logic_or        → logic_and ( "or" logic_and )*
logic_and       → equality ( "and" equality )*
equality        → comparison ( ( "==" | "!=" ) comparison )*
comparison      → addition ( ( "<" | "<=" | ">" | ">=" ) addition )*
addition        → multiplication ( ( "+" | "-" ) multiplication )*
multiplication  → unary ( ( "*" | "/" | "%" ) unary )*
unary           → ( "-" | "!" | "not" ) unary | call
call            → primary ( "(" arguments? ")" | "." IDENTIFIER | "[" expression "]" )*
primary         → NUMBER | STRING | "true" | "false" | "null"
                | IDENTIFIER
                | "this"
                | "new" IDENTIFIER "(" arguments? ")"
                | "(" expression ")"
                | "[" arguments? "]"

parameters      → IDENTIFIER ( "," IDENTIFIER )*
arguments       → expression ( "," expression )*
```

## Keywords

Reserved keywords that cannot be used as identifiers:

- `let`
- `fun`
- `class`
- `constructor`
- `extends`
- `if`
- `else`
- `while`
- `for`
- `return`
- `this`
- `new`
- `true`
- `false`
- `null`
- `and`
- `or`
- `not`
- `import`
- `export`

## File Extension

Privvy source files use the `.pv` extension.

## Example Programs

See the `examples/` directory for sample programs demonstrating various language features.

