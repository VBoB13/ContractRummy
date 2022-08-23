import socket
from . import SERVER, PORT, HEADER, FORMAT


class Network(object):
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = PORT
        self.addr = (self.server, self.port)
        self._pos = self.connect()

    @property
    def pos(self):
        return self._pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode(FORMAT)
        except:
            pass

    def send(self, data: str):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode(FORMAT)
        except socket.error as e:
            print(e)
