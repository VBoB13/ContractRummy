from colorama import Fore
from typing import List, Tuple

from user import User
from .game.card import Card
from .exceptions.players import PlayerException


class Player(User):
    def __init__(self, email: str, nickname: str):
        super().__init__(email, nickname)
        self._hand = None

    def print(self):
        print(Fore.CYAN + "{}".format(self.nickname), Fore.RESET)

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value: Tuple[Card]):
        """
        Sets player's hand to tuple([Card, Card, ...]).
        """
        for card in value:
            if not isinstance(card, Card):
                raise PlayerException(
                    "Only Card instances allowed in player's hand!\nGot type: {}".format(type(card)))
        self._hand = value

    @hand.deleter
    def hand(self):
        """
        Deletes hand from player.
        """
        self.hand = tuple()

    def add_card(self, card: Card) -> None:
        """
        Updates player's hand in-place.
        """
        card_list = list(self.hand)
        if isinstance(card, Card):
            card_list.append(card)
        else:
            raise PlayerException(
                "Only Card instances allowed in player's hand!\nGot type: {}".format(type(card)))
        self.hand = tuple(card_list)
