# Poker Hand Detector

A Python card game project for Computation II @ NOVA IMS.  
Players can draw a hand of cards, choose a sorting algorithm, and the program will sort, display, and detect any poker hands present. The game also tracks how many times each type of poker hand is found during the session.

---

## Technologies Used
- **Python 3**
- Object-Oriented Programming principles
- UML design for class structure

---

## Features
- Standard 52-card deck (spades, hearts, diamonds, clubs)
- User draws between 3 and 15 cards per round
- Choice of sorting algorithm:
  - Merge Sort (O(n log n))
  - Heap Sort (O(n log n))
  - Binary Insertion Sort (O(n²))
  - Quick Sort (O(n log n) on average)
- ASCII-art cards for a nicer display
- Poker hand detection:
  - Royal Flush
  - Straight Flush
  - Flush
  - Straight
  - Four of a Kind
  - Full House
  - Three of a Kind
  - Two Pair
  - One Pair
- Session statistics (counters for each detected hand type)
- Play again / exit option with reshuffling every round

---

## Project Structure

poker_project/
│
├── card.py          # card and deck classes
├── hand.py          # hand class and poker hand detection
├── sorters.py       # sorting algorithms
├── game.py          # game flow and session management
├── ui.py            # user input, menus, ascii display
├── constants.py     # global constants (suits, values, orders)
├── tests.py         # testing utilities
├── init.py          # marks package
└── main.py          # entry point

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/carlosamorim/Poker-Hand-Detector.py.git

---
This project was created for academic purposes at NOVA IMS and is NOT intended for commercial use.

## NOVA IMS @ 2025
**Carlos Amorim**
