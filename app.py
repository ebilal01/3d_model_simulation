import os
import time
import random
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
import serial
from rockblock import RockBlock

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Use eventlet with Flask-SocketIO
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live-data', methods=['GET'])
def live_data():
    # Simulate real-time 3D data
    data = {
        "x_rotation": random.uniform(-90.0, 90.0),
        "y_rotation": random.uniform(-180.0, 180.0),
        "z_rotation": random.uniform(-10.0, 10.0),
    }
    # Emit live data for 3D animation
    socketio.emit('update_3d_model', data)

    # Send data via RockBlock (example usage)
    rockblock_message = f"Rotation: X={data['x_rotation']}, Y={data['y_rotation']}, Z={data['z_rotation']}"
    send_rockblock_message(rockblock_message)

    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Bind to PORT from environment variable
    socketio.run(app, host='0.0.0.0', port=port)










