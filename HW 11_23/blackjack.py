#
# File: blackjack.py
# Author: Vlad Burca
#         Max Xiaoqi
#
# Created:  11/23/10
# Modified: 11/23/10
#

from cards import Card, Deck, Hand

#
# BlackJack Class
#

class BlackjackHand(Hand):

    def __init__(self, label = ''):
        self.cards = []
        self.label = label

    def __cmp__(self, other):
        if self.total() > other.total():
            return 1
        elif self.total() < other.total():
            return -1
        else:
            return 0

    def getLabel(self):
        return self.label

    def total(self):
        total = 0
        faces = ['Jack', 'Queen', 'King']
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        aces = 0
        for card in self.cards:
            rank = Card.rank_names[card.rank]
            if rank in faces:
                total = total + 10
            elif rank in numbers:
                total = total + int(rank)
            elif rank == 'Ace':
                aces = aces + 1
        if aces != 0:
            if total + 11 > 21:
                total = total + aces * 1
            elif total + 11 <= 21:
                total = total + 11 + (aces - 1) * 1
        return total

    def isaBust(self):
        if self.total() > 21:
            return True
        else:
            return False

    def isaBlackjack(self):
        if self.total() == 21:
            return True
        else:
            return False

#
# Main Program
#


def status(owner):
    print owner.getLabel(), " hand: (", owner.total(), "): ", owner
    if owner.isaBlackjack():
        print "That's Blackjack!"
    elif owner.isaBust():
        print "That is a Bust!"

print "\t\t\t Caesar - Todor's Palace"
print "\t\t\t ***********************"

deck = Deck()
deck.shuffle()

dealer = BlackjackHand('Dealer')
player_name = raw_input(" Please enter your name: ")
player = BlackjackHand(player_name)

deck.deal(dealer, 2)
deck.deal(player, 2)

print
print

status(dealer)
status(player)
if player.isaBlackjack() == True or player.isaBust() == True:
    choice = 0
if player.isaBust() == False:
    out = player.getLabel() + ", type 1 for a hit and 0 to stay >> "
    choice = input(out)

while dealer.isaBust() == False and player.isaBust() == False \
      and (choice == 1 or dealer.total() < 17):
    while choice == 1:
        deck.deal(player, 1)
        print player.getLabel(), " hand: (", player.total(), "): ", player
        if player.isaBlackjack():
            print "That's Blackjack!"
            choice = 0
        elif player.isaBust():
            print "That is a Bust!"
            choice = 0
        else:
            choice = input(out)
    print
    print player.getLabel(), " total is ", player.total(), " and ", \
          dealer.getLabel(), " total is ", dealer.total(), ". "
    if player.isaBust():
        print player.getLabel(), " went bust and loses the hand."
    print
    print dealer.getLabel(), "'s turn. Type any key to continue. "
    key = raw_input()
    if dealer.total() >= 17:
        print dealer.getLabel(), " stays with ", dealer.total()
    else:
        print dealer.getLabel(), " takes a hit. "
        deck.deal(dealer, 1)
        status(dealer)
        while dealer.total() < 17:
            print dealer.getLabel(), " takes a hit. "
            deck.deal(dealer, 1)
            status(dealer)
    print
    print player.getLabel(), " total is ", player.total(), " and ", \
          dealer.getLabel(), " total is ", dealer.total(), ". "
    if dealer.isaBust():
        print dealer.getLabel(), " went bust and loses the hand."
    print
    print player.getLabel(), "'s turn. Type any key to continue. "
    key = raw_input()
    if player.isaBlackjack() == False and player.isaBust() == False:
        out = player.getLabel() + ", type 1 for a hit and 0 to stay >> "
        choice = input(out)

print
print
print " ~~ Game Over! ~~ "
print
print player.getLabel(), " has ", player.total(), ". "
print dealer.getLabel(), " has ", dealer.total(), ". "
print
if player.isaBust():
    print player.getLabel(), " went bust. "
    print dealer.getLabel(), " wins this hand! "
elif dealer.isaBust():
    print dealer.getLabel(), " went bust. "
    print player.getLabel(), " wins this hand! "
else:
    if dealer > player:
        print dealer.getLabel(), " wins this hand! "
    elif dealer < player:
        print player.getLabel(), " wins this hand! "
    else:
        print "It's a draw! "

            
    
    
    
