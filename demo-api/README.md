# demo-api

A Privvy backend project

## Quick Start

### 1. Run Migrations

```bash
python3 privvy.py migrate.pv
```

### 2. Run Application

```bash
python3 privvy.py src/main.pv
```

## Project Structure

```
demo-api/
├── schema/
│   └── schema.pv       # Database schema (source of truth)
│
├── src/
│   └── main.pv         # Main application
│
├── tests/
│   └── (your tests)
│
├── migrate.pv          # Migration script
├── app.db              # SQLite database (generated)
│
└── privvy.py           # Privvy interpreter
```

## Database

**SQLite (default):** `let db = Database("app.db")`

**PostgreSQL:** `let db = Database("postgresql://user:pass@host:5432/dbname")`

## Learn More

- [Privvy Documentation](https://github.com/yourname/privvy)
- [ORM Guide](https://github.com/yourname/privvy/blob/main/ORM_GUIDE.md)
- [Database Guide](https://github.com/yourname/privvy/blob/main/DATABASE_GUIDE.md)

---

Built with ❤️ using Privvy - The Easiest Backend Language
