from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the frontend HTML

@app.route('/live-data', methods=['GET'])
def live_data():
    # Simulate force vectors for movement and rotation
    data = {
        "force": {
            "x": random.uniform(-10, 10),
            "y": random.uniform(-10, 10),
            "z": random.uniform(-10, 10)
        },
        "rotation": {
            "x": random.uniform(-1, 1),
            "y": random.uniform(-1, 1),
            "z": random.uniform(-1, 1)
        }
    }

    # Save the simulated force data to a file (optional)
    save_flight_data(data)

    # Return the simulated live force and rotation data
    return jsonify(data)

def save_flight_data(data):
    # Save data to a file (you can customize this if needed)
    with open('force_data.json', 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    app.run(debug=True)











