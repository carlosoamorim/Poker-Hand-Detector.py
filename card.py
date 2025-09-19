# card.py

import random
from constants import SUITS, VALUES, VALUE_ORDER


class Card:

    # represents a single playing card with its corresponding value and suit

    def __init__(self, value, suit):
        # sets the card’s value and suit
        self.value = value
        self.suit = suit

    def __repr__(self):
        # returns the card e.g. 'A♠' or '10♦'
        return f"{self.value}{self.suit}"

    def get_order(self):
        # gets the numeric value for sorting (like 11 for J)
        return VALUE_ORDER[self.value]


class Deck:

    # represents a standard deck of 52 unique playing cards, each value with the corresponding unique suit

    def __init__(self):
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]
        # a nested loop with list comprehension must be used to achieve the standard 52 card deck,
        # where the outer loop iterates trough each one of the 4 suits
        # and the inner loop itrates trough each of the 13 types of cards,
        # thus resulting (for every pair) in the object Card(value, suit)

    def shuffle(self):
        # randomizes the deck order
        random.shuffle(self.cards)

    def draw(self, count):
        # takes count cards from the top of the deck
        if count > len(self.cards):
            raise ValueError("Not enough cards left in the deck.")
        drawn = self.cards[:count]
        self.cards = self.cards[count:]
        return drawn

    def reset(self):
        # resets the deck to the standard 52 card deck
        self.__init__()