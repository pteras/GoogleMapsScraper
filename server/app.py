from flask import Flask, request, jsonify, session
from models import db, User
from flask_bcrypt import Bcrypt
from scraper import get_data
from flask_cors import CORS
from config import ApplicationConfig
from flask_session import Session
import json

app = Flask(__name__)
app.config.from_object(ApplicationConfig)

server_session = Session(app)
CORS().init_app(app, supports_credentials=True)
bcrypt = Bcrypt(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/api/scraper", methods=["POST"])
def fetch_data():
    form_data = request.get_json()
    address = form_data["address"]
    business_type = form_data["businessType"]
    radius = form_data["radius"]    
    data = get_data(address, business_type, radius)
    return json.dumps({"success": True, "data": data}), 200, {"ContentType": "application/json"}

@app.route("/register", methods=["POST"])
def register_user():
    username = request.json["username"]
    password = request.json["password"]

    user_exists = User.query.filter_by(username=username).first() is not None

    if user_exists:
        return jsonify({"error": "User already exists"}), 409
    
    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id, 
        "username": new_user.username
    })


@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "username": user.username
    })

@app.route("/login", methods=["POST"])
def login_user():
    username = request.json["username"]
    password = request.json["password"]

    user = User.query.filter_by(username=username).first()

    if user is None:
        return jsonify({"error": "Unauthorized"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401

    session["user_id"] = user.id
    
    return jsonify({
        "id": user.id,
        "username": user.username
    })

if __name__ == "__main__":
    #! remove debug=True in production
    app.run(debug=True)


    
    