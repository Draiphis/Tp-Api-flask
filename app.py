from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/rooms", methods=["GET"])
def list_rooms():
    return jsonify({
        "rooms":[{
        "id":1234,
        "name": "Salle 204",
        "type": "Classroom",
        "floor": 2,
        "equipement":["whiteboard"],
        "seats":30}]
    })