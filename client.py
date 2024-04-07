import socket
from time import time , sleep
from binascii import hexlify
import random
import string

HOST = 'localhost'
PORT = 12345
ONE = 0.06
ZERO = 0.12


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall("start".encode('utf-8'))

covert = "secert message"
covert_bin = ""
for i in covert:
    covert_bin += bin(int(hexlify(i.encode()), 16))[2:].zfill(8)

start_time = time()
string_length = 10
chars = string.ascii_letters + string.digits
for char in covert_bin:
    msg = ''.join(random.choices(chars, k=string_length))
    if (char == "0"):
        sleep(ZERO)
        client_socket.sendall(msg.encode('utf-8'))
    else:
        sleep(ONE)
        client_socket.sendall(msg.encode('utf-8'))
end_time =time()
print(f"bit rate = {len(covert_bin)/round(end_time - start_time, 3)}")
client_socket.sendto("end".encode('utf-8'), (HOST, PORT))
    
    
    
    
    
    
    
    