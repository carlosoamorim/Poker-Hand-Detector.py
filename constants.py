# constants.py

# Global constants for the suits, values, and the value order

SUITS = ['♠', '♥', '♦', '♣']

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

VALUE_ORDER = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
    # A=14 by default, later implementation for the specific case where A=1
    # will be inside the poker hand detection logic
}