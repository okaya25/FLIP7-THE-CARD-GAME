from playerside import Player
from deck import get_deck,draw_card

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
        currentname = current_player.get_name()
        cardss = current_player.get_cards()
        print(f"Secondchance: {current_player.has_second_chance()}, extras are: {current_player.get_extras()}")
        hit_or_stay = ""
        while hit_or_stay != "h" and hit_or_stay != "s":
            hit_or_stay = input(f"{currentname}, your cards are {cardss}, h for hit, s for stay: ")    
        if hit_or_stay == "s":
            current_player.stayed()
            print("\n")
        else:
            x = draw_card(deck,deck2,current_players, current_player,players,current_player_id)
            if x == "roundbreak":
                break
        
def roundover(Players):
    print("round is over, here are the scores")
    for player in Players:
        player.round_score()
        player.update_score()
        name = player.get_name()
        score = player.get_score()
        print(f"{name}: {score}")

def anywinners(players):
    scores = []
    for player in players:
        scores.append((player.get_score(),player.get_name()))
    scores.sort(key = lambda x: (x[0]),reverse = True)
    if scores[0][0] >= 200:
        return scores[0][1]
    else:
        return ""
            
def MainGame(amount_of_players):
    Players = []
    for x in range(amount_of_players):
        Players.append(Player(input("Your name: ")))
    NoWinner = True
    Deck = get_deck()
    Deck2 = []
    while NoWinner:
        oneround(Players,Deck,Deck2)
        Players = Players[1:] + [Players[0]]
        Winner = anywinners(Players)
        if Winner != "":
            print("Game is over")
            print(f"Winner is {Winner}")
            NoWinner = False

def target(card,players,deck,deck2,Players):
    targeted = ""
    while targeted not in players:
        targeted = input("name of target")
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

if __name__ == "__main__":
    MainGame(2)
    