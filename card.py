from random import shuffle


class Mana:
    '''Respresents a quantity of mana.'''
    
    def __init__(self, amount):
        self._amount = amount
        
    def __leq__(self, other):
        return self._amount <= other._amount
        
    def __add__(self, other):
        return Mana(self._amount + other._amount)
        
    def __radd__(self, other):
        return self + Mana(other)
        
    def __sub__(self, other):
        return self + Mana(-other.amount)
        
    def __str__(self):
        return str(self._amount)

class Card:
    '''Represents land and creature cards.'''

    def __init__(self, symbol, name, cost=0, power=0):
        self.symbol = symbol
        self.name = name
        self.cost = cost
        self.power = power
        self.tapped = False
        
class LandCard(Card):
    '''Subclass of cards for Lands.'''
    
    def tap_for_mana(self):
        '''Tap land to generate Mana.''' 
        if not self.tapped:
            self.tapped = True
            return Mana(1)
        else:
            print("This card has already been tapped!")
            return Mana(0)

def make_deck():
    '''Creates and returns a shuffled deck of Cards.'''
    deck = []
    for _ in range(20):
        deck.append(LandCard('l', "Land"))
    for _ in range(6):
        deck.append(Card('2', "Bear"))
    for _ in range(6):
        deck.append(Card('3', "Knight"))
    for _ in range(4):
        deck.append(Card('4', "Elemental"))
    for _ in range(2):
        deck.append(Card('5', "Vampire"))
    deck.append(Card('6', "Dragon"))
    shuffle(deck)
    return deck
