import socket
from colorama import Fore, Back, Style
import pygame

from network import Network
from player import Player
from game.deck import Deck
from game.card import Card
from . import DISCONNECT_MESSAGE, HEADER, SERVER, PORT
from game import WINDOW_SIZE
from exceptions.client import ClientException

FORMAT = str('utf-8')
ADDR = (SERVER, PORT)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
except Exception as err:
    raise ClientException("Could not connect to {}".format(SERVER)) from err

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Contract Rummy")
clientNumber = 0


def send(msg: str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def redrawWindow(card: Card):
    window.fill((255, 255, 255))
    card.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    pos = n.pos  # TWT Online Game Tutorial Pt.4
    card = Card()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                send(DISCONNECT_MESSAGE)
                pygame.quit()

        card.move()
        redrawWindow(card)


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
