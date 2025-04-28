from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'Akad & Parinaz Private Chat is Live!'

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    emit('message', msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
