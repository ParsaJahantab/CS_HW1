import socket
from time import time

ONE = 0.06
ZERO = 0.12
HOST = 'localhost'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
print(f"Server listening on port {PORT} (TCP)")
server_socket.listen()
client_socket, client_address = server_socket.accept()
print(f"Connected by {client_address}")

covert_bin = ""
data = client_socket.recv(1024).decode('utf-8')
count = 0
if data == "start":
    while True:
        t0 = time()
        data = client_socket.recv(1024).decode('utf-8')
        t1 = time()
        delta = round(t1 - t0, 3)
        if data == "end":
            break
        if (delta >= 0.12):
            covert_bin += "0"
        else:
            covert_bin += "1"
        count += 1
        
covert = ''
for i in range(0, len(covert_bin), 8):
    covert += chr(int(covert_bin[i:i+8], 2))
    
print(covert)
print("Server shutting down")