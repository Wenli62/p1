from flask import Flask, render_template, request, jsonify
import random
import json
import httpx
import os
import socket
import logging.config
import yaml
from datetime import datetime, timezone

# Load configuration safely
def load_yaml(file, default={}):
    try:
        with open(file, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return default

app_config = load_yaml('app_conf.yml')
log_config = load_yaml('log_conf.yml')

# Configure logging
if log_config:
    logging.config.dictConfig(log_config)
logger = logging.getLogger('basicLogger')

# Flask app setup
app = Flask(__name__)

# Environment variables (default: Cats vs. Dogs)
# option_a = os.getenv('OPTION_A', "Cats")
# option_b = os.getenv('OPTION_B', "Dogs")
#hostname = socket.gethostname()

@app.route("/submit_grade", methods=["GET", "POST"])
def submit_grade():
    if request.method == "GET":
        return render_template('index.html')

    data = request.get_json()
    required_fields = ['student_id', 'subject', 'grade']
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"{field} is required"}), 400

    data["receive_time"] = datetime.now(timezone.utc).isoformat()
    logger.info(f"Grade received on {data['receive_time']}")

    url = app_config['submit_grade']['url']
    headers = {"Content-Type": "application/json"}
    
    try:
        httpx.post(url, json=data, headers=headers).raise_for_status()
    except Exception as e:
        logger.error(f"Error forwarding grade: {str(e)}")
        return jsonify({"message": "Internal Server Error"}), 500

    return jsonify({"message": "Grade recorded successfully"}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
