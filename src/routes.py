from app import app
from flask import render_template, redirect, request
from src.services.drone_service import drone_service

@app.route("/")
def index():
    violators = drone_service.get_drones()
    return render_template("index.html", violators=violators)
