from AI_player import AI
from AI_deck import get_deck,draw_card
import random

def oneround(players,deck,deck2):
    current_players = players[::]
    for n in range(100000):
        if len(current_players) == 0:
            roundover(players)
            break
        current_player_id = n % len(players)
        current_player = players[current_player_id]
        if current_player in current_players:
            current_player_id = current_players.index(current_player)
        if not current_player.is_inround():
            if current_player in current_players:
                current_players.pop(current_player_id)
            continue
        if deck == []:
            random.shuffle(deck2)
            deck = deck2[::]
            deck2 = []
        hit_or_stay = current_player.hit_stay(deck)    
        if hit_or_stay == "s":
            current_player.stayed()
        else:
            x = draw_card(deck,deck2,current_players, current_player,players,current_player_id)
            if x == "roundbreak":
                break
        
def roundover(Players):
    for player in Players:
        player.round_score()
        player.update_score()


def anywinners(players):
    scores = []
    for player in players:
        scores.append((player.get_score(),player.get_name()))
    scores.sort(key = lambda x: (x[0]),reverse = True)
    if scores[0][0] >= 200:
        return scores[0][1]
    else:
        return ""
            
def MainGame(AI_Names):
    AIs = []
    for name in AI_Names:
        AIs.append(AI(name))
    NoWinner = True
    Deck = get_deck()
    Deck2 = []
    while NoWinner:
        oneround(AIs,Deck,Deck2)
        AIs = AIs[1:] + [AIs[0]]
        Winner = anywinners(AIs)
        if Winner != "":
            return Winner
            NoWinner = False

def target(card,players,deck,deck2,Players,current_player):
    if players == []:
        pass
    targeted = current_player.targete(players,card)
    match card:
        case "freeze":
            for player in players:
                if targeted == player.get_name():
                    player.stayed()
        case "secondchance":
            for player in players:
                if targeted == player.get_name():
                    player.got_secondchance()
        case "flip3":
            for player in players:
                if targeted == player.get_name():
                    for n in range(3):
                        draw_card(deck,deck2, players, player,Players)

def testers(n,gamers):
    dic = {}
    for gamer in gamers:
        dic[gamer] = 0
    for x in range(n):
        Win = MainGame(gamers[::])
        dic[Win] += 1
    return dic
    
if __name__ == "__main__":
    gamers = ["%20","%25","%30","20","25","30"]
    print(testers(10000,gamers))
    