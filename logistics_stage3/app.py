from flask import Flask, render_template, request, redirect
from database import init_db
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
# HOME - PACKAGE LIST
# --------------------
@app.route("/")
def index():
    packages = get_all_packages()
    return render_template("packages.html", packages=packages)


# --------------------
# ADD PACKAGE
# --------------------
@app.route("/add", methods=["GET", "POST"])
def add():
    hubs = get_all_hubs()

    if request.method == "POST":
        p_id = request.form.get("package_id")
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        priority_val = request.form.get("priority")

        if p_id:
            prio = int(priority_val) if priority_val and priority_val.isdigit() else 0
            pkg = Package(p_id, origin, destination, prio)
            add_package(pkg)
            return redirect("/")

    return render_template("add_package.html", hubs=hubs)


# --------------------
# ADD HUB
# --------------------
@app.route("/add-hub", methods=["GET", "POST"])
def add_hub_page():
    if request.method == "POST":
        hub_id = request.form.get("hub_id")
        name = request.form.get("name")

        if hub_id and name:
            add_hub(hub_id, name)
            return redirect("/add-hub")

    hubs = get_all_hubs()
    return render_template("add_hub.html", hubs=hubs)


# --------------------
# REPORT
# --------------------
@app.route("/report")
def report():
    total, delivered, ratio = generate_report()
    return render_template(
        "report.html",
        total=total,
        delivered=delivered,
        ratio=ratio
    )


# --------------------
# DELIVER PACKAGE
# --------------------
@app.route("/deliver/<package_id>")
def mark_delivered(package_id):
    update_package_status(package_id, "Delivered")
    return redirect("/")


# --------------------
# GROUPED PACKAGES
# --------------------
@app.route("/groups")
def grouped_packages():
    packages = get_all_packages()
    groups = {}

    for p in packages:
        groups.setdefault(p.destination, []).append(p.package_id)

    return render_template("groups.html", groups=groups)
@app.route("/delete/<p_id>")
def delete_item(p_id):
    from database import get_db_connection
    conn = get_db_connection()
    conn.execute("DELETE FROM packages WHERE package_id = ?", (p_id,))
    conn.commit()
    conn.close()
    return redirect("/")

# --------------------
# RUN
# --------------------
if __name__ == "__main__":
    app.run(debug=True)


