import time
import random
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Simulated storage for flight data
flight_data = []

def save_flight_data(data):
    # Append to flight data for simulation
    flight_data.append(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rockblock/MT', methods=['POST'])
def receive_mt():
    imei = request.args.get('imei')
    username = request.args.get('username')
    password = request.args.get('password')
    data = request.args.get('data')

    # Validate input (simulate simple validation for testing)
    if imei != "300434065264590" or username != "myUser" or password != "myPass":
        return "FAILED,10,Invalid login credentials", 400

    if not data:
        return "FAILED,16,No data", 400

    # Simulate decoding hex data
    try:
        decoded_message = bytes.fromhex(data).decode('utf-8')
    except ValueError:
        return "FAILED,14,Could not decode hex data", 400

    print(f"Received message: {decoded_message}")

    return "OK,4114651"

@app.route('/live-data', methods=['GET'])
def live_data():
    # Simulate flight data with random values for testing
    data = {
        "x_force": random.uniform(-90.0, 90.0),
        "y_force": random.uniform(-180.0, 180.0),
        "z_force": random.uniform(-10.0, 10.0),
        "latitude": random.uniform(-90.0, 90.0),
        "longitude": random.uniform(-180.0, 180.0),
        "timestamps": [time.time() - i * 60 for i in range(10)],
        "altitudes": [random.uniform(1000, 20000) for _ in range(10)],
    }

    # Save flight data to file (simulation)
    save_flight_data(data)

    # Return the simulated live data
    return jsonify(data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10000)







