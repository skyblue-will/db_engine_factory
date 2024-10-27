# shared_utils

**Version**: 0.2.4  
**Author**: Will Palmer  
**Description**: `shared_utils` is a Python library that simplifies the connection to multiple database types (MySQL, MSSQL, PostgreSQL) using SQLAlchemy and a centralized configuration file. This library is especially useful for projects needing consistent and maintainable database connections across various environments.

---

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Creating Database Engines](#creating-database-engines)
  - [Testing Connections](#testing-connections)
- [Example AI Prompt for Assistance](#example-ai-prompt-for-assistance)
- [Running Tests](#running-tests)
- [Contributing](#contributing)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/willpalmer81/shared_utils.git
   cd shared_utils
   ```

2. **Install the package**:
   ```bash
   pip install .
   ```

   This will also install the required dependencies, including:
   - `python-dotenv`
   - `SQLAlchemy>=2.0`
   - `pyodbc`
   - `pymysql`
   - `psycopg2-binary`

3. **Add a configuration file**: Place your `.ini` configuration file (e.g., `db_config.ini`) in the root directory of your project or specify its path when initializing connections.

## Configuration

Create a `.ini` configuration file (e.g., `db_config.ini`) in the root directory. Each section in this file should represent a different database connection. The parameters required depend on the database type (MySQL, MSSQL, or PostgreSQL).

### Example `.ini` File

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

### Explanation of Fields

- **type**: Type of the database, such as `mysql`, `mssql`, or `postgres`.
- **user / username**: Username for the database.
- **password**: Password for the database.
- **host / server**: Network address of the database server.
- **port**: Port number for the database (default is 3306 for MySQL and 5432 for PostgreSQL).
- **database**: Name of the database to connect to.

## Usage

### Creating Database Engines

You can create a database engine for each configured database type by calling the relevant functions in `db_connection.py`, passing in the database identifier (e.g., `"mysql_db"`). These identifiers should match the section names in the `.ini` file.

Example:

```python
from shared_utils.db_connection import create_mysql_engine, create_mssql_engine, create_postgres_engine

# Create engines
mysql_engine = create_mysql_engine("mysql_db")
mssql_engine = create_mssql_engine("mssql_db")
postgres_engine = create_postgres_engine("postgres_db")
```

### Function Parameters

- `create_mysql_engine(db_identifier)`, `create_mssql_engine(db_identifier)`, and `create_postgres_engine(db_identifier)` each take a single parameter:
  - **db_identifier**: The name of the database section in the `.ini` file to load the configuration from.

### Testing Connections

To test database connections as defined in the `.ini` file, you can use the `test_shared_utils` command, which runs a basic `SELECT 1` query on each database:

```bash
test_shared_utils
```

This command outputs the connection status for each database, including any errors encountered.

## Example AI Prompt for Assistance

For using AI assistance (such as ChatGPT) to troubleshoot or get help, consider the following prompt:

> "I am using the `shared_utils` package to connect to multiple databases. Each database is configured in an `.ini` file under sections like `[mysql_db]`, `[mssql_db]`, and `[postgres_db]`. The functions `create_mysql_engine(db_identifier)`, `create_mssql_engine(db_identifier)`, and `create_postgres_engine(db_identifier)` each take a `db_identifier` that matches these section names. Could you help troubleshoot if any connections fail or if query results aren’t as expected?"

This prompt provides essential context about your setup, making it easier for the AI assistant to offer precise advice.

## Running Tests

The `shared_utils` package includes a `test.py` script to verify database connections based on configurations provided in the `.ini` file.

To run the test script:

1. Ensure that the `.ini` file is correctly configured.
2. Run the `test_shared_utils` command:
   ```bash
   test_shared_utils
   ```

This will attempt a connection to each database and execute a simple query (`SELECT 1`). Success and error messages will be displayed based on the connection results.

---

For any issues or feature requests, please [open an issue on GitHub](https://github.com/willpalmer81/shared_utils/issues).
