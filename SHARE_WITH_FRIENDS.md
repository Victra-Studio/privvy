# Share Privvy with Friends! 🚀

**Send them this link or file!**

---

## What is Privvy?

**The easiest backend programming language** with:
- ✅ Built-in database ORM
- ✅ One command to create projects
- ✅ Zero configuration
- ✅ PostgreSQL & SQLite support

**Build a backend in 2 minutes!**

---

## Get Started (3 steps!)

### Step 1: Get Privvy

```bash
git clone https://github.com/yourname/privvy.git
cd privvy
```

### Step 2: Create Project

```bash
python3 privvy-cli.py create-project my-api
cd my-api
```

### Step 3: Run It!

```bash
python3 privvy.py migrate.pv
python3 privvy.py src/main.pv
```

**Done!** You have a working backend! 🎉

---

## Example Code

```privvy
// Connect to database
let db = Database("app.db")

// Define model
let User = Model("users", dict([
    "id", "SERIAL PRIMARY KEY",
    "username", "TEXT UNIQUE",
    "email", "TEXT"
]))

// Create table
User.migrate(db)

// Add user
User.create(db, dict(["username", "alice", "email", "alice@example.com"]))

// Get all users
let users = User.all(db)
print("Total users: " + str(len(users)))

db.close()
```

**That's all the code you need for a database backend!** 🚀

---

## What You Can Build

- 🔐 Authentication systems
- 📝 CRUD APIs
- 🛒 E-commerce backends
- 💬 Chat applications
- 📱 Mobile app backends
- 📊 Data management tools

---

## Requirements

- Python 3.7+ (that's it!)
- Optional: `pip install psycopg2-binary` (for PostgreSQL)

---

## Learn More

After installation, check these files:
- `QUICK_START.md` - Detailed tutorial
- `ORM_GUIDE.md` - Database operations
- `examples/` - Working examples

---

## Why Privvy?

### Traditional Backend (Django/Express):
```python
# 10+ files
# Complex configuration
# Hours of setup
# Steep learning curve
```

### Privvy:
```bash
python3 privvy-cli.py create-project my-api
cd my-api
python3 privvy.py migrate.pv
# Done in 30 seconds!
```

---

## Share This!

**GitHub:** https://github.com/yourname/privvy

**Quick Link:** Give friends this file or the `QUICK_START.md`

**Zip File:** Run `./share-privvy.sh` to create a shareable package

---

**Built with ❤️ for beginners learning backend development**

🌟 **Star on GitHub if you love it!**

