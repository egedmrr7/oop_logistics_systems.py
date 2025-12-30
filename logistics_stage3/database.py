import sqlite3

DB_NAME = "logistics.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS packages (
        id TEXT PRIMARY KEY,
        origin TEXT,
        destination TEXT,
        priority INTEGER,
        status TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()
