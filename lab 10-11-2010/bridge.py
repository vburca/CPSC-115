#
# File: bridge.py
# Author: Vlad Burca, Lauren Boulbol
# Lab Section: Wednesday
# 
# Created:       11/10/2010
# Last Modified: 11/10/2010
#

from cards import Card, Deck, Hand

class BridgeCard(Card):
    
    suit_names = ['C', 'D', 'H', 'S']
    rank_names = [None, None, '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'J', 'Q', 'K', 'A']
    point_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 , 2, 3, 4]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return "%s%s" % (BridgeCard.rank_names[self.rank],
                         BridgeCard.suit_names[self.suit])
        
class BridgeDeck(Deck):
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(2,15):
                card = BridgeCard(suit, rank)
                self.cards.append(card)
    
class BridgeHand(Hand):
    
    def getName(self):
        return self.label
    
    def countPoints(self):
        total_points = 0
        for card in self.cards:
            total_points = total_points + BridgeCard.point_values[card.rank]        
        return total_points
    
    def __cmp__(self, other):
        if self.countPoints() > other.countPoints():
            return True
        else:
            return False
        

card1 = BridgeCard(2,3)    # 3H  3 of Hearts
card2 = BridgeCard(0,11)   # JC  Jack of Clubs
card3 = BridgeCard(3,12)   # KS  King of Spades
card4 = BridgeCard(3,13)   # AS  Ace of spaces
print "#########################################"
print " 1.1 "
print
print card1
print card2
print card3
print card4
print
print "#########################################"
print " 1.2 "
print
deck = BridgeDeck()
print deck
print
deck.shuffle()
print deck
print
deck.sort()
print deck
print
print "#########################################"
print " 1.3, 1.4 "
print
deck = BridgeDeck()
deck.shuffle()
bridgetable = ['North', 'South', 'East', 'West']
for i in range(len(bridgetable)):
    bridgetable[i] = BridgeHand(bridgetable[i])
for i in range(52/len(bridgetable)):
    for i in range(len(bridgetable)):
        deck.deal(bridgetable[i], 1)
        
print "Done dealing, deck = "
print deck
imax = 0
for i in range(len(bridgetable)):
    bridgetable[i].sort()
    print bridgetable[i].getName(), " ( ", bridgetable[i].countPoints(), \
    " ): ", bridgetable[i]
    if bridgetable[i] > bridgetable[imax]:
        imax = i
print
print " The high hand is: "
print bridgetable[imax].getName(), " ( ", bridgetable[imax].countPoints(), \
    " ): ", bridgetable[imax]