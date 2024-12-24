from flask import Flask, render_template, jsonify
import random
import time
import json
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    # Render the main HTML file
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('force_data', {'message': 'Hello from the server!'})

@socketio.on('force_data')
def handle_force_data(data):
    print(f"Received data: {data}")
    # Example: Broadcast the force data back to all clients
    socketio.emit('force_data', data)

if __name__ == '__main__':
    # Run the Flask server
    socketio.run(app, host='0.0.0.0', port=5000)












