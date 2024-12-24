from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import json
import eventlet
import random

# Setup Flask and SocketIO
app = Flask(__name__, static_folder="static", template_folder="templates")
socketio = SocketIO(app, cors_allowed_origins="*")

# Serve the main page
@app.route("/")
def index():
    return render_template("index.html")

# /live-data route to serve telemetry data
@app.route("/live-data", methods=['GET'])
def live_data():
    # Example live telemetry data
    telemetry_data = {
        "rotation": random.uniform(0, 360),  # Rotation in degrees
        "position": {
            "x": random.uniform(-5, 5),
            "y": random.uniform(-5, 5),
            "z": random.uniform(-5, 5)
        },
        "force": {
            "x": random.uniform(0, 10),
            "y": random.uniform(0, 10),
            "z": random.uniform(0, 10)
        }
    }
    return jsonify(telemetry_data)

# Emit live data periodically for testing (optional)
def generate_live_data():
    while True:
        # This is an extra, but could simulate real-time data
        telemetry_data = {
            "rotation": random.uniform(0, 360),  # Rotation in degrees
            "position": {
                "x": random.uniform(-5, 5),
                "y": random.uniform(-5, 5),
                "z": random.uniform(-5, 5)
            }
        }
        socketio.emit("update_telemetry", json.dumps(telemetry_data))
        eventlet.sleep(1)  # Update every second

@socketio.on("connect")
def handle_connect():
    print("Client connected!")

if __name__ == "__main__":
    socketio.start_background_task(generate_live_data)
    socketio.run(app, host="0.0.0.0", port=5000)













