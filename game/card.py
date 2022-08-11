from colorama import Fore

from ..exceptions.cards import CardException
from . import CARD_VALS, SUIT_VALS


class Card():
    """
    Class for a single card.
    """
    def __init__(self, value: int, suit: int):
        self._value = value
        if self.value != 14:
            self._suit = suit
            

    def __str__(self):
        return "{} of {}".format(CARD_VALS[self._value], SUIT_VALS[self._suit])


    # Value
    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, val: int) -> None:
        if val < 1 and val > 14:
            raise CardException("Value for card needs to be between 1 (Ace) and 14 (King).")
        self._value = val

    @value.deleter
    def value(self) -> None:
        del self._value

    @property
    def value_str(self) -> str:
        return CARD_VALS[self.value]

    # Suit
    @property
    def suit(self) -> int:
        return self._suit

    @suit.setter
    def suit(self, val: int) -> None:
        if val < 1 and val > 4:
            raise CardException("Suit value can only be between 1 (Cloves) and 4 (Spades).")
        self._suit = val

    @suit.deleter
    def suit(self) -> None:
        del self._suit

    @property
    def suit_str(self) -> str:
        return SUIT_VALS[self.suit]
