# Name: Frank Shang
# Date: 3/15/2022

import random

class Card():
    def __init__(self, value, suite):
        self._value = value
        self._suite = suite

    def get_value(self):
        return self._value

    def get_suite(self):
        return self._suite

class Deck():

    def __init__(self):
        self._spades = {}
        self._hearts = {}
        self._diamonds = {}
        self._clubs = {}
        self._full_deck = [self._spades, self._hearts, self._diamonds, self._clubs]
        self._numCards = 0
        self.makeNewDeck()
    
    def add_card(self, card):
        if card.get_suite() == "spades":
            self._spades[card.get_value()] = card.get_suite()
        elif card.get_suite() == "hearts":
            self._hearts[card.get_value()] = card.get_suite()
        elif card.get_suite() == "diamonds":
            self._diamonds[card.get_value()] = card.get_suite()
        else:
            self._clubs[card.get_value()] = card.get_suite()
        self._numCards += 1

    def display_deck(self):
        print("Here are the cards in the deck.")
        for element in self._full_deck:
            for key in element:
                print(key, "of", element[key] + ".")

    def getNumCards(self):
        return self._numCards

    def makeNewDeck(self):
        # create the cards
        spades = []
        #spades
        for i in range(1, 14):
            if i == 1:
                spades.append(Card("Ace", "spades"))
            elif i == 11:
                spades.append(Card("Jack", "spades"))
            elif i == 12:
                spades.append(Card("Queen", "spades"))
            elif i == 13:
                spades.append(Card("King", "spades"))
            else:
                spades.append(Card(str(i), "spades"))
        hearts = []
        #hearts
        for i in range(1, 14):
            if i == 1:
                hearts.append(Card("Ace", "hearts"))
            elif i == 11:
                hearts.append(Card("Jack", "hearts"))
            elif i == 12:
                hearts.append(Card("Queen", "hearts"))
            elif i == 13:
                hearts.append(Card("King", "hearts"))
            else:
                hearts.append(Card(str(i), "hearts"))

        diamonds = []
        #diamonds
        for i in range(1, 14):
            if i == 1:
                diamonds.append(Card("Ace", "diamonds"))
            elif i == 11:
                diamonds.append(Card("Jack", "diamonds"))
            elif i == 12:
                diamonds.append(Card("Queen", "diamonds"))
            elif i == 13:
                diamonds.append(Card("King", "diamonds"))
            else:
                diamonds.append(Card(str(i), "diamonds"))
        
        clubs = []
        #clubs
        for i in range(1, 14):
            if i == 1:
                clubs.append(Card("Ace", "clubs"))
            elif i == 11:
                clubs.append(Card("Jack", "clubs"))
            elif i == 12:
                clubs.append(Card("Queen", "clubs"))
            elif i == 13:
                clubs.append(Card("King", "clubs"))
            else:
                clubs.append(Card(str(i), "clubs"))

            # Create deck
        for card in spades:
            self.add_card(card)

        for card in hearts:
            self.add_card(card)

        for card in diamonds:
            self.add_card(card)
    
        for card in clubs:
            self.add_card(card)

class Dealer():

    def __init__(self):
        pass

class Player():

    def __init__(self, total = 1000):
        self._total = total
        self._small_blind = False
        self._big_blind = False


def main():

    deck = Deck()
    deck.display_deck()
    print(deck.getNumCards())

# main running as script
if __name__ == "main":
    main()

