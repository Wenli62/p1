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
option_a = os.getenv('OPTION_A', "Cats")
option_b = os.getenv('OPTION_B', "Dogs")
hostname = socket.gethostname()

@app.route("/vote", methods=["GET", "POST"])
def vote():
    if request.method == "GET":
        return render_template('index.html', option_a=option_a, option_b=option_b, hostname=hostname)

    data = request.get_json() or {}
    if 'user_input' not in data:
        return jsonify({"message": "Invalid request data"}), 400
    
    data.update({"id": str(random.randint(1000, 9999)), "vote_time": datetime.now(timezone.utc).isoformat()})
    logger.info(f"Vote received: {json.dumps(data, indent=2)}")

    # Send vote to external service if URL exists
    vote_url = app_config.get('vote', {}).get('url')
    try:
        httpx.post(vote_url, json=data, headers={"Content-Type": "application/json"}).raise_for_status()
    except Exception as e:
        logger.error(f"Error forwarding vote: {str(e)}")
        return jsonify({"message": "Internal Server Error"}), 500

    return jsonify({"message": "Vote recorded successfully"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
