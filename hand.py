# hand.py

from collections import Counter
from card import Card
from ui import print_cards


class Hand:
    # represents the hand of cards drawn from the deck

    def __init__(self, cards):
        # saves the cards in the hand
        self.cards = cards

    def sort(self, algorithm_name):
        # this method sorts the hand based on the user choosen sorting algorithm
        # and calls the SortManager to apply the algorithm

        from sorters import SortManager  # used a local import to avoid circular dependency
        SortManager.sort(self.cards, algorithm_name)

    def display(self):
        # shows the hand in ascii using print_cards() for a more aesthetic ui

        print_cards(self.cards)

    def detect_poker_hands(self):
        # checks for poker hands using the PokerHandDetector class
        return PokerHandDetector.detect(self.cards)


class PokerHandDetector:
    # contains the logic to detect poker hands and how many of each are in the drawn hand
    # static methods to detect every type of poker hand, used because no need for methods to store or remember anything

    # checks suit-based hands first (like flushes), then counts card values for pairs and sets

    @staticmethod
    def detect(cards):
        # returns a dictionary ( {hand_type: count} ) with hand types and how many times each showed up

        result = {}

        # flush and straight detection (only 1 occurrence max per drawn hand)
        if len(cards) >= 5:
            if PokerHandDetector.is_royal_flush(cards):  # checks for 10-J-Q-K-A of same suit
                result["Royal Flush"] = 1
                return result
            elif PokerHandDetector.is_straight_flush(cards):  # checks for both straight and flush combo
                result["Straight Flush"] = 1
                return result
            elif PokerHandDetector.is_flush(cards):  # True if all suits match
                result["Flush"] = 1
            elif PokerHandDetector.is_straight(cards):  # checks if cards form a sequence
                result["Straight"] = 1

        counts = list(PokerHandDetector.get_value_counts(cards).values())

        # count logic
        hand_tallies = Counter()
        # first analyze the value frequencies ie how many pairs, trips, or quads we have in this hand

        num_fours = counts.count(4)
        num_threes = counts.count(3)
        num_pairs = counts.count(2)

        if num_fours:
            hand_tallies["Four of a Kind"] = num_fours

        if num_threes and num_pairs:
            hand_tallies["Full House"] = min(num_threes, num_pairs)
            # Full house = 3 of a kind and a pair, use min for cases where there are multiple of each
            num_threes -= hand_tallies["Full House"]
            num_pairs -= hand_tallies["Full House"]
            # To avoid double-counting, decrement the number of threes and pairs after using them in a Full House

        if num_threes:
            hand_tallies["Three of a Kind"] = num_threes

        if num_pairs >= 2:
            hand_tallies["Two Pair"] = num_pairs // 2
            if num_pairs % 2 == 1:
                hand_tallies["One Pair"] = 1
        elif num_pairs == 1:
            hand_tallies["One Pair"] = 1

        # merge into result
        result.update(hand_tallies)
        return result

    @staticmethod
    def get_value_counts(cards):
        # counts how many of each value is in the hand and builds a dictionary e.g. counts == {'5': 3, '7': 1, 'K': 1}
        counts = {}
        for card in cards:
            counts[card.value] = counts.get(card.value, 0) + 1
        return counts

    @staticmethod
    def is_flush(cards):
        # is true if all cards have the same suit i.e. if they form a flush
        suits = [card.suit for card in cards]
        return all(suit == suits[0] for suit in suits)

    @staticmethod
    def is_straight(cards):
        # is true if cards form a consective sequence i.e.  a straight (like 5-6-7-8-9 or A-2-3-4-5)

        orders = sorted(card.get_order() for card in cards)

        # checks for regular straight
        is_seq = all(orders[i] == orders[i - 1] + 1 for i in range(1, len(orders)))

        # checks for a straight where the ace is the lowest card (A, 2, 3, 4, 5)
        if not is_seq and 'A' in [card.value for card in cards]:
            alt_orders = sorted(1 if card.value == 'A' else card.get_order() for card in cards)
            is_seq = all(alt_orders[i] == alt_orders[i - 1] + 1 for i in range(1, len(alt_orders)))

        return is_seq

    @staticmethod
    def is_royal_flush(cards):

        # is true if the drawn hand forms a royal flush (10 to A, all same suit).
        if not PokerHandDetector.is_flush(cards):
            return False
        values = set(card.value for card in cards)
        return values == {'10', 'J', 'Q', 'K', 'A'}

    @staticmethod
    def is_straight_flush(cards):
        # is true if the dran hand is both straight and flush
        return PokerHandDetector.is_flush(cards) and PokerHandDetector.is_straight(cards)
