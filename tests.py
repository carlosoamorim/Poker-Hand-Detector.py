# TESTING

# test_special_hands()
# test_hand_sorting()
# test_deck()


"""
    def test_deck():
        deck = Deck()
        deck.shuffle()
        cards_drawn = deck.draw(5)
        print("Cards drawn:", cards_drawn)
        print("Cards remaining:", len(deck.cards))


    if __name__ == "__main__":
        test_deck()
"""

""" 
def test_special_hands(): 
# test special hand detection. substitute the cards list with the lists below to test all the special hands
    cards = [ 
    # royal flush:
        Card('10', '♠'),
        Card('J', '♠'),
        Card('Q', '♠'),
        Card('K', '♠'),
        Card('A', '♠'),
    ]

    hand = Hand(cards)
    hand.sort("merge")  # Optional, in case order matters for straight detection
    hand.display()

    results = hand.detect_poker_hands()
    print("\nDetected hands:", results)

# substitute     

    cards = [  

    # straight flush:

        Card('9', '♠'), 
        Card('10', '♠'),
        Card('K', '♠'),
        Card('J', '♠'),
        Card('Q', '♠'),
    ]

    cards = [  

    # straight with A = 1 i.e. wheel straight;

        Card('A', '♠'),
        Card('2', '♠'),
        Card('3', '♠'),
        Card('4', '♠'),
        Card('5', '♠'),
    ]

    cards = [  

    # flush:

        Card('J', '♠'),
        Card('2', '♠'),
        Card('8', '♠'),
        Card('4', '♠'),
        Card('10', '♠'),
    ]

    cards = [  

    # full house:

        Card('Q', '♣'),
        Card('Q', '♣'),
        Card('Q', '♣'),
        Card('5', '♥'),
        Card('5', '♥'),
    ]

    cards = [  

    # invalid straight:

        Card('Q', '♣'),
        Card('K', '♣'),
        Card('A', '♣'),
        Card('2', '♥'),
        Card('3', '♥'),
    ]

from card import Deck
from hand import Hand
from ui import choose_sorting_algorithm

def test_hand_sorting():
    deck = Deck()
    deck.shuffle()
    cards = deck.draw(7)
    hand = Hand(cards)

    print("Original hand:")
    hand.display()

    algorithm = choose_sorting_algorithm()
    hand.sort(algorithm)

    print("\nSorted hand:")
    hand.display()
    
    
    from test_utils import test_hand_sorting
    test_hand_sorting()
    
    """