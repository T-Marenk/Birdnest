from threading import Timer
from flask import render_template, redirect, request, jsonify
from app import app
from src.services.drone_service import drone_service

def updater(interval):
    Timer(interval, updater, [interval]).start()
    drone_service._update_violators()

updater(1)

@app.route("/")
def index():
    violators = drone_service.get_violators()
    return render_template("index.html", violators=violators)

@app.route("/update", methods=['POST'])
def update():
     
    violators = drone_service.get_violators()
    return render_template("section.html", violators=violators)
