import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

def create_mssql_engine():
    """
    Creates a SQL Server engine using SQLAlchemy with pyodbc.
    """
    # Retrieve SQL Server credentials from environment variables
    server = os.getenv('SQL_SERVER')
    database = os.getenv('SQL_DATABASE')
    username = os.getenv('SQL_USERNAME')
    password = os.getenv('SQL_PASSWORD')

    # Check that all credentials are provided
    if not all([server, database, username, password]):
        raise ValueError("Missing SQL Server credentials in environment variables.")

    # Construct the connection string with ODBC Driver 17 for SQL Server
    conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    
    # Create engine with additional parameters for improved stability and performance
    return create_engine(conn_str, fast_executemany=True, pool_pre_ping=True)

def create_mysql_engine():
    """
    Creates a MySQL engine using SQLAlchemy.
    """
    mysql_user = os.getenv('MYSQL_USER')
    mysql_password = os.getenv('MYSQL_PASSWORD')
    mysql_host = os.getenv('MYSQL_HOST', 'localhost')
    mysql_port = os.getenv('MYSQL_PORT', '3306')
    mysql_db = os.getenv('MYSQL_DATABASE')

    if not all([mysql_user, mysql_password, mysql_db]):
        raise ValueError("Missing MySQL credentials in environment variables.")

    conn_str = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
    return create_engine(conn_str)

def create_postgres_engine():
    """
    Creates a PostgreSQL engine using SQLAlchemy.
    """
    pg_user = os.getenv('POSTGRES_USER')
    pg_password = os.getenv('POSTGRES_PASSWORD')
    pg_host = os.getenv('POSTGRES_HOST', 'localhost')
    pg_port = os.getenv('POSTGRES_PORT', '5432')
    pg_db = os.getenv('POSTGRES_DATABASE')

    if not all([pg_user, pg_password, pg_db]):
        raise ValueError("Missing PostgreSQL credentials in environment variables.")

    conn_str = f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"
    return create_engine(conn_str)

def execute_query(engine, query, params=None):
    """
    Executes a SQL query using the provided engine.

    Args:
        engine: SQLAlchemy engine instance.
        query (str): The SQL query to execute.
        params (dict, optional): Parameters for parameterized queries.

    Returns:
        ResultProxy: The result of the executed query.
    """
    with engine.connect() as connection:
        result = connection.execute(text(query), params or {})
        return result
