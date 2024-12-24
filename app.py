from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def on_connect():
    print("Client connected")

@socketio.on("request_force_data")
def send_force_data():
    while True:
        # Simulating live data
        force_vector = {
            "fx": random.uniform(-10, 10),  # Random x-force
            "fy": random.uniform(-10, 10),  # Random y-force
            "fz": random.uniform(-10, 10),  # Random z-force
        }
        emit("force_data", force_vector)  # Send force data to client
        time.sleep(1)  # Simulate data update every second

if __name__ == "__main__":
    socketio.run(app, debug=True)
