# game.py


from collections import Counter
from card import Deck
from hand import Hand
from ui import choose_sorting_algorithm


class Game:

    # runs the whole game and keeps track of hand statistics

    def __init__(self):
        # sets up the game with a fresh deck and an empty stats counter
        self.stats = Counter()
        self.deck = Deck()

    def start(self):
        # the main loop that handles the full game flow
        print("♠ ♥ ♦ ♣  Welcome to the NOVA IMS Poker Tables! ♣ ♦ ♥ ♠")
        print("Here we deal in cards, sort in O(n log n), and gamble with complexity!")

        while True:
            self.play_round()

            while True:
                again = input("\nFeeling lucky?"
                              "\nShall we play again? (y/n): ").strip().lower()
                if again == 'y':
                    break
                elif again == 'n':
                    self.show_stats()
                    print("\nExiting... "
                          "\n♠ ♥ ♦ ♣ Thank you playing at the NOVA IMS Poker Tables! ♠ ♥ ♦ ♣"
                          "\nYou can exchange your chips at the reception with Dona Rute."
                          "\nGoodbye!")
                    return
                else:
                    print("Invalid input. Please enter 'y' to play again or 'n' to end the game.")

    def play_round(self):
        # handles one round of play: shuffle, draw, sort, detect hands

        print("\nShuffling the deck...")
        self.deck = Deck()
        self.deck.shuffle()

        print("\nHow many cards would you like to draw? (choose a number between 3 and 15)")
        while True:
            try:
                count = int(input("Enter number of cards: "))
                if 3 <= count <= 15:
                    break
                else:
                    print("Please choose a number between 3 and 15.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        drawn_cards = self.deck.draw(count)
        hand = Hand(drawn_cards)

        print("\nYour drawn hand:")
        hand.display()

        algo = choose_sorting_algorithm()
        hand.sort(algo)

        complexities = {
            "merge": "O(n log n)",
            "heap": "O(n log n)",
            "binary": "O(n²)",
            "quick": "O(n log n) -- on average"
        }

        print(f"\nSorting completed using {algo.title()} Sort with time complexity: {complexities[algo]}")

        print("\nYour sorted hand:")
        hand.display()

        # detect poker hands
        results = hand.detect_poker_hands()
        if results:
            print("\nLucky you! The following poker hands were detected:")
            for hand_type, count in results.items():
                print(f"- {count}x {hand_type}")
                self.stats[hand_type] += count
        else:
            print("\nOh bummer! No poker hands were detected :/ ")

    def show_stats(self):
        # displays how many times each poker hand was detected during the session
        print("\nSession Summary:")
        if not self.stats:
            print("No poker hands were detected during this session :/ ")
        else:
            for hand_type, count in self.stats.items():
                print(f"{hand_type}: {count} time(s)")
