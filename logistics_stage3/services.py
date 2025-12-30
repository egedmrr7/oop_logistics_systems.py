from database import get_connection
from datetime import datetime
from models import Package

def add_package(pkg: Package):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO packages VALUES (?, ?, ?, ?, ?, ?)",
        (pkg.id, pkg.origin, pkg.destination, pkg.priority,
         pkg.status, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def get_all_packages():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM packages")
    rows = cur.fetchall()
    conn.close()
    return rows


def generate_report():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM packages")
    total = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM packages WHERE status='DELIVERED'")
    delivered = cur.fetchone()[0]

    conn.close()

    success_ratio = (delivered / total) * 100 if total > 0 else 0
    return total, delivered, success_ratio
