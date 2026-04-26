import socket
import time
# from types import String
JETSON_IP = "192.168.69.69"
JETSON_PORT = 6002
JETSON_ADDR_PORT = (JETSON_IP,JETSON_PORT )

class HMI_LOGGER:
    def __init__(self):
        self.socket = None 
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("HMI Connected")


    def log(self, message):
        message_byte = message.encode('utf-8')
        self.socket.sendto(message_byte, JETSON_ADDR_PORT)

    def __del__(self):
        self.socket.close()
