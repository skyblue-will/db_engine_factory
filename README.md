# DB Engine Factory

**Version**: 0.1.5  
**Author**: Will Palmer  
**Description**: `DB Engine Factory` is a Python library designed to simplify connecting to multiple database types (MySQL, MSSQL, PostgreSQL) using SQLAlchemy. Connections are configured via a central `.ini` file, streamlining database management for applications needing to work with diverse database systems.

---

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Creating Database Engines](#creating-database-engines)
  - [Testing Connections](#testing-connections)
- [AI Assistance Prompt](#ai-assistance-prompt)
- [Running Tests](#running-tests)
- [Contributing](#contributing)

---

## Installation

1. **Install the package from PyPI**:
   ```bash
   pip install db-engine-factory
   ```

2. **Create a configuration file**: Ensure your `.ini` configuration file (e.g., `db_config.ini`) is in the project root or the directory where you run scripts.

## Configuration

### Setting Up Your `.ini` Configuration File

Create a `.ini` file (e.g., `db_config.ini`) in the project’s root directory. Each section represents a database configuration.

#### Example `db_config.ini`

```ini
# MySQL Database
[mysql_db]
type = mysql
user = myuser
password = mypassword
host = localhost
port = 3306
database = mydatabase

# MSSQL Database
[mssql_db]
type = mssql
server = sqlserver.example.com
database = mydatabase
username = myuser
password = mypassword

# PostgreSQL Database
[postgres_db]
type = postgres
user = myuser
password = mypassword
host = localhost
port = 5432
database = mydatabase
```

**Explanation of Fields**

- **type**: Database type (`mysql`, `mssql`, or `postgres`).
- **user/username**: Database username.
- **password**: Database password.
- **host/server**: Database server address.
- **port**: Database port (`3306` for MySQL, `5432` for PostgreSQL).
- **database**: Name of the database.

## Usage

### Creating Database Engines

Use the functions in `db_connection.py` to create database engines. Each function accepts a `db_identifier` matching a section in `db_config.ini`.

```python
from db_engine_factory.db_connection import create_mysql_engine, create_mssql_engine, create_postgres_engine

# Create a MySQL engine
mysql_engine = create_mysql_engine("mysql_db")

# Create an MSSQL engine
mssql_engine = create_mssql_engine("mssql_db")

# Create a PostgreSQL engine
postgres_engine = create_postgres_engine("postgres_db")
```

### Function Parameters

- **create_mysql_engine(db_identifier)**: Creates a MySQL engine based on the `.ini` configuration.
- **create_mssql_engine(db_identifier)**: Creates an MSSQL engine using the specified `.ini` section.
- **create_postgres_engine(db_identifier)**: Creates a PostgreSQL engine per `.ini` configuration.

### Testing Connections

Run `test_db_engine_factory` from the command line to test connections to all configured databases with a simple `SELECT 1` query.

```bash
test_db_engine_factory
```

This outputs success or error messages for each database connection attempt, confirming if `.ini` configurations are correct.

## AI Assistance Prompt

If you need help from an AI assistant, use this example prompt:

> "I'm using `DB Engine Factory` to connect to MySQL, MSSQL, and PostgreSQL databases, configured in a `.ini` file under sections like `[mysql_db]`, `[mssql_db]`, and `[postgres_db]`. I use functions like `create_mysql_engine(db_identifier)`, `create_mssql_engine(db_identifier)`, and `create_postgres_engine(db_identifier)`. Could you help troubleshoot any connection issues or verify query results?"

## Running Tests

The package includes a test script for verifying database connections defined in the `.ini` file.

1. Confirm `.ini` file is correctly configured.
2. Run the test command:
   ```bash
   test_db_engine_factory
   ```

This script connects to each database and runs a `SELECT 1` query, displaying connection results in the console.

## Contributing

To contribute:

1. **Fork** the repository.
2. **Create a branch** (`git checkout -b feature/YourFeature`).
3. **Commit your changes** (`git commit -m 'Add a new feature'`).
4. **Push to the branch** (`git push origin feature/YourFeature`).
5. **Open a pull request**.

If you encounter issues or have suggestions, please [open an issue on GitHub](https://github.com/skyblue-will/db_engine_factory/issues).

--- 
