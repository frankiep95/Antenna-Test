import socket
import time

TCP_PORT = 22
BUFFER_SIZE = 1024


class IPInterface:
    def __init__(self,ip,port=TCP_PORT):
        self.__ip = ip
        self.__port = port

    def connect(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.settimeout(5)
        try:
            self.__socket.connect((self.__ip, self.__port))
        except socket.error:
            print("Failed to connect to IP address:", self.__ip, "on port:", self.__port)

    def send(self,message):
        try:
            self.__socket.sendall(message.encode())
        except socket.error:
            print("Failed to send message to IP address:", self.__ip, "on port:", self.__port)  
    

    def close(self):
        self.__socket.close()
