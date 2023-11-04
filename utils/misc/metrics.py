import psycopg2

QUERIES = []
def add_banned_queries(q):
    QUERIES.append(q)

def get_banned_queries():
    return QUERIES

def get_metrics(dbname: str, user: str, password: str):
    # Connect to your postgres DB
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM pg_stat_activity")

    # Retrieve query results
    records = cur.fetchall()
    return records

def get_queries(dbname: str, user: str, password: str):
    # Connect to your postgres DB
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT query FROM pg_stat_activity")

    # Retrieve query results
    records = cur.fetchall()
    print(records)
    return records