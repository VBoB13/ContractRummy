import socket

from . import check_ip, DISCONNECT_MESSAGE
from ..exceptions.client import ClientException

HEADER = int(64)
PORT = int(5050)
FORMAT = str('utf-8')
SERVER = check_ip()
ADDR = (SERVER, PORT)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
except Exception as err:
    raise ClientException("Could not connect to {}".format(SERVER)) from err


def send(msg: str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


if __name__ == "__main__":
    send("Hello bitches!")
    send("Hi cool people!")
    send("And hi Richard! (:")
    send(DISCONNECT_MESSAGE)
