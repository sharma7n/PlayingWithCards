from card import Mana, make_deck


class Player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.mana = Mana(0)
        self.hand = []
        self.field = []
        self.blockers = []
        self.lands = []
        self.dpile = []
        self.deck = make_deck()
        self.playedland = False
        for _ in range(7):
            self.draw()

    def update_mana(self):
        for land in self.lands:
            self.mana += land.tap_for_mana()

    def draw(self):
        card = self.deck.pop()
        self.hand.append(card)
            
    def play_land(self):
        '''If the player hasn't already played a land, plays a land.'''
        if not self.playedland:
            for card in self.hand:
                if hasattr(card, 'tap_for_mana'):
                    self.hand.remove(card)
                    self.lands.append(card)
                    self.playedland = True
                    print(self.name + " played a land.")
                    break
            else: # no break
                print(self.name + " has no lands to play!")
        else:
            print(self.name + " already played a land this turn!")
            
    def summon(self, card):
        '''Summons a card from the player's hand.'''
        if card in self.hand:
            if card.cost <= self.mana:
                self.mana -= card.cost
                self.hand.remove(card)
                self.field.append(card)
            else:
                print("Insufficient mana.")
        else:
            print(card + " not in hand.")
    
    def attack(self, cards, opponent):
        '''Attacks with the set of cards chosen by the player.'''
        pass
    
    def block(self, cards):
        '''Blocks with the set of cards chosen by the block.'''
        pass
