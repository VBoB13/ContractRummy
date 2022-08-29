from colorama import Fore, Back, Style
import socket
from socket import socket as _socket
import threading

from . import check_ip, DISCONNECT_MESSAGE, HEADER, SERVER, PORT, FORMAT, make_pos, read_pos

ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

pos = [(250, 0), (250, 500)]

CURRENT_PLAYER = int(0)


def handle_client(conn: _socket, addr, player: int):
    global CURRENT_PLAYER
    print(Fore.GREEN + "[SERVER]" + Fore.CYAN +
          f" {addr}" + Fore.RESET, "connected.")

    conn.send(str.encode(make_pos(pos[player])))

    connected = True

    while connected:
        reply = ""
        raw_data = conn.recv(HEADER).decode(FORMAT)
        if raw_data:
            print("Raw data:", raw_data)
            data = read_pos(raw_data)
            pos[player] = data

        if data == DISCONNECT_MESSAGE:
            connected = False
            print(Fore.LIGHTGREEN_EX + "[SERVER]" +
                  Fore.CYAN, "{}".format(addr), "disconnected." + Fore.RESET)
            CURRENT_PLAYER -= int(1)
        if data:
            if player == 1:
                reply = pos[0]
            else:
                reply = pos[1]
            client_msg = Fore.LIGHTGREEN_EX + "[SERVER] " + Fore.LIGHTYELLOW_EX + \
                "{}".format(addr) + Fore.RESET + " {}".format(data)
            print(client_msg)
            conn.send(str.encode(make_pos(reply)))

    conn.close()


def start():
    global CURRENT_PLAYER
    server.listen()
    print(Fore.GREEN + "[SERVER]" + Fore.RESET,
          "Listening on {}:{}.".format(SERVER, PORT))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(
            target=handle_client, args=(conn, addr, CURRENT_PLAYER))
        thread.start()
        CURRENT_PLAYER += int(1)
        print(Fore.GREEN + "[SERVER]" + Fore.RESET, "Active connections:" +
              Fore.CYAN + " {}".format(threading.activeCount() - 1) + Fore.RESET)


if __name__ == "__main__":
    print(Fore.GREEN + "[SERVER]", Fore.RESET, "Starting...")
    start()
