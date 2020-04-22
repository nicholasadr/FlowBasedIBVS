import socket

HOST = '127.0.0.1'
PORT = 50055
s_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_.connect((HOST, PORT))
frames=0
s_.send(str.encode(str(frames)))
