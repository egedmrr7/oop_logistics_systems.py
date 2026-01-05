import sqlite3

def get_db_connection():
    """Veritabanına bağlantı oluşturur."""
    conn = sqlite3.connect('logistics.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Tabloyu eksiksiz sütunlarla oluşturur."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS packages (
            package_id TEXT PRIMARY KEY,
            origin TEXT,
            destination TEXT,
            priority INTEGER,
            weight TEXT,
            volume TEXT,
            status TEXT DEFAULT 'Beklemede'
        )
    ''')
    conn.commit()
    conn.close()

def insert_package(pkg):
    """Yeni bir paketi veritabanına kaydeder."""
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO packages (package_id, origin, destination, priority, weight, volume) VALUES (?, ?, ?, ?, ?, ?)",
        (pkg.package_id, pkg.origin, pkg.destination, pkg.priority, pkg.weight, pkg.volume)
    )
    conn.commit()
    conn.close()

def fetch_all_packages():
    """Tüm paketleri liste olarak döner (services.py için)."""
    conn = get_db_connection()
    # Verileri liste (tuple) formatında alıyoruz
    rows = conn.execute("SELECT package_id, origin, destination, priority, weight, volume, status FROM packages").fetchall()
    conn.close()
    return rows

def update_package_status(package_id, status):
    """Paket durumunu günceller."""
    conn = get_db_connection()
    conn.execute("UPDATE packages SET status = ? WHERE package_id = ?", (status, package_id))
    conn.commit()
    conn.close()

def fetch_all_hubs():
    """Eğer hub tablon varsa onları çeker (Hata almamak için boş dönebilir)."""
    conn = get_db_connection()
    # Hub tablon henüz yoksa hata vermemesi için kontrol ekleyebilirsin
    try:
        rows = conn.execute("SELECT * FROM hubs").fetchall()
    except:
        rows = []
    conn.close()
    return rows

def insert_hub(hub_id, name):
    """Yeni hub ekler."""
    conn = get_db_connection()
    conn.execute("CREATE TABLE IF NOT EXISTS hubs (id TEXT PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO hubs (id, name) VALUES (?, ?)", (hub_id, name))
    conn.commit()
    conn.close()
