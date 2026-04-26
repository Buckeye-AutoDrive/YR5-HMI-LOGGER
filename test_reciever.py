import socket
import time

JETSON_IP = "0.0.0.0"
JETSON_PORT = 6002
JETSON_ADDR_PORT = (JETSON_IP,JETSON_PORT )
buffer_size = 1024


UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
UDPServerSocket.bind(JETSON_ADDR_PORT)
print("UDP server up and listening")

while(True):
    msg, addr = UDPServerSocket.recvfrom(buffer_size)
    msg = msg.decode('utf-8')
    print("Message from Client: {}".format(msg))