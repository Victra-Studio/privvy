# Privvy Quick Start - For Your Friends! 🚀

**Build a complete backend in 5 minutes!**

---

## What is Privvy?

Privvy is **the easiest backend programming language ever made**. It has:

✅ **Built-in Database ORM** - Connect and query in 1-2 lines  
✅ **Zero Configuration** - No complex setup  
✅ **Beginner Friendly** - Easy to learn  
✅ **PostgreSQL & SQLite** - Works with real databases  
✅ **One Command Setup** - Create projects instantly  

---

## Install (30 seconds)

### Step 1: Get Privvy

```bash
# Clone or download
git clone https://github.com/yourname/privvy.git
cd privvy
```

**OR download the zip file and unzip it**

### Step 2: Test it

```bash
python3 privvy-cli.py help
```

You should see:

```
╔════════════════════════════════════════╗
║         Privvy CLI v1.0.0             ║
║   The Easiest Backend Language Ever   ║
╚════════════════════════════════════════╝
```

**Done!** ✅

---

## Create Your First Backend (2 minutes)

### Step 1: Create Project

```bash
python3 privvy-cli.py create-project my-api
cd my-api
```

This creates:
- ✅ Complete backend project
- ✅ Database models
- ✅ Migration scripts
- ✅ Example code
- ✅ Everything ready to run!

### Step 2: Run Migrations

```bash
python3 privvy.py migrate.pv
```

Output:
```
=== Running Migrations ===
📡 Connected to database
🔨 Creating tables...
  ✓ Created table: users
  ✓ Created table: posts
✅ All migrations complete!
```

### Step 3: Run Your App

```bash
python3 privvy.py src/main.pv
```

**That's it!** You have a working backend! 🎉

---

## Your First API (5 minutes)

Let's build a simple user API!

### Edit `src/main.pv`:

```privvy
// Connect to database
let db = Database("app.db")

// Define User model
let User = Model("users", dict([
    "id", "SERIAL PRIMARY KEY",
    "username", "TEXT UNIQUE NOT NULL",
    "email", "TEXT UNIQUE NOT NULL"
]))

// Migrate
User.migrate(db)

// CREATE - Add a user
let userData = dict(["username", "alice", "email", "alice@example.com"])
let userId = User.create(db, userData)
print("Created user ID: " + str(userId))

// READ - Get all users
let users = User.all(db)
print("Total users: " + str(len(users)))

// READ - Find by ID
let user = User.find(db, userId)
print("Found: " + user["username"])

// UPDATE - Change email
User.update(db, userId, dict(["email", "newemail@example.com"]))
print("Updated!")

// DELETE - Remove user
User.delete(db, userId)
print("Deleted!")

db.close()
```

### Run it:

```bash
python3 privvy.py src/main.pv
```

**You just did full CRUD operations!** 🚀

---

## Example Projects

### 1. Todo App

```privvy
let Todo = Model("todos", dict([
    "id", "SERIAL PRIMARY KEY",
    "title", "TEXT NOT NULL",
    "completed", "INTEGER DEFAULT 0"
]))

Todo.migrate(db)

// Add todo
Todo.create(db, dict(["title", "Learn Privvy"]))

// Get all todos
let todos = Todo.all(db)
```

### 2. Blog Backend

```privvy
let Post = Model("posts", dict([
    "id", "SERIAL PRIMARY KEY",
    "title", "TEXT NOT NULL",
    "content", "TEXT",
    "published", "INTEGER DEFAULT 0"
]))

Post.migrate(db)

// Create post
Post.create(db, dict(["title", "My First Post", "content", "Hello World!"]))

// Get published posts
let published = Post.where(db, "published = 1")
```

### 3. User Auth (See `test priv` project!)

Full authentication system with:
- User registration
- Login
- Profile management
- Password hashing

---

## What You Can Build

Perfect for:
- 🔐 **Authentication APIs**
- 📝 **CRUD APIs**
- 📊 **Data Management**
- 🛒 **E-commerce Backends**
- 💬 **Chat Applications**
- 📱 **Mobile App Backends**

---

## Commands Cheat Sheet

```bash
# Create new project
python3 privvy-cli.py create-project <name>

# Run a file
python3 privvy.py <file.pv>

# Run migrations
python3 privvy.py migrate.pv

# Run main app
python3 privvy.py src/main.pv
```

---

## Database Support

### SQLite (Default - Easy!)

```privvy
let db = Database("app.db")  // No setup required!
```

### PostgreSQL (Production)

```privvy
let db = Database("postgresql://user:pass@host:5432/dbname")
```

Works with:
- ✅ Neon
- ✅ Supabase
- ✅ Heroku
- ✅ Railway
- ✅ Local PostgreSQL

---

## Learn More

### Core Concepts

**1. Models (Tables)**
```privvy
let User = Model("users", dict(["id", "SERIAL PRIMARY KEY", "name", "TEXT"]))
```

**2. Create Table**
```privvy
User.migrate(db)
```

**3. CRUD Operations**
```privvy
// Create
User.create(db, dict(["name", "Alice"]))

// Read
User.all(db)
User.find(db, 1)
User.findBy(db, "name", "Alice")

// Update
User.update(db, 1, dict(["name", "Bob"]))

// Delete
User.delete(db, 1)
```

### Full Documentation

- [README.md](README.md) - Overview
- [ORM_GUIDE.md](ORM_GUIDE.md) - Database operations (40+ pages!)
- [DATABASE_GUIDE.md](DATABASE_GUIDE.md) - Database basics
- [CLI_GUIDE.md](CLI_GUIDE.md) - CLI commands
- [INSTALL.md](INSTALL.md) - Installation guide

---

## Examples Included

Try these:

```bash
# Basic ORM
python3 privvy.py examples/orm_simple.pv

# Complete blog backend
python3 privvy.py examples/blog_backend_orm.pv

# Database basics
python3 privvy.py examples/database_sqlite.pv
```

---

## Troubleshooting

### "python3: command not found"

Install Python: https://www.python.org/downloads/

### "No module named 'psycopg2'"

For PostgreSQL support:
```bash
pip3 install psycopg2-binary
```

### Need Help?

- Check [INSTALL.md](INSTALL.md)
- See [examples/](examples/) folder
- Read the guides in the docs folder

---

## Share with Friends!

**Option 1: GitHub**
```bash
git clone https://github.com/yourname/privvy.git
cd privvy
python3 privvy-cli.py create-project my-api
```

**Option 2: Zip File**
1. Zip the `privvy` folder
2. Share with friends
3. They unzip and run:
   ```bash
   cd privvy
   python3 privvy-cli.py create-project my-api
   ```

---

## Why Privvy?

### vs Django (Python)
**Django:** 10+ files, complex config, steep learning curve  
**Privvy:** 1 command, 2 lines for database, instant results  

### vs Express.js (Node)
**Express:** Need ORM library, config files, middleware setup  
**Privvy:** Built-in ORM, zero config, just code  

### vs Ruby on Rails
**Rails:** Magic, conventions, lots to learn  
**Privvy:** Simple, explicit, easy to understand  

**Privvy = Easiest backend language for beginners!** ✅

---

## Next Steps

1. ✅ Install Privvy
2. ✅ Create first project
3. ✅ Run migrations
4. ✅ Build something!

**Now go build something awesome!** 🚀

---

## Questions?

- 📖 Read the guides
- 👀 Check examples
- 💬 Ask questions
- 🌟 Star on GitHub!

**Welcome to Privvy! Happy coding! 🎉**

