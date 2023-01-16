from app import app
from flask import render_template, redirect, request
from src.services.drone_service import DroneService

@app.route("/")
def index():
    s = DroneService()
    s.get_drones()
    return render_template("index.html")
