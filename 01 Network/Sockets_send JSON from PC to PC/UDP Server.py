# import network
import socket
import json


# Define server parameters
UDP_IP = "0.0.0.0"
UDP_PORT = 12345

# # WiFi configuration
# SSID = "your_wifi_ssid"
# PASSWORD = "your_wifi_password"

# # Connect to WiFi
# sta_if = network.WLAN(network.STA_IF)
# sta_if.active(True)
# sta_if.connect(SSID, PASSWORD)

# while not sta_if.isconnected():
#   pass

# print("WiFi connected.")

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
  # Receive data
  data, addr = sock.recvfrom(2048)
  print(f'length of data: {len(data)}')

  # Decode JSON data
  try:
    decoded_data = json.loads(data.decode('utf-8'))

    # Extract values
    package_number = decoded_data.get('packagenumber')
    command = decoded_data.get('command')
    rgb_values = decoded_data.get('rgb_values')

    # Process the data as needed
    print(f"Package Number: {package_number}")
    print(f"RGB Values: {rgb_values}")

  except Exception as e:
    print(f"Error decoding or processing data: {e}")