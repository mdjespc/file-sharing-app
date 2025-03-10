from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}
connected_devices = set()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register_device():
    data = request.get_json()
    ip = data.get("ip")

    if ip:
        connected_devices.add(ip)

    return jsonify({"success":True})

@app.route('/register', methods=["GET"])
def get_devices():
    return jsonify({"devices":
                    list(connected_devices)})

# @socketio.on('connect')
# def handle_connect():
#     emit('user_connected', {'message': 'A user has connected'})

# @socketio.on('register')
# def handle_register(data):
#     users[data['id']] = request.sid
#     emit('user_list', list(users.keys()), broadcast=True)

# @socketio.on('offer')
# def handle_offer(data):
#     recipient_sid = users.get(data['target'])
#     if recipient_sid:
#         emit('offer', data, room=recipient_sid)

# @socketio.on('answer')
# def handle_answer(data):
#     recipient_sid = users.get(data['target'])
#     if recipient_sid:
#         emit('answer', data, room=recipient_sid)

# @socketio.on('ice-candidate')
# def handle_ice_candidate(data):
#     recipient_sid = users.get(data['target'])
#     if recipient_sid:
#         emit('ice-candidate', data, room=recipient_sid)

# @socketio.on('disconnect')
# def handle_disconnect():
#     user_id = None
#     for key, value in users.items():
#         if value == request.sid:
#             user_id = key
#             break
#     if user_id:
#         del users[user_id]
#     emit('user_list', list(users.keys()), broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
