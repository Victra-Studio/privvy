# Privvy Quick Reference Card

Quick reference for Privvy syntax and features.

## Basic Syntax

### Variables
```privvy
let name = "value"
let age = 25
let active = true
let data = null
```

### Comments
```privvy
// Single-line comment
```

### Data Types
- **Number**: `42`, `3.14`
- **String**: `"hello"`, `'world'`
- **Boolean**: `true`, `false`
- **Null**: `null`
- **Array**: `[1, 2, 3]`

## Operators

### Arithmetic
```privvy
+   // Addition
-   // Subtraction
*   // Multiplication
/   // Division
%   // Modulo
```

### Comparison
```privvy
==  // Equal
!=  // Not equal
<   // Less than
<=  // Less or equal
>   // Greater than
>=  // Greater or equal
```

### Logical
```privvy
and  // Logical AND
or   // Logical OR
not  // Logical NOT
```

## Control Flow

### If/Else
```privvy
if (condition) {
    // code
} else {
    // code
}
```

### While Loop
```privvy
while (condition) {
    // code
}
```

### For Loop
```privvy
for (let i = 0; i < 10; i = i + 1) {
    // code
}
```

## Functions

### Declaration
```privvy
fun name(param1, param2) {
    return value
}
```

### Call
```privvy
let result = name(arg1, arg2)
```

## Classes

### Declaration
```privvy
class ClassName {
    constructor(param) {
        this.property = param
    }
    
    fun method() {
        return this.property
    }
}
```

### Instantiation
```privvy
let obj = new ClassName(value)
obj.method()
obj.property
```

### Inheritance
```privvy
class Child extends Parent {
    constructor(param) {
        this.property = param
    }
}
```

## Arrays

### Creation
```privvy
let arr = [1, 2, 3, 4, 5]
```

### Access
```privvy
let first = arr[0]
arr[1] = 10
```

### Length
```privvy
let size = len(arr)
```

## Built-in Functions

### print()
```privvy
print("Hello")
print("Value:", 42)
```

### len()
```privvy
len([1, 2, 3])    // 3
len("hello")      // 5
```

### Type Conversions
```privvy
str(42)           // "42"
int("100")        // 100
float("3.14")     // 3.14
```

## Common Patterns

### Iteration
```privvy
for (let i = 0; i < len(array); i = i + 1) {
    print(array[i])
}
```

### Recursion
```privvy
fun factorial(n) {
    if (n <= 1) {
        return 1
    }
    return n * factorial(n - 1)
}
```

### String Concatenation
```privvy
let full = first + " " + last
```

### Object Methods
```privvy
class Counter {
    constructor() {
        this.count = 0
    }
    
    fun increment() {
        this.count = this.count + 1
    }
}
```

## VS Code Snippets

Type these and press Tab:

- `let` → Variable declaration
- `fun` → Function
- `class` → Class with constructor
- `if` → If statement
- `for` → For loop
- `while` → While loop

## Running Code

### Command Line
```bash
# Run file
python3 privvy.py file.pv

# Start REPL
python3 privvy.py
```

### VS Code
- Press `Cmd+Shift+B` to run current file
- Or use the integrated terminal

## File Extension

All Privvy files use the `.pv` extension.

## Keywords (Reserved)

```
let       fun       class      constructor
if        else      while      for
return    this      new        extends
true      false     null
and       or        not
import    export
```

## Escape Sequences

In strings:
- `\n` - Newline
- `\t` - Tab
- `\r` - Carriage return
- `\\` - Backslash
- `\"` - Double quote
- `\'` - Single quote

## Examples

### Hello World
```privvy
print("Hello, World!")
```

### Function with Return
```privvy
fun add(a, b) {
    return a + b
}
```

### Class Example
```privvy
class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
    
    fun greet() {
        print("Hi, I'm " + this.name)
    }
}

let alice = new Person("Alice", 25)
alice.greet()
```

### Loop Example
```privvy
let sum = 0
for (let i = 1; i <= 10; i = i + 1) {
    sum = sum + i
}
print("Sum:", sum)
```

---

For more details, see:
- [LANGUAGE_SPEC.md](LANGUAGE_SPEC.md) - Complete specification
- [GETTING_STARTED.md](GETTING_STARTED.md) - Tutorial
- [examples/](examples/) - Code examples

