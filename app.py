from flask import Flask, render_template, jsonify
import random
import time
import json

app = Flask(__name__)

# Simulated function to save flight data (you may adjust this to save to a file)
def save_flight_data(data):
    with open("flight_data.json", "w") as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the frontend HTML

@app.route('/live-data', methods=['GET'])
def live_data():
    # Simulate rotation and force data for testing
    data = {
        "rotation": {
            "x": random.uniform(0, 2 * 3.14159),  # Random rotation on x-axis
            "y": random.uniform(0, 2 * 3.14159),  # Random rotation on y-axis
            "z": random.uniform(0, 2 * 3.14159)   # Random rotation on z-axis
        },
        "forces": [
            {
                "x": random.uniform(-10, 10),
                "y": random.uniform(-10, 10),
                "z": random.uniform(-10, 10),
                "magnitude": random.uniform(1, 20)
            } for _ in range(3)
        ]
    }

    # Save flight data to file (optional)
    save_flight_data(data)

    return jsonify(data)  # Return the simulated live data

if __name__ == '__main__':
    app.run(debug=True)











