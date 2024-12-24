from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    # This renders the HTML page with the 3D model viewer
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('force_data', {'message': 'Hello from the server!'})

@socketio.on('force_data')
def handle_force_data(data):
    print(f"Received data: {data}")
    # You can send responses to the frontend
    emit('force_data', {'message': 'Data received by server!'})

if __name__ == '__main__':
    # Run the Flask server with SocketIO
    socketio.run(app, host='0.0.0.0', port=5000)


