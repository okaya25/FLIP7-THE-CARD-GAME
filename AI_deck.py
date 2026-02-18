import random

def get_deck():
    deck = [ "flip3", "flip3", "flip3",
             "secondchance", "secondchance", "secondchance",
             "freeze", "freeze", "freeze", 
             "+2","+4","+6","+8","+10","x2","0"]
    for n in range(1,13):
        deck += [str(n)] * n
    random.shuffle(deck)
    return deck
    
def draw_card(deck,deck2,players,current_player,Players,ids = 0):
    from AI_gameside import target,roundover
    if players == []:
        roundover(Players)
        return "roundbreak"
    if not current_player.is_inround():
        if current_player in players:
            players.pop(ids)
        return "None"
    if deck == []:
       random.shuffle(deck2)
       deck = deck2[::]
       deck2 = []
    card = deck.pop(0)
    deck2.append(card)
    targeter = ["flip3","freeze","secondchance"]
    if card in targeter:
        if card == "secondchance" and not current_player.has_second_chance():
            current_player.got_secondchance()
        else:
            target(card,players,deck,deck2,Players,current_player)
    else:
        is_flip7 = current_player.update_cards(card)
        if is_flip7:
            current_player.flip7ed()
            roundover(Players)
            return "roundbreak"
        

