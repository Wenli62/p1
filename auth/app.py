from flask import Flask, request, render_template, jsonify
import jwt
from datetime import datetime, timedelta
import yaml

def load_yaml(file, default={}):
    try:
        with open(file, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return default

app_config = load_yaml('app_conf.yml')
SECRET_KEY = app_config["secret_key"]


app = Flask(__name__)

users = app_config["users_db"]


def create_jwt(username: str):
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def validate_token(token: str):
    if not token:
        return {"error": "Missing token"}, 422
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload, 200
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}, 401
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}, 401

@app.route("/", methods=["GET"])
def serve_login_page():
    return render_template("login.html")


@app.route("/dashboard", methods=["GET"])
def serve_dashboard_page():

    token = request.args.get("token")
    if not token:
        return "Missing token", 400
    
    decoded_token, status_code = validate_token(token)
    if status_code == 200:
        return render_template("dashboard.html", username=decoded_token["username"])
    else:
        return jsonify(decoded_token), status_code

@app.route("/", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        token = create_jwt(username)
        return jsonify({"access_token": token})
    else:
        return jsonify({"detail": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
