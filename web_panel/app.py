from flask import Flask, render_template, request, redirect
from db.database import groups, stats
from config import ADMIN_USERNAME, ADMIN_PASSWORD
import threading

app = Flask(__name__)

def start_web():
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=5000), daemon=True).start()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["user"] == ADMIN_USERNAME and request.form["pass"] == ADMIN_PASSWORD:
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    total_groups = 0
    total_joins = 0

    async def get_data():
        nonlocal total_groups, total_joins
        async for g in groups.find():
            total_groups += 1
        async for s in stats.find():
            total_joins += s.get("joins", 0)

    import asyncio
    asyncio.run(get_data())

    return render_template("dashboard.html", groups=total_groups, joins=total_joins)
