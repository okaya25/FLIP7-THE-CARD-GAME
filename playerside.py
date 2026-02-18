class Player(object):
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.extras = []
        self.score = 0
        self.roundscore = 0
        self.inround = True
        self.secondchance = False
    
    def get_cards(self):
        return self.cards
    
    def get_score(self):
        return self.score
    
    def get_extras(self):
        return self.extras
    
    def update_cards(self,card):
        effects = ["+2","+4","+6","+8","+10","x2"]
        if card in effects:
            self.extras.append(card)
        else:
            if int(card) in self.cards:
                if not self.has_second_chance():
                    self.inround = False
                    self.cards = []
                    self.extras = []
                else:
                    self.secondchance = False
            else:
                self.cards.append(int(card))
        return len(self.cards) == 7

    def update_score(self):
        self.score += self.roundscore
        self.cards = []
        self.extras = []
        self.roundscore = 0
        self.inround = True
    
    def stayed(self):
        self.inround = False
    
    def is_inround(self):
        return self.inround
    
    def round_score(self):
        tempscore = sum(self.cards)
        if "x2" in self.extras:
            tempscore *= 2
            self.extras.remove("x2")
        for plus in self.extras:
            tempscore += int(plus[1:])
        self.roundscore = tempscore

    def get_name(self):
        return self.name
    
    def flip7ed(self):
        self.score += 15
    
    def got_secondchance(self):
        self.secondchance = True
    
    def has_second_chance(self):
        return self.secondchance
    