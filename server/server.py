from tabnanny import check
from colorama import Fore, Back, Style
import socket
import threading

from . import check_ip

HEADER = 64
PORT = 5050
SERVER = check_ip()
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(Fore.GREEN + "[SERVER]" + Fore.CYAN + f" {addr}" + Fore.RESET, "connected.")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(Fore.LIGHTYELLOW_EX + f"[{addr}]" + Fore.RESET, f"{msg}")
            full_msg = Fore.LIGHTGREEN_EX + "[SERVER - INFO]" + Fore.RESET + " Message received."
            conn.send(full_msg.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(Fore.GREEN + "[SERVER]" + Fore.RESET, "Listening on {}".format(SERVER))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(Fore.GREEN + "[SERVER]" + Fore.RESET, "Active connections:" + Fore.CYAN + " {}".format(threading.activeCount() - 1) + Fore.RESET)


if __name__ == "__main__":
    print(Fore.GREEN + "[SERVER]", Fore.RESET, "Starting...")
    start()
