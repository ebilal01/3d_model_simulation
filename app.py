import json
import eventlet
import random
from flask import Flask, render_template
from flask_socketio import SocketIO

# Setup Flask and SocketIO
app = Flask(__name__, static_folder="static", template_folder="templates")
socketio = SocketIO(app, cors_allowed_origins="*")

# Serve the main page
@app.route("/")
def index():
    return render_template("index.html")

# Emit live data periodically
def generate_live_data():
    while True:
        # Example live telemetry data
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














