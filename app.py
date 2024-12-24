from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    # Renders the HTML page with the 3D model viewer
    return render_template('index.html')

@app.route('/rockblock', methods=['POST'])
def handle_rockblock():
    # Parse RockBlock webhook data
    data = request.json
    imei = data.get('imei', 'Unknown')
    force_x = random.uniform(-5, 5)  # Simulated force values
    force_y = random.uniform(-5, 5)
    force_z = random.uniform(-5, 5)

    # Emit the force data to all connected clients
    socketio.emit('force_data', {'forceX': force_x, 'forceY': force_y, 'forceZ': force_z})
    return "Data received"

def simulate_forces():
    # Continuously simulate and send random forces
    while True:
        force_x = random.uniform(-5, 5)
        force_y = random.uniform(-5, 5)
        force_z = random.uniform(-5, 5)
        socketio.emit('force_data', {'forceX': force_x, 'forceY': force_y, 'forceZ': force_z})
        time.sleep(2)  # Update forces every 2 seconds

# Start a background thread for force simulation
thread = threading.Thread(target=simulate_forces, daemon=True)
thread.start()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)





