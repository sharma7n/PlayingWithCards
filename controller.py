class Controller:
    '''Responsible for transforming player decisions into game instructions.
    Abstract class, subclassed by HumanController and AIController.'''
       
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def _start_turn(self):
        '''Setup actions for a single turn.'''
        self.player.playedland = False
        self.player.update_mana()
        self.player.draw()
        self._can_act = True
    
    def _end_turn(self):
        '''Teardown actions for a single turn.'''
        print("End of {}'s Turn.\n {}'s Turn".format(self.player.name, self.opponent.name))
    
    def _land(self):
        '''Plays a land from the player's hand.'''
        self.player.play_land()

    def _summon(self):
        '''Summons a card from the player's hand.
        Requires interface for a human, and AI for a computer.'''
        raise NotImplementedError()
        
    def _attack(self):
        '''Selects a set of attacking cards.
        Requires interface for a human, and AI for a computer.'''
        raise NotImplementedError()
        
    def _try_attack(self):
        '''Attacks if the player has attackers.'''
        if self.player.field:
            self._attack()
            self._can_act = False
        else:
            print(self.player.name + " does not have any attackers available.")
        
    def _block(self):
        '''Selects a set of blocking cards.
        Requires interface for a human, and AI for a computer.'''
        raise NotImplementedError()
        
    def _try_block(self):
        '''Blocks if the player has blockers available.'''
        if self.player.field:
            self._block()
        else:
            print(self.player.name + " does not have any blockers available.")

    def _done(self):
        '''Flags the player's turn as done.'''
        self.player.blockers = list(self.player.field)
        self._can_act = False
        
    def _prompt(self):
        '''Asks player for next action. 
        Requires interface for a human, and AI for a computer.'''
        raise NotImplementedError()
        
    def play(self):
        self._start_turn()
        while self._can_act:
            self._prompt()
        self._end_turn()
        
class HumanController(Controller):
    '''Controller for human players.'''
    
    def _summon(self):
        print("Monsters: {}".format(self.player.monsters))
        monster = input("Which monster would you like to summon?\n")
        self.player.summon(monster)
    
    def _attack(self):
        print(self.player.name + "'s field: {}".format(self.player.field))
        print(self.opponent.name + "'s field: {}".format(self.opponent.field))
        attackers = input("Which creatures would you like to attack with? (Separate by spaces)\n").split(' ')
        self.player.attack(attackers, self.opponent)
    
    def _block(self):
        print(self.player.name + "'s field: {}".format(self.player.field))
        blockers = input("Which creatures would you like to block with? (Space separated list of indices)\n").split(' ')
        self.player.block(blockers, self.opponent)
    
    def _prompt(self):
        print("Mana: {}".format(self.player.mana))
        choice = input("It's your turn. What will you do? \n LAND SUMMON ATTACK DONE\n").upper()
        if choice == "LAND":
            self._land()
        elif choice == "SUMMON":
            self._summon()
        elif choice == "ATTACK":
            self._attack()
        elif choice == "DONE":
            self._done()
        elif choice == "QUIT":
            exit()
        else:
            print("That's not even a thing")
            
class AIController(Controller):
    '''Controller for AI players.'''
    
    def _summon(self):
        self.player.summon(self.player.monsters[0])
        
    def _attack(self):
        self.player.attack(self.player.field, self.opponent)
        
    def _block(self):
        self.player.block(self.player.field, self.opponent)
        
    def _prompt(self):
        self._machine_learning_decision()
        if not self.player.playedland:
            self._land()
        elif self.player.mana >= sum(int(card) for card in self.player.hand if card != 'l') and len(self.player.hand) > 0:
            self._summon()
        else:
            self._attack()
            
    def _machine_learning_decision(self):
        pass
            
def controller_factory(n, player, opponent, handler_type):
    '''Creates a HumanController or AIController based on user input.'''
    valid_input = False
    if handler_type == 'HUMAN' or handler_type == 'H':
        valid_input = True
        return HumanController(player, opponent)
        
    if handler_type == 'AI' or handler_type == 'A':
        valid_input = True
        return AIController(player, opponent)
