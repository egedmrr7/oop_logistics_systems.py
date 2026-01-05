from flask import Flask, render_template, request, redirect
from database import init_db, get_db_connection  # get_db_connection'ı buradan alıyoruz
from models import Package
from services import (
    add_package,
    get_all_packages,
    generate_report,
    update_package_status,
    add_hub,
    get_all_hubs
)

app = Flask(__name__)
init_db()

# --------------------
# ANA SAYFA - LİSTELEME VE SIRALAMA
# --------------------
@app.route("/")
def index():
    packages = get_all_packages()
    
    # Paketleri Önem Derecesine göre Büyükten Küçüğe sıralıyoruz
    if packages:
        # Prio değerinin sayısal olduğundan emin olup sıralıyoruz
        packages.sort(key=lambda x: int(x.priority) if str(x.priority).isdigit() else 0, reverse=True)
    
    groups = {}
    for p in packages:
        groups.setdefault(p.destination, []).append(p.package_id)
    
    return render_template("packages.html", packages=packages, groups=groups)

# --------------------
# PAKET EKLEME
# --------------------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        p_id = request.form.get("package_id")
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        priority_val = request.form.get("priority")
        weight = request.form.get("weight")
        volume = request.form.get("volume")

        if p_id:
            prio = int(priority_val) if priority_val and priority_val.isdigit() else 0
            pkg = Package(p_id, origin, destination, prio, weight, volume)
            add_package(pkg)
            return redirect("/")

    return render_template("add_package.html")

# --------------------
# SİLME İŞLEMİ (Düzeltildi)
# --------------------
@app.route("/delete/<p_id>")
def delete_item(p_id):
    # Hata almamak için bağlantıyı güvenli şekilde kuruyoruz
    conn = get_db_connection()
    try:
        # Veritabanında sütun adının package_id olduğundan emin oluyoruz
        conn.execute("DELETE FROM packages WHERE package_id = ?", (p_id,))
        conn.commit()
    finally:
        conn.close()
    return redirect("/")

# --------------------
# DİĞER ROTALAR
# --------------------
@app.route("/report")
def report():
    total, delivered, ratio = generate_report()
    return render_template("report.html", total=total, delivered=delivered, ratio=ratio)

@app.route("/deliver/<package_id>")
def mark_delivered(package_id):
    update_package_status(package_id, "Delivered")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
