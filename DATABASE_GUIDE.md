# Privvy Database Guide - The Easiest Backend for Beginners! 🚀

Privvy makes database programming **incredibly simple**. Connect and query in just 1-2 lines!

## Why Privvy for Databases?

✅ **Super Simple** - Connect in 1 line, query in 1 line  
✅ **Beginner Friendly** - No complex setup or configuration  
✅ **SQLite Built-in** - Start coding immediately, no installation  
✅ **PostgreSQL Ready** - Scale to production when you're ready  
✅ **Clean Syntax** - Easy to read and understand  

---

## Quick Start (30 Seconds!)

### SQLite (Zero Setup!)

```privvy
// That's it! You're coding with a database!
let db = Database("myapp.db")
let users = db.query("SELECT * FROM users")
```

SQLite is perfect for:
- Learning databases
- Small applications
- Quick prototypes
- Local development

---

## Installation

### For SQLite (Built-in!)
**Nothing to install!** SQLite comes with Python. Just start coding!

### For PostgreSQL (Production)

```bash
# Install PostgreSQL support
pip install psycopg2-binary

# Or use the requirements file
pip install -r requirements.txt
```

---

## Database Basics - Learn in 5 Minutes

### 1. Connect to Database

**SQLite** (easiest):
```privvy
let db = Database("myapp.db")           // Creates file
let db = Database(":memory:")            // In-memory (for testing)
```

**PostgreSQL** (production):
```privvy
let db = Database("postgresql://username:password@localhost:5432/dbname")
```

### 2. Create Tables

```privvy
db.execute("CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    age INTEGER
)")
```

### 3. Insert Data

```privvy
// Simple insert
db.execute("INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com', 25)")

// Insert with parameters (safer!)
db.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", 
    "Bob", "bob@example.com", 30)
```

### 4. Query Data

```privvy
// Get all users
let users = db.query("SELECT * FROM users")

// Loop through results
for user in users {
    print(user["name"] + " - " + user["email"])
}

// Query with conditions
let adults = db.query("SELECT * FROM users WHERE age >= 18")
```

### 5. Update Data

```privvy
db.execute("UPDATE users SET age = 26 WHERE name = 'Alice'")
```

### 6. Delete Data

```privvy
db.execute("DELETE FROM users WHERE age < 18")
```

### 7. Close Connection

```privvy
db.close()
```

---

## Complete Examples

### Example 1: User Management (Beginner)

```privvy
// Connect
let db = Database("users.db")

// Setup
db.execute("CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT
)")

// Add users
db.execute("INSERT INTO users (username, email) VALUES (?, ?)", 
    "john", "john@example.com")
db.execute("INSERT INTO users (username, email) VALUES (?, ?)", 
    "jane", "jane@example.com")

// Get all users
let users = db.query("SELECT * FROM users")
print("All users:")
for user in users {
    print("  " + str(user["id"]) + ". " + user["username"] + " (" + user["email"] + ")")
}

// Find specific user
let john = db.query("SELECT * FROM users WHERE username = ?", "john")
print("Found: " + john[0]["email"])

db.close()
```

### Example 2: Blog Backend (Intermediate)

```privvy
// Setup database
let db = Database("blog.db")

// Create tables
db.execute("CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    author TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)")

db.execute("CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER,
    author TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id)
)")

// Create a post
db.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)",
    "My First Post", 
    "This is my amazing first blog post!", 
    "Alice")

// Get the post ID
let posts = db.query("SELECT * FROM posts WHERE title = ?", "My First Post")
let postId = posts[0]["id"]

// Add comments
db.execute("INSERT INTO comments (post_id, author, content) VALUES (?, ?, ?)",
    postId, "Bob", "Great post!")
db.execute("INSERT INTO comments (post_id, author, content) VALUES (?, ?, ?)",
    postId, "Charlie", "Very interesting!")

// Get post with comments
print("Post: " + posts[0]["title"])
print("By: " + posts[0]["author"])
print("Content: " + posts[0]["content"])
print("")
print("Comments:")

let comments = db.query("SELECT * FROM comments WHERE post_id = ?", postId)
for comment in comments {
    print("  - " + comment["author"] + ": " + comment["content"])
}

db.close()
```

### Example 3: E-commerce Backend (Advanced)

See `examples/todo_app_backend.pv` for a complete example with classes!

---

## Database Methods Reference

### `Database(connection_string)` - Connect

```privvy
let db = Database("myapp.db")                     // SQLite
let db = Database(":memory:")                     // SQLite in-memory
let db = Database("postgresql://user:pass@host/db")  // PostgreSQL
```

### `db.query(sql, ...params)` - Read Data

Returns an array of objects (dictionaries).

```privvy
let users = db.query("SELECT * FROM users")
let user = db.query("SELECT * FROM users WHERE id = ?", 5)
```

### `db.execute(sql, ...params)` - Modify Data

Use for INSERT, UPDATE, DELETE. Returns number of affected rows.

```privvy
db.execute("INSERT INTO users (name) VALUES (?)", "Alice")
db.execute("UPDATE users SET age = ? WHERE name = ?", 26, "Alice")
db.execute("DELETE FROM users WHERE id = ?", 5)
```

### `db.commit()` - Save Changes

Usually automatic, but you can control it:

```privvy
db.execute("INSERT INTO users (name) VALUES ('Alice')")
db.commit()  // Explicit save
```

### `db.rollback()` - Undo Changes

```privvy
db.execute("DELETE FROM users")  // Oops!
db.rollback()  // Phew, saved!
```

### `db.close()` - Close Connection

```privvy
db.close()
```

---

## Best Practices for Beginners

### ✅ DO

1. **Use parameters** to prevent SQL injection:
   ```privvy
   db.execute("SELECT * FROM users WHERE name = ?", username)
   ```

2. **Close connections** when done:
   ```privvy
   db.close()
   ```

3. **Use `IF NOT EXISTS`** when creating tables:
   ```privvy
   db.execute("CREATE TABLE IF NOT EXISTS users (...)")
   ```

4. **Start with SQLite** for learning and development

5. **Use classes** to organize your database code

### ❌ DON'T

1. **Don't concatenate user input** into SQL:
   ```privvy
   // BAD - Don't do this!
   db.execute("SELECT * FROM users WHERE name = '" + username + "'")
   
   // GOOD - Do this instead!
   db.execute("SELECT * FROM users WHERE name = ?", username)
   ```

2. **Don't forget to handle errors** (coming soon in Privvy!)

3. **Don't leave connections open** unnecessarily

---

## PostgreSQL Setup (For Production)

### 1. Install PostgreSQL

**Mac:**
```bash
brew install postgresql
brew services start postgresql
```

**Ubuntu/Debian:**
```bash
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

**Windows:**
Download from [postgresql.org](https://www.postgresql.org/download/windows/)

### 2. Create Database

```bash
# Create a database
createdb myapp

# Or use psql
psql postgres
CREATE DATABASE myapp;
\q
```

### 3. Get Connection String

```
postgresql://username:password@host:port/database
```

Example:
```
postgresql://postgres:mypassword@localhost:5432/myapp
```

### 4. Use in Privvy

```privvy
let db = Database("postgresql://postgres:mypassword@localhost:5432/myapp")
```

---

## Common Patterns

### Pattern 1: Check if exists before insert

```privvy
let existing = db.query("SELECT * FROM users WHERE email = ?", email)
if len(existing) == 0 {
    db.execute("INSERT INTO users (email) VALUES (?)", email)
    print("User created!")
} else {
    print("User already exists!")
}
```

### Pattern 2: Get last inserted ID (SQLite)

```privvy
db.execute("INSERT INTO users (name) VALUES (?)", "Alice")
let lastId = db.query("SELECT last_insert_rowid() as id")
print("New user ID: " + str(lastId[0]["id"]))
```

### Pattern 3: Count results

```privvy
let count = db.query("SELECT COUNT(*) as total FROM users")
print("Total users: " + str(count[0]["total"]))
```

### Pattern 4: Use with classes

```privvy
class UserService {
    constructor(database) {
        this.db = database
    }
    
    fun createUser(name, email) {
        this.db.execute("INSERT INTO users (name, email) VALUES (?, ?)", name, email)
    }
    
    fun getUser(id) {
        return this.db.query("SELECT * FROM users WHERE id = ?", id)
    }
    
    fun getAllUsers() {
        return this.db.query("SELECT * FROM users")
    }
}

let db = Database("app.db")
let userService = new UserService(db)
userService.createUser("Alice", "alice@example.com")
```

---

## Next Steps

1. ✅ Try `examples/database_sqlite.pv` - Basic SQLite example
2. ✅ Run `examples/todo_app_backend.pv` - Complete backend with classes
3. ✅ Install PostgreSQL and try `examples/database_postgres.pv`
4. 🚀 Build your own backend application!

---

## Troubleshooting

### Error: "Failed to connect to PostgreSQL"

**Solution:** Make sure PostgreSQL is installed and running:
```bash
# Check if running
pg_isready

# Start PostgreSQL
brew services start postgresql  # Mac
sudo systemctl start postgresql  # Linux
```

### Error: "No module named 'psycopg2'"

**Solution:** Install PostgreSQL support:
```bash
pip install psycopg2-binary
```

### Error: "Database is locked" (SQLite)

**Solution:** Close other connections or use a timeout:
```privvy
let db = Database("myapp.db")
// Do your work quickly
db.close()
```

---

## Why is Privvy's Database API So Simple?

Most languages require:
- Complex connection pooling
- ORM setup and configuration
- Multiple files and boilerplate
- Understanding of async/await

**Privvy gives you:**
```privvy
let db = Database("myapp.db")
let users = db.query("SELECT * FROM users")
```

**That's it!** 2 lines and you're querying a database! 🎉

---

## Coming Soon

- 🔜 MySQL support
- 🔜 Connection pooling
- 🔜 Database migrations
- 🔜 Built-in ORM
- 🔜 Async database operations

---

Happy coding! Build amazing backends with Privvy! 🚀

Questions? Check out `LANGUAGE_SPEC.md` or open an issue on GitHub!

