from . import DECK_SIZE
from .deck import Deck
from player import Player
from exceptions.game import GameException


class Game(object):
    """
    Object that keeps track of game state and players' statuses.
    """

    def __init__(self, players: int = 3):
        # Create a deck of cards depending on the number of players in the game
        for num_of_decks in range(5):
            if (players * 12) <= ((DECK_SIZE*num_of_decks)/(2/3)):
                continue
            else:
                self._deck = Deck(num_of_decks=num_of_decks)
                break

    @property
    def deck(self) -> Deck:
        """
        Returns the main deck of the game.
        """
        return self._deck

    @deck.setter
    def deck(self, value: Deck):
        """
        Initializes main Deck of the game.
        """
        if not isinstance(value, Deck):
            raise GameException(
                "Deck property must be an instance of the 'Deck' class!")
        self._deck = value

    @deck.deleter
    def deck(self):
        del self._deck
