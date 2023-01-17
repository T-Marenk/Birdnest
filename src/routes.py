from app import app
from flask import render_template, redirect, request, jsonify
from src.services.drone_service import drone_service

@app.route("/")
def index():
    violators = drone_service.update_violators()
    return render_template("index.html", violators=violators)

@app.route("/update", methods=['POST'])
def update():
     
    violators = drone_service.update_violators()
    return render_template("section.html", violators=violators)
