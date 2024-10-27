from shared_utils.db_connection import create_mysql_engine, create_mssql_engine, create_postgres_engine
from sqlalchemy import text

def test_connections():
    engines = {
        "MySQL": create_mysql_engine(),
        "MSSQL": create_mssql_engine(),
        "PostgreSQL": create_postgres_engine(),
    }
    
    test_query = {
        "MySQL": "SELECT 1",
        "MSSQL": "SELECT 1",
        "PostgreSQL": "SELECT 1",
    }
    
    for db_name, engine in engines.items():
        try:
            with engine.connect() as conn:
                print(f"[INFO] Testing connection to {db_name}...")
                result = conn.execute(text(test_query[db_name]))
                for row in result:
                    print(f"[SUCCESS] {db_name} test query result:", row)
        except Exception as e:
            print(f"[ERROR] Failed to connect to {db_name}: {e}")

if __name__ == "__main__":
    test_connections()
