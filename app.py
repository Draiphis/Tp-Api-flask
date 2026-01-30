import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase




app = Flask(__name__)




# 🔹 Configuration SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'


db = SQLAlchemy(app)

# 🔹 Modèle HistoryEntry
class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    equipement = db.Column(db.Text, nullable=False)
    seats = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Room {self.name}>"


with app.app_context():
    db.create_all()

@app.route("/rooms", methods=["GET"])
def list_rooms():
    rooms = roomsEntry.query.all()
    clean_rooms = []
    for r in rooms:
       clean_rooms.append({
          "id": r.id,
          "name": r.name,
          "type": r.type,
          "floor": r.floor,
          "equipement": r.equipement,
          "seats": r.seats
       })

    return jsonify({
        "rooms": clean_rooms
    })

@app.route("/rooms", methods=["POST"])
def create_room():

    data = request.get_json()
    new_room = Room()
    new_room.name=data["name"],
    new_room.type=data["type"],
    new_room.floor=data["floor"],
    new_room.equipement=data["equipement"],
    new_room.seats=data["seats"]

    db.session.add(new_room)
    db.session.commit()

    return  jsonify({
        "id": new_room.id,
        "name": new_room.name,
        "type": new_room.type,
        "floor": new_room.floor,
        "equipement": new_room.equipement,
        "seats": new_room.seats
    })