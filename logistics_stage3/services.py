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
    insert_package(pkg)


def get_all_packages():
    rows = fetch_all_packages()
    packages = []

    for r in rows:
        packages.append(
            Package(
                package_id=r[0],
                origin=r[1],
                destination=r[2],
                priority=r[3],
                status=r[4]
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
