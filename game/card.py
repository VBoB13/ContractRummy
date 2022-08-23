from colorama import Fore
from typing import Tuple
import pygame

from exceptions.cards import CardException
from . import CARD_VALS, SUIT_VALS, WINDOW_SIZE, MOVE_SPEED


class Card(object):
    """
    Class for a single card.
    """

    def __init__(self, value: int, suit: int, x_pos: int = (WINDOW_SIZE[0]/2), y_pos: int = (WINDOW_SIZE[1]/2), width: int = 50, height: int = 75):
        self.value = value
        self.suit = suit
        self._x = x_pos
        self._y = y_pos
        self._width = width
        self._height = height

    def __str__(self):
        return "{} of {}".format(CARD_VALS[self._value], SUIT_VALS[self._suit])

    # Value

    @property
    def value(self) -> int:
        """
        Return the card's value.
        """
        return self._value

    @value.setter
    def value(self, val: int) -> None:
        """
        Set a card's value to 'val'.
        """
        if isinstance(val, int):
            if val < 1 and val > 14:
                raise CardException(
                    "Value for card needs to be between 1 (Ace) and 14 (King).")
            self._value = val
        else:
            raise CardException(
                "Can only set a card value to [int] values; NOT {}.".format(type(val)))

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
            raise CardException(
                "Suit value can only be between 1 (Clubs) and 4 (Spades).")
        self._suit = val

    @suit.deleter
    def suit(self) -> None:
        del self._suit

    @property
    def suit_str(self) -> str:
        return SUIT_VALS[self.suit]

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        if value < 0:
            raise CardException(
                "Can only set coordinates to POSITIVE values, not {}.".format(value))
        self._x = value

    @x.deleter
    def x(self):
        self._x = int(0)

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        if value < 0:
            raise CardException(
                "Can only set coordinates to POSITIVE values, not {}.".format(value))
        self._y = value

    @y.deleter
    def y(self):
        self._y = int(0)

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        if value < 0:
            raise CardException(
                "Can only set physical properties to POSITIVE values, not {}.".format(value))
        self._width = value

    @width.deleter
    def width(self):
        self._width = int(50)

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        if value < 0:
            raise CardException(
                "Can only set physical properties to POSITIVE values, not {}.".format(value))
        self._height = value

    @height.deleter
    def height(self):
        self._height = int(75)

    @property
    def rect(self) -> Tuple[int, int, int, int]:
        return (self.x, self.y, self.width, self.height)

    @property
    def color(self) -> Tuple[int, int, int]:
        return (int(255), int(0), int(0))

    def default(self) -> None:
        """
        Restore the Card's default width, height, x and y values.
        """
        self.default_pos()
        self.default_size()

    def default_pos(self) -> None:
        """
        Restore the Card's default x and y values.
        """
        del self.x
        del self.y

    def default_size(self) -> None:
        """
        Restore the Card's default width and height values.
        """
        del self.width
        del self.height

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= MOVE_SPEED

        if keys[pygame.K_RIGHT]:
            self.x += MOVE_SPEED

        if keys[pygame.K_UP]:
            self.y -= MOVE_SPEED

        if keys[pygame.K_DOWN]:
            self.y += MOVE_SPEED
