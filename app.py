from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

# Background task to send simulated force data
def background_force_data():
    while True:
        # Simulating live data
        force_vector = {
            "fx": random.uniform(-10, 10),  # Random x-force
            "fy": random.uniform(-10, 10),  # Random y-force
            "fz": random.uniform(-10, 10),  # Random z-force
        }
        socketio.emit("force_data", force_vector)  # Send force data to all clients
        time.sleep(1)  # Simulate data update every second

@socketio.on("connect")
def on_connect():
    print("Client connected")

if __name__ == "__main__":
    socketio.start_background_task(background_force_data)  # Start the background task
    socketio.run(app, debug=True)

