import random
from typing import List, Tuple, Iterator

from ..exceptions.cards import DeckException
from .card import Card
from . import CARD_VALS, SUIT_VALS


class Deck(List[Card]):
    """
    Class that handles a deck of Cards.
    """

    def __init__(self, jokers: bool = True, shuffle_deck: bool = True, num_of_decks: int = 1):
        """
        Method that instantiates a deck with 54 cards (regular 52 + 2 Jokers).
        """
        # Add cards to deck to initialize
        for deck_num in range(num_of_decks):
            for val in CARD_VALS.keys():
                if val != 14:
                    for suit_val in SUIT_VALS:
                        self.append(Card(val, suit_val))
                else:
                    if jokers:
                        for i in range(2):
                            self.append(Card(val))

        # Check so that there is correct amount of cards in deck
        if jokers:
            if len(self) != 54:
                self.clear()
                raise DeckException(
                    "Incorrect amount of cards in deck! (not 54)")
        else:
            if len(self) != 52:
                self.clear()
                raise DeckException(
                    "Incorrect amount of cards in deck! (not 52)")

        if shuffle_deck:
            random.shuffle(self)

    def __iter__(self) -> Iterator[Card]:
        for card in super().__iter__():
            if isinstance(card, Card):
                yield card
            else:
                raise DeckException("Decks can only contain Card objects!")

    def __str__(self):
        return "Deck with {} cards.".format(len(self))

    def deal_one(self) -> Card:
        """
        Method that deals (spits out) the first card from the deck.
        """
        if len(self) > 0:
            card = self.pop(0)
            return card
        raise DeckException("Can't deal any card when deck is empty!")

    def deal_multiple(self, num: int) -> Tuple[Card]:
        """
        Method that deals (spits out) multiple cards from the top of the deck.
        """
        card_list = []
        if num < len(self):
            for i in range(num):
                card_list.append(self.pop(0))

        else:
            raise DeckException(
                "Not enough cards to deal! Trying to deal {} cards when there are only {} left.".format(num, len(self)))

        return tuple(card_list)

    def count(self) -> int:
        """
        Returns the amount of remaining cards in deck - len(self)
        """
        return len(self)
