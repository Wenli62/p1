import connexion
from flask import request, jsonify
import jwt
import datetime
import os

# Secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

# Dummy user database (replace with real DB lookup)
USER_CREDENTIALS = {
    "admin": "password123",
    "user1": "securepass"
}

# Set up the Connexion app
app = connexion.FlaskApp(__name__, specification_dir='')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Validate credentials
    if USER_CREDENTIALS.get(username) == password:
        token = jwt.encode(
            {"username": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify({"token": token}), 200

    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/validate', methods=['POST'])
def validate_token():
    data = request.get_json()
    token = data.get("token")

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"valid": True, "username": decoded["username"]}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"valid": False, "message": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"valid": False, "message": "Invalid token"}), 401

if __name__ == "__main__":
    app.run(port=5020)
