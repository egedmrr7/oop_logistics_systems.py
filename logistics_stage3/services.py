from models import Package, Hub
from database import (
    insert_package,
    fetch_all_packages,
    update_package_status as db_update_package_status,
    insert_hub,
    fetch_all_hubs
)

# --------------------
# PACKAGE SERVICES
# --------------------

def add_package(pkg: Package):
    """Veritabanına paket nesnesini kaydeder."""
    insert_package(pkg)

def get_all_packages():
    """
    Veritabanındaki tüm paketleri çeker ve Package nesnesine dönüştürür.
    Sütun sıralaması database.py'deki tablo yapısına göre:
    r[0]: id, r[1]: origin, r[2]: destination, r[3]: priority, 
    r[4]: weight, r[5]: volume, r[6]: status
    """
    rows = fetch_all_packages()
    packages = []

    for r in rows:
        # Hata almamak için sütun sayısını kontrol ediyoruz
        packages.append(
            Package(
                package_id=r[0],
                origin=r[1],
                destination=r[2],
                priority=r[3],
                weight=r[4],  # YENİ: Ağırlık (Kg)
                volume=r[5],  # YENİ: Boyut (Hacim)
                status=r[6]   # Durum
            )
        )
    return packages

def update_package_status(package_id, status):
    db_update_package_status(package_id, status)

def generate_report():
    packages = get_all_packages()
    total = len(packages)
    delivered = len([p for p in packages if p.status == "Delivered"])
    ratio = (delivered / total) * 100 if total > 0 else 0
    return total, delivered, round(ratio, 2)

# --------------------
# HUB SERVICES
# --------------------

def add_hub(hub_id, name):
    insert_hub(hub_id, name)

def get_all_hubs():
    rows = fetch_all_hubs()
    return [Hub(r[0], r[1]) for r in rows]
