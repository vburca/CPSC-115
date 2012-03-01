# File: cards.py
# Author: cpsc115
# Date: Novebmer 8, 2010
# Description:  This module contains definitions of the Card, Deck, and Hand clases.

# Import the random module
import random

# The Card class represents a card in temrs of two attributes, its suit
# and its rank. 
class Card(object):
    """represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        # suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        # ranks are the same... it's a tie
        return 0    

# The Deck class represents a deck of cards.  The
# cards are stored in a list. It includes methods
# to pop, add, shuffle, and deal cards. 
class Deck(object):
    """represents a deck of cards"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()

    def deal(self, hand, n):
       for i in range(n):
          hand.add_card(self.pop_card())
       return hand

# The Hand class is a subclass of Deck.  It stores a 
# sublist of a deck -- i.e., usually fewer than 52 cards.
# It is meant to be subclassed to represent different
# card games, such as blackjack, poker, hearts. 
class Hand(Deck):
    """represents a hand of playing cards"""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

