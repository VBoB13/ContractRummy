from .base import BaseException

class CardException(BaseException):
    """
    Exception that gets raised by individual cards.
    """

class DeckException(BaseException):
    """
    Exception that gets raised by a deck of cards.
    """
