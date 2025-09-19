# ui.py

def print_cards(cards):
    # prints out the cards side by side using ascii
    top = []
    mid1 = []
    mid2 = []
    mid3 = []
    bot = []

    for card in cards:
        val = card.value
        suit = card.suit
        val_ljust = val.ljust(2)
        val_rjust = val.rjust(2)
        top.append("┌─────┐")
        mid1.append(f"│{val_ljust}   │")
        mid2.append(f"│  {suit}  │")
        mid3.append(f"│   {val_rjust}│")
        bot.append("└─────┘")

    # print each row line-by-line
    for row in [top, mid1, mid2, mid3, bot]:
        print(" ".join(row))


def choose_sorting_algorithm():
    # asks the user to pick one of the 4 sorting algorithms
    mapping = {
        "1": "merge",
        "2": "heap",
        "3": "binary",
        "4": "quick"
    }

    while True:
        print("\nChoose a sorting algorithm:")
        print("1. Merge Sort")
        print("2. Heap Sort")
        print("3. Binary Insertion Sort")
        print("4. Quick Sort")

        choice = input("Enter the number of the algorithm: ").strip()

        if choice in mapping:
            return mapping[choice]
        else:
            print("\nInvalid input. "
                  "\nPlease choose a number from 1 to 4.")
