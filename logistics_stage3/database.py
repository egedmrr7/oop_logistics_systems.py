import sqlite3
from datetime import datetime

DB_NAME = "logistics.db"


# --------------------
# CONNECTION
# --------------------
def get_connection():
    return sqlite3.connect(DB_NAME)


# --------------------
# INITIALIZATION
# --------------------
def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Packages table
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

    # Hubs table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS hubs (
        id TEXT PRIMARY KEY,
        name TEXT
    )
    """)

    # Hub distances (for routing / Dijkstra)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS hub_distances (
        from_hub TEXT,
        to_hub TEXT,
        distance INTEGER,
        PRIMARY KEY (from_hub, to_hub)
    )
    """)

    conn.commit()
    conn.close()


# --------------------
# PACKAGE OPERATIONS
# --------------------
def insert_package(package):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO packages (id, origin, destination, priority, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        package.package_id,
        package.origin,
        package.destination,
        package.priority,
        package.status,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def fetch_all_packages():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, origin, destination, priority, status
        FROM packages
        ORDER BY priority DESC
    """)

    rows = cur.fetchall()
    conn.close()
    return rows


def update_package_status(package_id, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE packages
        SET status = ?
        WHERE id = ?
    """, (status, package_id))

    conn.commit()
    conn.close()


# --------------------
# HUB OPERATIONS
# --------------------
def insert_hub(hub_id, name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO hubs (id, name)
        VALUES (?, ?)
    """, (hub_id, name))

    conn.commit()
    conn.close()


def fetch_all_hubs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM hubs")
    rows = cur.fetchall()

    conn.close()
    return rows


# --------------------
# HUB DISTANCE OPERATIONS
# --------------------
def insert_hub_distance(from_hub, to_hub, distance):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT OR REPLACE INTO hub_distances (from_hub, to_hub, distance)
        VALUES (?, ?, ?)
    """, (from_hub, to_hub, distance))

    conn.commit()
    conn.close()


def fetch_hub_distances():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT from_hub, to_hub, distance
        FROM hub_distances
    """)

    rows = cur.fetchall()
    conn.close()
    return rows
