# logSystem Backend

A simple backend API for logging and retrieving system events, built with FastAPI, SQLAlchemy, MySQL, and Alembic for migrations.

---

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)

  * [MySQL Connection](#mysql-connection)
* [Database Setup & Migrations](#database-setup--migrations)
* [Running the Application](#running-the-application)
* [API Documentation](#api-documentation)
* [License](#license)

---

## Features

* CRUD endpoints for log entries
* FastAPI-powered async server
* SQLAlchemy ORM for database interactions
* Alembic for schema migrations

---

## Prerequisites

* Python 3.9+
* MySQL server (5.7+ or 8.0+)
* `git` (for cloning the repo)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Adler105JP/logSystem_backend.git
   cd logSystem_backend
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv .venv
   # On macOS/Linux
   source .venv/bin/activate
   # On Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install Python dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Configuration

### .env File

rename the `.env.example` to `.env`. Fill the nesesary environment variable 

```dotenv
# .env
SECRET_KEY=<Secret key for JWT>
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=1140
```

and then edit `.env` accordingly.

### MySQL Connection

The application reads its database URL from an environment variable named `DATABASE_URL`:

```dotenv
# .env
DATABASE_URL=mysql+mysqldb://<DB_USER>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>?charset=utf8mb4
```

* Replace `<DB_USER>`, `<DB_PASSWORD>`, `<DB_HOST>`, `<DB_PORT>`, and `<DB_NAME>` with your MySQL credentials and database name.
* The `?charset=utf8mb4` ensures full Unicode support.

---

## Database Setup & Migrations

1. **Ensure your MySQL database exists**

   * For MySQL: create manually (e.g., via phpMyAdmin or Workbench) a database matching `<DB_NAME>` in your `DATABASE_URL`.

2. **Run Alembic migrations**

   Set `sqlalchemy.url` as the same connection string at `DATABASE_URL` in `alembic.ini` 

   ```conf
   sqlalchemy.url = mysql+mysqldb://<DB_USER>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>?charset=utf8mb4
   ```

   ```bash
   alembic upgrade head
   ```

   This will create all tables and constraints as defined in your migration scripts.

---

## Running the Application

Start the FastAPI server with Uvicorn:

```bash
uvicorn app.main:app --reload
```

* Server will run on `http://127.0.0.1:8000`
* Interactive API docs available at `http://127.0.0.1:8000/docs`

---

## API Documentation

Once running, explore the Swagger UI at `/docs` or the ReDoc UI at `/redoc`.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
