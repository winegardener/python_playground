import socket
import json
import time

# UDP server address, change from localhost to dedicatet server ip, if you want to run it on 2 pcs
UDP_IP = "localhost"
UDP_PORT = 12345

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Example data to send
for i in range(1000):
    data_to_send = {
        "packagenumber": i,
        "rgb_values": 60*[255-i, i, (255+i)/2]
    }

    # Convert the data to JSON
    json_data = json.dumps(data_to_send)

    # Send the data to the MicroPython UDP server
    sock.sendto(json_data.encode('utf-8'), (UDP_IP, UDP_PORT))
    time.sleep(0.1)

# Close the socket (optional)
sock.close()
