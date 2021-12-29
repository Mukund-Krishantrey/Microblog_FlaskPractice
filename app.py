from datetime import datetime
import re
from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.microblog
    entries_list = []

    @app.route("/", methods = ["GET", "POST"])
    def hello():
        cur_date = datetime.datetime.now()
        if request.method == "POST":
            entry_content = request.form.get("log_entry")
            today = cur_date.strftime("%b %d")
            app.db.entries.insert_one({"content":entry_content, "date":today})
        entries_list = [(entry["content"], entry["date"]) for entry in app.db.entries.find({})]
        return render_template("html_prac.html", entries_list = entries_list)
    return app

    