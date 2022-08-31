import socket
from colorama import Fore, Back, Style
from typing import Tuple
import pygame

from server.network import Network
from game.card import Card
from . import DISCONNECT_MESSAGE, HEADER, SERVER, PORT, make_pos, read_pos
from game import WINDOW_SIZE
from exceptions.client import ClientException

FORMAT = str('utf-8')
ADDR = (SERVER, PORT)

# try:
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect(ADDR)
# except Exception as err:
#     raise ClientException("Could not connect to {}".format(SERVER)) from err

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Contract Rummy")


def send(msg: str, client: Network):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))


def redrawWindow(card: Card, card2: Card):
    global window
    window.fill((255, 255, 255))
    card.draw(window)
    card2.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    pos = n.pos
    card = Card(1, 4, x_pos=int(pos[0]), y_pos=int(pos[1]))
    card2 = Card(1, 3, 0, 0)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        card2_pos = read_pos(n.send(make_pos((card2.x, card2.y))))
        card2.x = card2_pos[0]
        card2.y = card2_pos[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                send(DISCONNECT_MESSAGE, n)
                pygame.quit()

        card.move()
        redrawWindow(card, card2)


if __name__ == "__main__":
    main()
    # print(Fore.LIGHTYELLOW_EX + "[CLIENT] " +
    #       Fore.RESET + "Welcome to Contract Rummy, player!")
    # email = input(
    #     "What's your email?\nIf you don't want to provide it, just press [ENTER]\nEmail: ")
    # nickname = input("What nickname would you like to use?\nNickname: ")
    # player = Player(email, nickname)

    # send("Hello bitches!")
    # send("Hi cool people!")
    # send("And hi Richard! (:")
    # send(DISCONNECT_MESSAGE)
