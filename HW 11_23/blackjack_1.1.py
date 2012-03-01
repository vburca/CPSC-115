#
# File: blackjack.py
# Author: Vlad Burca
#         Max Xiaoqi
#
# Created:  11/09/10
# Modified: 11/21/10
#
# Description:
#       This program is meant to simulate a simple game of BlackJack,
#   by dealing cards to both the Player and the Dealer, evaluating
#   each hand (summing the values of the cards), and checking when
#   the game is over (when someone scored a blackjack / both players
#   busted / etc.)
#

from cards import Card, Deck, Hand

#
# BlackJack Class
#

class BlackjackHand(Hand):
    
    ''' Initiates a Hand of BlacJack with no cards, but having a label. '''
    def __init__(self, label = ''):
        self.cards = []
        self.label = label

    ''' Compares to Hands of BlackJack, by checking the total sum of each
    each ones cards. '''
    def __cmp__(self, other):
        if self.total() > other.total():
            return 1
        elif self.total() < other.total():
            return -1
        else:
            return 0

    ''' Returns the Label of the Hand. '''
    def getLabel(self):
        return self.label

    ''' Computes the total value of the cards containing by the Hand. '''
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

    ''' Checks if the current value of the Hand is considered to be a Bust. '''
    def isaBust(self):
        if self.total() > 21:
            return True
        else:
            return False

    ''' Checks if the current value of the Hand is considered to be a
    BlackJack. '''
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

def blackjackGame(player_name):
    deck = Deck()
    deck.shuffle()

    player = BlackjackHand(player_name)
    dealer = BlackjackHand('Dealer')
    
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
        choice = raw_input(out)
        while choice != '1' and choice != '0':
                out = player.getLabel() + ", type 1 for a hit and 0 to stay >> "
                choice = raw_input(out)
        choice = int(choice)

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
                choice = raw_input(out)
                while choice != '1' and choice != '0':
                    choice = raw_input(out)
                choice = int(choice)
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
            key = raw_input()
            while dealer.total() < 17:
                print dealer.getLabel(), " takes a hit. "
                deck.deal(dealer, 1)
                status(dealer)
                key = raw_input()
        print
        print player.getLabel(), " total is ", player.total(), " and ", \
              dealer.getLabel(), " total is ", dealer.total(), ". "
        if dealer.isaBust():
            print dealer.getLabel(), " went bust and loses the hand."
        print
        print player.getLabel(), "'s turn. Type any key to continue. "
        key = raw_input()
        if player.isaBust() == True and dealer.isaBust() == True:
            out = player.getLabel() + ", press any key to continue. "
        elif player.isaBlackjack() == False and player.isaBust() == False:
            out = player.getLabel() + ", type 1 for a hit and 0 to stay >> "
            choice = raw_input(out)
            while choice != '1' and choice != '0':
                out = player.getLabel() + ", type 1 for a hit and 0 to stay >> "
                choice = raw_input(out)
            choice = int(choice)
                

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
    

print "\t\t\t BlackJack Simulator"
print "\t\t\t *******************"

player_name = raw_input(" Please enter your name: ")

play_again = 1
while play_again == 1:
    blackjackGame(player_name)
    print
    play_again = raw_input(" Press 1 for playing another round, or 0 to exit the game >> ")
    while play_again != '1' and play_again != '0':
        play_again = raw_input(" Press 1 for playing another round, or 0 to exit the game >> ")
    play_again = int(play_again)
    if play_again == 1:
        ch_name = raw_input(" Press 1 to change the name or 0 to keep the same name >> ")
        while ch_name != '1' and ch_name != '0':
            ch_name = raw_input(" Press 1 to change the name or 0 to keep the same name >> ")
        ch_name = int(ch_name)
        if ch_name == 1:
            player_name = raw_input(" Please enter your name: ")
    
                        
