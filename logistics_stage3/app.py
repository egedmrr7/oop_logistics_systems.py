from flask import Flask, render_template, request, redirect
from database import init_db
from models import Package
from services import add_package, get_all_packages, generate_report

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    packages = get_all_packages()
    return render_template("index.html", packages=packages)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        pkg = Package(
            request.form["id"],
            request.form["origin"],
            request.form["destination"],
            int(request.form["priority"])
        )
        add_package(pkg)
        return redirect("/")
    return render_template("add_package.html")

@app.route("/report")
def report():
    total, delivered, ratio = generate_report()
    return render_template("report.html",
                           total=total,
                           delivered=delivered,
                           ratio=ratio)

if __name__ == "__main__":
    app.run(debug=True)
