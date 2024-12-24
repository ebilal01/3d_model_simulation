from flask import Flask, render_template, jsonify
import random
import time
import json  # Add this import statement

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the frontend HTML

@app.route('/live-data', methods=['GET'])
def live_data():
    try:
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

        # Save flight data to file (this will now work)
        save_flight_data(data)

        # Return the simulated live data
        return jsonify(data)

    except Exception as e:
        # If any error occurs, print the error and return a 500 status
        print(f"Error generating live data: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

def save_flight_data(data):
    try:
        # Save data to a file (you can customize this if needed)
        with open('force_data.json', 'w') as f:
            json.dump(data, f)  # This will work now
    except Exception as e:
        print(f"Error saving flight data: {e}")

if __name__ == '__main__':
    app.run(debug=True)











