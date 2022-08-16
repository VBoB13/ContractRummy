import subprocess
import socket
from sys import platform
from colorama import Fore

DISCONNECT_MESSAGE = "!DISCONNECT"


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
