# shared_utils

`shared_utils` is a Python utility package that simplifies database connections for MySQL, SQL Server (MSSQL), and PostgreSQL using SQLAlchemy. It provides easy-to-use functions to create SQLAlchemy engines, with configuration handled securely through environment variables.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing Connections](#testing-connections)
- [Dependencies](#dependencies)
- [AI Assistant Prompt](#ai-assistant-prompt)

---

## Installation

To install `shared_utils`, clone the repository and install it in editable mode with `pip`:

```bash
git clone https://github.com/willpalmer81/shared_utils.git
cd shared_utils
pip install -e .
```

This will make the `shared_utils` package available in your environment, including a test script to verify connections.

## Configuration

`shared_utils` uses environment variables stored in a `.env` file for securely managing database credentials. Place your `.env` file in the root directory of the project (next to `setup.py`). It should follow this format:

```plaintext
# MySQL configuration
MYSQL_USER=<your_mysql_user>
MYSQL_PASSWORD=<your_mysql_password>
MYSQL_HOST=<your_mysql_host>
MYSQL_PORT=<your_mysql_port>
MYSQL_DATABASE=<your_mysql_database>

# MSSQL (SQL Server) configuration
SQL_SERVER=<your_sql_server_host>
SQL_DATABASE=<your_sql_server_database>
SQL_USERNAME=<your_sql_server_user>
SQL_PASSWORD=<your_sql_server_password>

# PostgreSQL configuration
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_HOST=<your_postgres_host>
POSTGRES_PORT=<your_postgres_port>
POSTGRES_DATABASE=<your_postgres_database>
```

### Example `.env` File

```plaintext
MYSQL_USER=myuser
MYSQL_PASSWORD=mypassword
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=mydatabase

SQL_SERVER=sqlserver.example.com
SQL_DATABASE=mydb
SQL_USERNAME=myuser
SQL_PASSWORD=mypassword

POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=mydatabase
```

## Usage

The `shared_utils` package provides functions to create SQLAlchemy engines for each supported database. Here’s how to use it to connect and run queries:

### Import and Create Database Engines

In your Python code, import the functions and create database engines as follows:

```python
from shared_utils.db_connection import create_mysql_engine, create_mssql_engine, create_postgres_engine
from sqlalchemy import text

# Create engines
mysql_engine = create_mysql_engine()
mssql_engine = create_mssql_engine()
postgres_engine = create_postgres_engine()
```

### Running a Sample Query

Here’s how to connect to each database and run a sample query to fetch the first 10 rows of a table:

```python
# Example query execution
with mysql_engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM your_mysql_table LIMIT 10"))
    for row in result:
        print(row)

with mssql_engine.connect() as conn:
    result = conn.execute(text("SELECT TOP 10 * FROM your_mssql_table"))
    for row in result:
        print(row)

with postgres_engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM your_postgres_table LIMIT 10"))
    for row in result:
        print(row)
```

Replace `your_mysql_table`, `your_mssql_table`, and `your_postgres_table` with the actual table names in your databases.

## Testing Connections

The `shared_utils` package includes a `test_shared_utils` command that runs a basic connection test for each database. This verifies that connections are set up correctly.

To run the test, use the following command in your terminal:

```bash
test_shared_utils
```

This command will:
- Attempt to connect to each database specified in the `.env` file.
- Run a simple `SELECT 1` query to confirm connectivity.
- Display the result for each database or an error message if there’s an issue.

Ensure your `.env` file is set up correctly with valid credentials before running the test.

## Dependencies

The `shared_utils` package relies on the following dependencies, which are installed automatically:

- `python-dotenv`: For loading environment variables from a `.env` file.
- `SQLAlchemy`: The main ORM and database toolkit used for managing database connections.
- `pyodbc`: Required for SQL Server (MSSQL) connections.
- `pymysql`: Required for MySQL connections.
- `psycopg2-binary`: Required for PostgreSQL connections.

## AI Assistant Prompt

If you need additional guidance on using `shared_utils`, here’s a sample prompt you can use with an AI assistant (e.g., ChatGPT):

**Prompt:**

*I have a Python package called `shared_utils` that I installed, which helps me connect to MySQL, SQL Server, and PostgreSQL databases using SQLAlchemy. The package uses environment variables stored in a `.env` file for database credentials. I want to set this up so I can connect to my databases and run queries easily. Here’s the information you’ll need:*

1. *The `.env` file format for storing credentials looks like this:*

    ```plaintext
    MYSQL_USER=<your_mysql_user>
    MYSQL_PASSWORD=<your_mysql_password>
    MYSQL_HOST=<your_mysql_host>
    MYSQL_PORT=<your_mysql_port>
    MYSQL_DATABASE=<your_mysql_database>

    SQL_SERVER=<your_sql_server_host>
    SQL_DATABASE=<your_sql_server_database>
    SQL_USERNAME=<your_sql_server_user>
    SQL_PASSWORD=<your_sql_server_password>

    POSTGRES_USER=<your_postgres_user>
    POSTGRES_PASSWORD=<your_postgres_password>
    POSTGRES_HOST=<your_postgres_host>
    POSTGRES_PORT=<your_postgres_port>
    POSTGRES_DATABASE=<your_postgres_database>
    ```

2. *The main functions in `shared_utils` are `create_mysql_engine`, `create_mssql_engine`, and `create_postgres_engine`, which create SQLAlchemy engines for each database.*

3. *Once the engines are created, I want to write a script that connects to each database and runs a sample query to fetch the first 10 rows of a table. Could you guide me through creating a script that does this, including any necessary setup with `shared_utils`?*

*Additionally, there’s a `test_shared_utils` command that I can run to verify if the connections work correctly. Can you show me how to use it after setting up my `.env` file?*

---
