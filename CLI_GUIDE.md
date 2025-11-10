# Privvy Database CLI - Like Prisma, But Simpler! 🚀

**Manage your database with a beautiful CLI - Inspired by Prisma!**

The Privvy Database CLI makes database management as simple as possible. Generate schemas, run migrations, seed data - all with clean, intuitive commands.

---

## Quick Start (2 Minutes!)

```bash
# 1. Initialize a new database project
python3 privvy-db.py init

# 2. Run migrations (create tables)
python3 privvy.py db-migrate.pv

# 3. Seed with sample data
python3 privvy.py db-seed.pv

# Done! Your database is ready! 🎉
```

---

## Installation

**Already installed!** The CLI comes with Privvy. Just make sure it's executable:

```bash
chmod +x privvy-db.py
```

Optional: Create an alias for easier use:

```bash
# Add to your ~/.zshrc or ~/.bashrc
alias privvy-db="python3 /Users/apple/Desktop/privvy/privvy-db.py"

# Then use it like:
privvy-db init
```

---

## Commands

### `privvy-db init`

Create a new `schema.pv` file with example models.

**Usage:**
```bash
python3 privvy-db.py init
```

**What it does:**
- Creates `schema.pv` with User and Post models
- Includes helpful comments and structure
- Safe to run (asks before overwriting)

**Example Output:**
```
✅ Created schema.pv
ℹ️  Edit schema.pv to define your models
ℹ️  Then run: privvy-db migrate
```

---

### `privvy-db migrate`

Generate migration scripts from your schema.

**Usage:**
```bash
python3 privvy-db.py migrate
```

**What it does:**
- Creates `migrate.pv` helper script
- Includes instructions for running migrations
- Uses `DATABASE_URL` environment variable or defaults to `app.db`

**Then run:**
```bash
python3 privvy.py db-migrate.pv
```

---

### `privvy-db seed`

Seed your database with test data.

**Usage:**
```bash
python3 privvy-db.py seed
```

**What it does:**
- Creates `seed.pv` template if it doesn't exist
- Runs the seed script if it exists
- Perfect for development data

**Then run:**
```bash
python3 privvy.py db-seed.pv
```

---

### `privvy-db reset`

Reset your database (drop all tables).

**Usage:**
```bash
python3 privvy-db.py reset
```

**Warning:** This deletes ALL data! Use with caution!

**What it does:**
- Creates `reset.pv` script
- Asks for confirmation before running
- Drops all tables

---

### `privvy-db push`

Push schema changes to database (coming soon!).

**Usage:**
```bash
python3 privvy-db.py push
```

**Future feature:**
- Will automatically detect schema changes
- Create and run migrations
- Like `prisma db push`

---

### `privvy-db studio`

Open database browser (coming soon!).

**Usage:**
```bash
python3 privvy-db.py studio
```

**Future feature:**
- Visual database browser
- Like Prisma Studio
- View and edit data

---

## Complete Workflow

### 1. Start a New Project

```bash
# Create project directory
mkdir my-blog
cd my-blog

# Copy Privvy runtime
cp -r /path/to/privvy/* .

# Initialize database
python3 privvy-db.py init

# You now have:
#   - schema.pv (define your models here)
```

### 2. Define Your Models

Edit `schema.pv`:

```privvy
// Define User model
let User = Model("users", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "username", "TEXT UNIQUE NOT NULL",
    "email", "TEXT UNIQUE NOT NULL",
    "password", "TEXT NOT NULL",
    "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
]))

// Define Post model
let Post = Model("posts", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "user_id", "INTEGER NOT NULL",
    "title", "TEXT NOT NULL",
    "content", "TEXT",
    "published", "INTEGER DEFAULT 0",
    "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
]))
```

### 3. Create Migration Script

Copy your models to `db-migrate.pv`:

```privvy
let db = Database("app.db")

// Paste your models from schema.pv
let User = Model("users", dict([...]))
let Post = Model("posts", dict([...]))

// Run migrations
User.migrate(db)
Post.migrate(db)

db.close()
```

### 4. Run Migrations

```bash
python3 privvy.py db-migrate.pv
```

Output:
```
📡 Connected to database: app.db
✓ Created table: users
✓ Created table: posts
✅ All migrations complete!
```

### 5. Create Seed Script

Create `db-seed.pv`:

```privvy
let db = Database("app.db")

// Define models (same as migration)
let User = Model("users", dict([...]))

// Create test data
let user1 = dict(["username", "alice", "email", "alice@example.com", "password", "hashed"])
User.create(db, user1)

db.close()
```

### 6. Seed Database

```bash
python3 privvy.py db-seed.pv
```

### 7. Build Your App!

```privvy
// app.pv - Your application
let db = Database("app.db")
let User = Model("users", dict([...]))

// Use your models
let users = User.all(db)
print("Total users: " + str(len(users)))

db.close()
```

---

## Environment Variables

### `DATABASE_URL`

Set your database connection string:

```bash
# SQLite (default)
export DATABASE_URL="app.db"

# PostgreSQL
export DATABASE_URL="postgresql://user:password@localhost:5432/mydb"

# Use in your scripts
python3 privvy.py db-migrate.pv
```

---

## File Structure

A typical Privvy database project looks like:

```
my-project/
├── privvy.py              # Privvy interpreter
├── lexer.py               # Language lexer
├── parser.py              # Language parser
├── interpreter.py         # Language interpreter (with ORM!)
├── ast_nodes.py           # AST definitions
├── token_types.py         # Token types
│
├── privvy-db.py           # Database CLI tool
│
├── schema.pv              # Your database schema (models)
├── db-migrate.pv          # Migration script
├── db-seed.pv             # Seeding script
│
├── app.db                 # SQLite database (generated)
│
└── src/
    ├── main.pv            # Your application
    ├── models.pv          # Model definitions
    └── routes.pv          # API routes (future)
```

---

## Examples

### Example 1: Blog Platform

```privvy
// schema.pv
let User = Model("users", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "username", "TEXT UNIQUE NOT NULL",
    "email", "TEXT UNIQUE NOT NULL",
    "bio", "TEXT",
    "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
]))

let Post = Model("posts", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "user_id", "INTEGER NOT NULL",
    "title", "TEXT NOT NULL",
    "content", "TEXT",
    "published", "INTEGER DEFAULT 0",
    "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
]))

let Comment = Model("comments", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "post_id", "INTEGER NOT NULL",
    "user_id", "INTEGER NOT NULL",
    "content", "TEXT NOT NULL",
    "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
]))
```

**Workflow:**
```bash
# 1. Create migrations
python3 privvy.py db-migrate.pv

# 2. Seed data
python3 privvy.py db-seed.pv

# 3. Run app
python3 privvy.py src/main.pv
```

### Example 2: E-commerce

```privvy
// schema.pv
let Product = Model("products", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "name", "TEXT NOT NULL",
    "description", "TEXT",
    "price", "REAL NOT NULL",
    "stock", "INTEGER DEFAULT 0",
    "category", "TEXT",
    "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
]))

let Order = Model("orders", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "user_id", "INTEGER NOT NULL",
    "total", "REAL NOT NULL",
    "status", "TEXT DEFAULT 'pending'",
    "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
]))

let OrderItem = Model("order_items", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "order_id", "INTEGER NOT NULL",
    "product_id", "INTEGER NOT NULL",
    "quantity", "INTEGER NOT NULL",
    "price", "REAL NOT NULL"
]))
```

---

## Comparison with Prisma

### Prisma

```bash
# Initialize
npx prisma init

# Create schema (prisma/schema.prisma)
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}

# Run migrations
npx prisma migrate dev --name init

# Seed
npx prisma db seed

# Studio
npx prisma studio
```

### Privvy

```bash
# Initialize
python3 privvy-db.py init

# Create schema (schema.pv)
let User = Model("users", dict([
    "id", "INTEGER PRIMARY KEY AUTOINCREMENT",
    "email", "TEXT UNIQUE",
    "name", "TEXT"
]))

# Run migrations
python3 privvy.py db-migrate.pv

# Seed
python3 privvy.py db-seed.pv

# Studio (coming soon!)
python3 privvy-db.py studio
```

**Comparison:**
- ✅ Simpler syntax (no DSL, just Privvy code!)
- ✅ Fewer files
- ✅ No Node.js required
- ✅ Easier to understand for beginners
- ⏳ Some features coming soon

---

## Tips & Best Practices

### 1. Keep Models in One Place

Create a `models.pv` file with all model definitions:

```privvy
// models.pv
let User = Model("users", dict([...]))
let Post = Model("posts", dict([...]))
let Comment = Model("comments", dict([...]))
```

Use it in all scripts:
```privvy
// Import would go here (feature coming soon!)
// For now, copy-paste model definitions
```

### 2. Version Your Migrations

Keep track of migrations:

```
migrations/
├── 001_initial.pv
├── 002_add_posts.pv
├── 003_add_comments.pv
```

### 3. Separate Dev and Production DBs

```bash
# Development
export DATABASE_URL="dev.db"

# Production
export DATABASE_URL="postgresql://user:pass@prod-server/db"
```

### 4. Use Seed Data for Testing

```privvy
// seed.pv
fun createTestUser() {
    let user = dict(["username", "test_user", ...])
    return User.create(db, user)
}

fun createTestPost(userId) {
    let post = dict(["user_id", userId, ...])
    return Post.create(db, post)
}

// Create test data
let userId = createTestUser()
createTestPost(userId)
```

### 5. Backup Before Reset

```bash
# Backup database
cp app.db app.db.backup

# Reset
python3 privvy-db.py reset

# Restore if needed
cp app.db.backup app.db
```

---

## Troubleshooting

### Error: "schema.pv not found"

**Solution:** Run `python3 privvy-db.py init` first

### Error: "table already exists"

**Solution:** The ORM uses `CREATE TABLE IF NOT EXISTS`, so this is usually safe. If you want a fresh start, run `python3 privvy-db.py reset`

### Error: "Database is locked" (SQLite)

**Solution:**
1. Close all connections: `db.close()`
2. Make sure no other processes are using the database
3. Try again

### Models don't match between files

**Solution:** Copy model definitions consistently across:
- `db-migrate.pv`
- `db-seed.pv`
- Your application files

---

## Coming Soon

- 🔜 `privvy-db push` - Auto-detect and apply schema changes
- 🔜 `privvy-db studio` - Visual database browser
- 🔜 `privvy-db generate` - Generate boilerplate code
- 🔜 `privvy-db introspect` - Generate schema from existing database
- 🔜 Migration versioning and rollback
- 🔜 Schema validation
- 🔜 Import/export models

---

## Summary

The Privvy Database CLI makes database management **ridiculously easy**:

```bash
# One command to initialize
python3 privvy-db.py init

# One command to migrate
python3 privvy.py db-migrate.pv

# One command to seed
python3 privvy.py db-seed.pv
```

**That's it!** No complex configuration, no boilerplate, just pure simplicity! 🚀

---

## Next Steps

1. ✅ Try the examples: `python3 privvy.py examples/orm_simple.pv`
2. ✅ Initialize your project: `python3 privvy-db.py init`
3. ✅ Define your schema in `schema.pv`
4. ✅ Run migrations: `python3 privvy.py db-migrate.pv`
5. 🚀 Build your application!

Happy coding with Privvy Database CLI! 🎉

**Questions?** Check out `ORM_GUIDE.md` or `DATABASE_GUIDE.md`!

