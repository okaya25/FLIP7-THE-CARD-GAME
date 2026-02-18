from playerside import Player

class AI(Player):
    def hit_stay(self,deck):
        if self.has_second_chance() or len(self.get_cards()) == 6:
            return "h"
        else:
            n = 0
            for card in self.get_cards():
                n += deck.count(str(card))
            if self.get_name()[0] == "%": 
                if n * 100 / len(deck) <= int(self.get_name()[1:]):
                    return "h"
                else:
                    return "s"
            else:
                if sum(self.get_cards()) <= int(self.get_name()):
                    return "h"
                else:
                    return "s"
                
    def targete(self,players,card):
        if len(players) == 1:
            return players[0].get_name()     
        if "flip3" == card and len(self.get_cards()) <= 2:
            return self.get_name()
        datas = []
        for player in players:
            if player == self:
                continue
            if player.has_second_chance():
                life = 1
            else:
                life = 0
            data = (player.get_name(),life,player.get_score())
            datas.append(data)
        datas.sort(key = lambda x: (x[2]),reverse = True)
        match card:
            case "freeze":
                return datas[0][0]
            case "flip3":
                for player in datas:
                    if not player[1]:
                        return player[0]
            case "secondchance":
                return datas[-1][0]
