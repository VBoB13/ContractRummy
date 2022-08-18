import random
from typing import List, Tuple, Iterator
import pygame

from exceptions.cards import DeckException
from .card import Card
from . import CARD_VALS, SUIT_VALS, WINDOW_SIZE, MOVE_SPEED


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
                    for suit_val in SUIT_VALS.keys():
                        self.append(Card(val, suit_val))
                else:
                    if jokers:
                        for i in range(2):
                            self.append(Card(val, 4-i))

        self.x = int(WINDOW_SIZE[0]/2)
        self.y = int(WINDOW_SIZE[1]/2)
        self.width = int(50)
        self.height = int(50)

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

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        if (value > WINDOW_SIZE[0]) or (value < 0):
            raise DeckException(
                "Deck X position out of bounds!\nX: {}".format(self._x))
        self._x = value

    @x.deleter
    def x(self):
        del self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        if (value > WINDOW_SIZE[1]) or (value < 0):
            raise DeckException(
                "Deck Y position out of bounds!\nY: {}".format(self._y))
        self._y = value

    @y.deleter
    def y(self):
        del self._y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @width.deleter
    def width(self):
        del self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @height.deleter
    def height(self):
        del self._height

    @property
    def rect(self):
        return (self.x, self.y, self.width, self.height)

    @property
    def color(self):
        return (255, 0, 0)

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
