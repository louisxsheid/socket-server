from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode="eventlet")

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
