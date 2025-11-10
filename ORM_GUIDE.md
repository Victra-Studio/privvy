## Privvy ORM - The Easiest Database ORM Ever! 🚀

**Build a complete backend in < 50 lines of code!**

Privvy's built-in ORM makes database operations ridiculously simple. No complex configuration, no boilerplate - just pure simplicity.

---

## Why Privvy ORM?

✅ **Zero Configuration** - No setup files or complex configs  
✅ **Minimal Code** - Define models in 2 lines  
✅ **Beginner Friendly** - Easy to learn, easy to use  
✅ **Full CRUD** - Create, Read, Update, Delete in one line each  
✅ **Type Safe** - Field definitions with validation  
✅ **Works Everywhere** - SQLite and PostgreSQL support  

---

## Quick Start (60 Seconds!)

```privvy
// 1. Connect to database
let db = Database("myapp.db")

// 2. Define a model (2 lines!)
let userFields = dict(["id", "INTEGER PRIMARY KEY AUTOINCREMENT", "name", "TEXT", "email", "TEXT UNIQUE"])
let User = Model("users", userFields)

// 3. Create the table
User.migrate(db)

// 4. Create a user (1 line!)
let userData = dict(["name", "Alice", "email", "alice@example.com"])
User.create(db, userData)

// 5. Query users (1 line!)
let users = User.all(db)
```

**That's it!** You're using a production-ready ORM! 🎉

---

## Installation

**Nothing to install!** ORM is built into Privvy. Just start coding!

```bash
# Run any ORM example
python3 privvy.py examples/orm_simple.pv
```

---

## Core Concepts

### 1. Models

A **Model** represents a database table. Define the table name and fields:

```privvy
let fields = dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "name", "TEXT NOT NULL",
    "email", "TEXT UNIQUE",
    "age", "INTEGER"
])
let User = Model("users", fields)
```

**Field Types:**
- `INTEGER` - Whole numbers
- `TEXT` - Strings
- `REAL` - Decimal numbers
- `BLOB` - Binary data
- `TIMESTAMP` - Date/time

**Constraints:**
- `PRIMARY KEY` - Unique identifier
- `AUTOINCREMENT` - Auto-generate IDs
- `NOT NULL` - Required field
- `UNIQUE` - No duplicates
- `DEFAULT value` - Default value

### 2. Migration

Create tables in the database:

```privvy
User.migrate(db)
```

This creates the table if it doesn't exist. **Safe to run multiple times!**

### 3. CRUD Operations

#### Create (INSERT)

```privvy
let userData = dict(["name", "Alice", "email", "alice@example.com", "age", 25])
let userId = User.create(db, userData)
print("Created user with ID: " + str(userId))
```

#### Read (SELECT)

```privvy
// Get all records
let users = User.all(db)

// Find by ID
let user = User.find(db, 1)

// Find by field
let alices = User.findBy(db, "name", "Alice")

// Custom WHERE query
let adults = User.where(db, "age >= ?", 18)
```

#### Update

```privvy
let updateData = dict(["age", 26, "email", "alice_new@example.com"])
User.update(db, 1, updateData)
```

#### Delete

```privvy
User.delete(db, 1)
```

---

## Complete API Reference

### Model Creation

#### `Model(tableName, fields)`

Create a new model definition.

**Parameters:**
- `tableName` (string): Name of the database table
- `fields` (dict): Field definitions

**Returns:** Model instance

**Example:**
```privvy
let fields = dict(["id", "INTEGER PRIMARY KEY", "name", "TEXT"])
let User = Model("users", fields)
```

---

### Model Methods

#### `model.migrate(db)`

Create the table in the database.

**Parameters:**
- `db`: Database connection

**Returns:** null

**Example:**
```privvy
User.migrate(db)
```

---

#### `model.create(db, data)`

Insert a new record.

**Parameters:**
- `db`: Database connection
- `data` (dict): Field values

**Returns:** Inserted record ID

**Example:**
```privvy
let userData = dict(["name", "Alice", "email", "alice@example.com"])
let userId = User.create(db, userData)
```

---

#### `model.find(db, id)`

Find a record by ID.

**Parameters:**
- `db`: Database connection
- `id`: Record ID

**Returns:** Record object (dict) or null

**Example:**
```privvy
let user = User.find(db, 1)
if (user != null) {
    print("Found: " + user["name"])
}
```

---

#### `model.findBy(db, field, value)`

Find records by field value.

**Parameters:**
- `db`: Database connection
- `field` (string): Field name
- `value`: Value to search for

**Returns:** Array of records

**Example:**
```privvy
let alices = User.findBy(db, "name", "Alice")
```

---

#### `model.all(db)`

Get all records.

**Parameters:**
- `db`: Database connection

**Returns:** Array of all records

**Example:**
```privvy
let users = User.all(db)
for (let i = 0; i < len(users); i = i + 1) {
    print(users[i]["name"])
}
```

---

#### `model.where(db, condition, ...params)`

Query with custom WHERE clause.

**Parameters:**
- `db`: Database connection
- `condition` (string): SQL WHERE condition
- `...params`: Parameters for placeholders

**Returns:** Array of matching records

**Examples:**
```privvy
// Simple condition
let adults = User.where(db, "age >= 18")

// With parameters
let result = User.where(db, "age > ? AND name LIKE ?", 25, "A%")

// Complex queries
let users = User.where(db, "created_at > ? ORDER BY age DESC", "2024-01-01")
```

---

#### `model.update(db, id, data)`

Update a record by ID.

**Parameters:**
- `db`: Database connection
- `id`: Record ID
- `data` (dict): Fields to update

**Returns:** Number of rows updated

**Example:**
```privvy
let updates = dict(["age", 26, "email", "newemail@example.com"])
let rowsUpdated = User.update(db, 1, updates)
```

---

#### `model.delete(db, id)`

Delete a record by ID.

**Parameters:**
- `db`: Database connection
- `id`: Record ID

**Returns:** Number of rows deleted

**Example:**
```privvy
User.delete(db, 1)
```

---

#### `model.count(db)`

Count total records.

**Parameters:**
- `db`: Database connection

**Returns:** Total count

**Example:**
```privvy
let total = User.count(db)
print("Total users: " + str(total))
```

---

#### `model.drop(db)`

Drop (delete) the table. **USE WITH CAUTION!**

**Parameters:**
- `db`: Database connection

**Returns:** null

**Example:**
```privvy
User.drop(db)  // Deletes the entire table!
```

---

## Patterns & Best Practices

### Pattern 1: Schema File

Create a `schema.pv` file with all your models:

```privvy
// schema.pv
let UserFields = dict(["id", "INTEGER PRIMARY KEY AUTOINCREMENT", "name", "TEXT", "email", "TEXT UNIQUE"])
let User = Model("users", UserFields)

let PostFields = dict(["id", "INTEGER PRIMARY KEY AUTOINCREMENT", "user_id", "INTEGER", "title", "TEXT", "content", "TEXT"])
let Post = Model("posts", PostFields)

// Export or use directly
```

### Pattern 2: Check Before Create

```privvy
let existing = User.findBy(db, "email", email)
if (len(existing) == 0) {
    User.create(db, userData)
} else {
    print("User already exists!")
}
```

### Pattern 3: Relationships

```privvy
// Get user's posts
let user = User.find(db, 1)
let userPosts = Post.findBy(db, "user_id", user["id"])

// Get post with author
let post = Post.find(db, 1)
let author = User.find(db, post["user_id"])
```

### Pattern 4: Validation

```privvy
fun validateEmail(email) {
    // Simple validation
    if (len(email) < 5) {
        return false
    }
    return true
}

if (validateEmail(email)) {
    let userData = dict(["email", email])
    User.create(db, userData)
} else {
    print("Invalid email!")
}
```

### Pattern 5: Transaction-like Pattern

```privvy
// Create user and initial post together
let userId = User.create(db, userData)
let postData = dict(["user_id", userId, "title", "First Post"])
Post.create(db, postData)
```

---

## Complete Examples

### Example 1: User Management

```privvy
let db = Database("users.db")

// Define model
let fields = dict(["id", "INTEGER PRIMARY KEY AUTOINCREMENT", "username", "TEXT UNIQUE", "email", "TEXT", "age", "INTEGER"])
let User = Model("users", fields)

// Migrate
User.migrate(db)

// Create users
User.create(db, dict(["username", "alice", "email", "alice@example.com", "age", 25]))
User.create(db, dict(["username", "bob", "email", "bob@example.com", "age", 30]))

// Get all users
let users = User.all(db)
print("Total users: " + str(len(users)))

// Find specific user
let alice = User.findBy(db, "username", "alice")
print("Alice's email: " + alice[0]["email"])

// Update user
User.update(db, 1, dict(["age", 26]))

// Delete user
User.delete(db, 2)

db.close()
```

### Example 2: Blog System

See `examples/blog_backend_orm.pv` for a complete blog with:
- Users
- Posts
- Comments
- Relationships
- Queries

**< 100 lines of code for a full backend!**

### Example 3: E-commerce

```privvy
let db = Database("shop.db")

// Products
let productFields = dict(["id", "INTEGER PRIMARY KEY AUTOINCREMENT", "name", "TEXT", "price", "REAL", "stock", "INTEGER"])
let Product = Model("products", productFields)

// Orders
let orderFields = dict(["id", "INTEGER PRIMARY KEY AUTOINCREMENT", "user_id", "INTEGER", "product_id", "INTEGER", "quantity", "INTEGER", "total", "REAL"])
let Order = Model("orders", orderFields)

// Migrate
Product.migrate(db)
Order.migrate(db)

// Add products
Product.create(db, dict(["name", "Laptop", "price", 999.99, "stock", 10]))
Product.create(db, dict(["name", "Mouse", "price", 29.99, "stock", 50]))

// Create order
let order = dict(["user_id", 1, "product_id", 1, "quantity", 1, "total", 999.99])
Order.create(db, order)

// Update stock
let product = Product.find(db, 1)
let newStock = product["stock"] - 1
Product.update(db, 1, dict(["stock", newStock]))

// Get user's orders
let userOrders = Order.findBy(db, "user_id", 1)
print("Orders: " + str(len(userOrders)))

db.close()
```

---

## Advanced Features

### Custom Queries

Use `where()` for complex queries:

```privvy
// Multiple conditions
let results = User.where(db, "age > 18 AND email IS NOT NULL")

// Sorting
let sorted = User.where(db, "1=1 ORDER BY age DESC")

// Limits
let top10 = User.where(db, "1=1 ORDER BY created_at DESC LIMIT 10")

// Joins (advanced)
let query = "SELECT users.name, posts.title FROM users JOIN posts ON users.id = posts.user_id WHERE users.age > ?"
let results = db.query(query, 18)
```

### Helper Functions

#### dict() - Create Dictionary

```privvy
// Create from array of key-value pairs
let data = dict(["name", "Alice", "age", 25])

// Access values
print(data["name"])  // "Alice"
```

---

## PostgreSQL Support

Everything works the same with PostgreSQL!

```privvy
// Connect to PostgreSQL
let db = Database("postgresql://user:password@localhost:5432/mydb")

// Same API!
User.migrate(db)
User.create(db, userData)
let users = User.all(db)
```

---

## Migration Commands

### Create All Tables

```privvy
// Create a migrate function
fun migrateAll(db) {
    User.migrate(db)
    Post.migrate(db)
    Comment.migrate(db)
    print("✅ All tables created!")
}

let db = Database("app.db")
migrateAll(db)
```

### Drop and Recreate

```privvy
fun resetDatabase(db) {
    User.drop(db)
    Post.drop(db)
    
    User.migrate(db)
    Post.migrate(db)
    
    print("✅ Database reset!")
}
```

### Seed Data

```privvy
fun seedDatabase(db) {
    // Create test users
    User.create(db, dict(["name", "Test User 1", "email", "test1@example.com"]))
    User.create(db, dict(["name", "Test User 2", "email", "test2@example.com"]))
    
    print("✅ Database seeded!")
}
```

---

## Troubleshooting

### Error: "Table already exists"

**Solution:** ORM uses `CREATE TABLE IF NOT EXISTS`, so this shouldn't happen. If it does, use `migrate()` which is safe to run multiple times.

### Error: "Cannot find field"

**Solution:** Make sure field names match exactly:
```privvy
// Wrong
User.findBy(db, "Name", "Alice")  // Capital N

// Correct
User.findBy(db, "name", "Alice")  // lowercase n
```

### Performance Tips

1. **Use `findBy()` instead of `where()` for simple queries**
   ```privvy
   // Faster
   User.findBy(db, "email", email)
   
   // Slower
   User.where(db, "email = ?", email)
   ```

2. **Add indexes for frequently searched fields** (advanced)
   ```privvy
   db.execute("CREATE INDEX IF NOT EXISTS idx_user_email ON users(email)")
   ```

3. **Use `count()` instead of `len(all())`**
   ```privvy
   // Fast
   let total = User.count(db)
   
   // Slow (loads all records)
   let total = len(User.all(db))
   ```

---

## Comparison with Other ORMs

### Django ORM (Python)

**Django:**
```python
# settings.py configuration
# models.py
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Usage
user = User.objects.create(name="Alice", email="alice@example.com")
```

**Privvy:**
```privvy
let User = Model("users", dict(["id", "INTEGER PRIMARY KEY", "name", "TEXT", "email", "TEXT UNIQUE"]))
User.migrate(db)
User.create(db, dict(["name", "Alice", "email", "alice@example.com"]))
```

**Winner:** Privvy - 3 lines vs 10+ lines! ✅

### ActiveRecord (Ruby on Rails)

**Rails:**
```ruby
# Generate model
rails generate model User name:string email:string
rake db:migrate

# Usage
User.create(name: "Alice", email: "alice@example.com")
```

**Privvy:**
```privvy
let User = Model("users", dict(["name", "TEXT", "email", "TEXT"]))
User.migrate(db)
User.create(db, dict(["name", "Alice", "email", "alice@example.com"]))
```

**Winner:** Tie - Both are simple! 🤝

---

## Coming Soon

- 🔜 Model relationships (`hasMany`, `belongsTo`)
- 🔜 Automatic validation
- 🔜 Migration versioning
- 🔜 Query builder
- 🔜 Transactions
- 🔜 Connection pooling

---

## Summary

Privvy ORM makes backend development **ridiculously easy**:

```privvy
// Define (2 lines)
let fields = dict(["id", "INTEGER PRIMARY KEY", "name", "TEXT"])
let User = Model("users", fields)

// Create table (1 line)
User.migrate(db)

// CRUD operations (1 line each)
User.create(db, data)
User.find(db, 1)
User.all(db)
User.update(db, 1, data)
User.delete(db, 1)
```

**That's it!** No configuration, no boilerplate, just pure simplicity! 🚀

---

## Next Steps

1. ✅ Try `examples/orm_simple.pv` - Basic ORM
2. ✅ Run `examples/blog_backend_orm.pv` - Complete blog backend
3. ✅ Create your own `schema.pv` file
4. 🚀 Build your own backend application!

Happy coding with Privvy ORM! 🎉

**Questions?** Check out `DATABASE_GUIDE.md` for more database info!

