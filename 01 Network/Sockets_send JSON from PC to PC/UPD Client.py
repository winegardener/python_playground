import socket
import json
import time
from random import randint

# UDP server address, change from localhost to dedicatet server ip, if you want to run it on 2 pcs
UDP_IP = "192.168.1.146"
UDP_PORT = 12345

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((UDP_IP, UDP_PORT))
print("Verbunden mit {}:{}".format(UDP_IP, UDP_PORT))

# Example data to send
for i in range(1000):
    data_to_send = {
        "packagenumber": i,
        "command" : "Send RGB data",
        "values": 50*[randint(0,255), randint(0,255), randint(0,255)]
    }
    # Convert the data to JSON
    json_data = json.dumps(data_to_send)
    # Send the data to the MicroPython UDP server
    sock.sendall(json_data.encode())
    confirmation_message = sock.recv(1024).decode()
    print("Bestätigung erhalten:", str(confirmation_message))

# Close the socket (optional)
sock.close()
