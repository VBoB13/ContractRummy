from colorama import Fore
from typing import List, Tuple
import random

from game.user import User
from game.card import Card
from exceptions.players import PlayerException


class Player(User):
    def __init__(self, nickname: str, email: str = ""):
        super().__init__(nickname, email)
        self._hand = None

    def print(self):
        print(Fore.CYAN + "{}".format(self.nickname), Fore.RESET)

    @property
    def hand(self) -> Tuple[Card]:
        return self._hand

    @hand.setter
    def hand(self, value: Tuple[Card]) -> None:
        """
        Sets player's hand to tuple([Card, Card, ...]).
        """
        for card in value:
            if not isinstance(card, Card):
                raise PlayerException(
                    "Only Card instances allowed in player's hand!\nGot type: {}".format(type(card)))
        self._hand = value

    @hand.deleter
    def hand(self) -> None:
        """
        Deletes hand from player.
        """
        self.hand = tuple()

    def shuffle_hand(self) -> None:
        hand = list(self.hand)  # Immutable -> mutable
        random.shuffle(hand)  # Shuffle the mutable hand
        self.hand = tuple(hand)  # Assign immutable tuple to hand

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

    def add_card_multiple(self, cards: Tuple[Card]) -> None:
        """
        Adds multiple cards from a Tuple[Card, Card, ...] type object.
        """
        for card in cards:
            self.add_card(card)

    def play_card(self, card_pos: int) -> Card:
        """
        Plays the card in player's hand which is in the index position [card_pos].
        """
        hand_list = list(self.hand)  # Create a list (mutable) of hand
        card = hand_list.pop(card_pos)  # Extract card at position [card_pos]
        self.hand = tuple(hand_list)  # Make hand into the newly modified list
        return card
