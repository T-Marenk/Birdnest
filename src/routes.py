from src.config import APP_FILE_PATH
from app import app
from flask import render_template, redirect, request

@app.route("/")
def index():
    return render_template("index.html")
