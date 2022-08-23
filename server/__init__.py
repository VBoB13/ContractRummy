import subprocess
import socket
from sys import platform
from colorama import Fore
from typing import Tuple

DISCONNECT_MESSAGE = "!DISCONNECT"
HEADER = int(2048)
PORT = int(5050)
FORMAT = "utf-8"


def check_ip():
    address = ""
    if platform == 'linux':
        address = subprocess.check_output(
            ["ifconfig", "|", "egrep", "'192\.168\.[0-9]{1}\.[0-9]{1,3}'", "|", "awk", "'{print $2}'"])
    elif platform == 'darwin':
        address = subprocess.check_output(["ipconfig", "getifaddr", "en0"])
    else:
        address = socket.gethostbyname(socket.gethostname())

    print(Fore.LIGHTGREEN_EX + "[SERVER - INFO]" + Fore.RESET,
          "Platform: " + Fore.RED + platform + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "[SERVER - INFO]" + Fore.RESET, "Server IP: " +
          Fore.RED + address.decode('utf-8').strip('\n') + Fore.RESET)

    return address.decode('utf-8').strip('\n')


SERVER = check_ip()


def read_pos(string: str) -> Tuple[int, int]:
    pos_list = string.split(",")
    return int(pos_list[0]), int(pos_list[1])


def make_pos(tup: tuple) -> str:
    return str(tup[0]) + "," + str(tup[1])
