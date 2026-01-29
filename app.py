from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/rooms", method=["GET"])
def list_rooms():
    return jsonify({
        "id":1234,
        "name": "Salle 204"
        "type": "Classroom",
        "floor":2,
        "equipement":["whiteboard"],
        "seats":30
    })