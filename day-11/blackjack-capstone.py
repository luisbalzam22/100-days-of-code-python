from random import choice

labeled_cards = {"A": 11, "J":10, "Q": 10, "K": 10 }
game_over = False
dealer_status = {
    "entity_type": "DEALER",
    "card_count": 0,
    "shown_cards": [],
    "status": "PLAYING",
    "stay": False
}
player_status = {
    "entity_type": "PLAYER 1",
    "card_count": 0,
    "shown_cards": [],
    "status": "PLAYING",
    "stay": False
}
entities_playing = [player_status, dealer_status]
lead = { "top_score": 0, "players": []}
WELCOME_MSG = "Welcome to the BlackJack Capstone Game!"
CHECK_PROMPT_MSG = "Do you want to check, or stay? (c/s)\n"
CONSTANTS = {"MIN_CARD_RANGE": 2, "MAX_CARD_RANGE": 10}

def get_random_top_card():
    deck_keys = [item for item in labeled_cards] + [num for num in range(CONSTANTS["MIN_CARD_RANGE"],CONSTANTS["MAX_CARD_RANGE"] + 1)]
    picked = choice(deck_keys)
    if picked in labeled_cards:
        return (picked, labeled_cards[picked])
    return (str(picked), picked)

def draw(entity):
    picked_card = get_random_top_card()
    return {
        "entity_type": entity["entity_type"],
        "shown_cards": entity["shown_cards"] + [picked_card[0]],
        "card_count": entity["card_count"] + picked_card[1],
        "status": entity["status"],
        "stay": False
    }

def turn(entity):
    will_draw = False
    if entity["status"] == "PLAYING" and (not entity["stay"]):
        if entity["entity_type"] == "DEALER":
            will_draw = entity["card_count"] < 17
        else:
            will_draw = input(CHECK_PROMPT_MSG).lower() == 'c'
        if (will_draw):
            return draw(entity)
        else:
            changed_stay = entity.copy()
            changed_stay["stay"] = True
            return changed_stay
    return entity

def check_if_looses(entity):
    temporal_entity = entity.copy()
    
    if 'A' in entity["shown_cards"]:
        temporal_entity["card_count"] -= 10
        temporal_entity["shown_cards"][temporal_entity["shown_cards"].index('A')] = 'A(1)'

    if temporal_entity["card_count"] > 21:
        temporal_entity["status"] = "GAMEOVER"
        
    return temporal_entity

# TODO: separate this into 2 functions
def update_game_status(entities, lead):
    for index in range(0, len(entities)):
        if entities[index]["card_count"] <= 21 and entities[index]["status"] == "PLAYING":
            if entities[index]["card_count"] >= lead["top_score"]:
                lead["top_score"] = entities[index]["card_count"]
                if not entities[index]["entity_type"] in lead["players"]:
                    lead["players"].append(entities[index]["entity_type"])

        elif entities[index]["card_count"] > 21 and entities[index]["status"] == "PLAYING":
            entities[index] = check_if_looses(entities[index])
    
    for index in range(0, len(entities)):      
        if entities[index]["entity_type"] in lead["players"] and entities[index]["card_count"] < lead["top_score"]:
            # TODO: change this line below for lead["players"].remove(entities[index]["entity_type"]) -->then test
            lead["players"].pop(lead["players"].index(entities[index]["entity_type"]))
    
    
def game_should_stop(entities):
    entities_still_playing = [item for item in entities if item["status"] == "PLAYING"]
    stay_count = 0
    for entity in entities_still_playing:
        if entity["stay"]:
            stay_count +=1
    return stay_count == len(entities_still_playing)
    
    
def initial_draws(entities):
    def map_items(item):
        mew_item = draw(item)
        return draw(mew_item)
    
    return list(map(map_items, entities))
        
def print_players_status(entitites):
    for entity in entitites:
        print(f"{entity['entity_type']} Cards: {entity['shown_cards']}. Total Score: {entity['card_count']}")
        
def drawing_turns(entities):
    for index in range(0, len(entities)):
        entities[index] = turn(entities[index])
        
    
print(WELCOME_MSG)

# initial draws
entities_playing = initial_draws(entities_playing)
   
while(not game_over):
    # show cards and current scores
    print_players_status(entities_playing)
    
    # taking turns in checking/passing
    drawing_turns(entities_playing)
    update_game_status(entities_playing, lead)
    
    # evaluate if game should end
    game_over = game_should_stop(entities_playing)

# declare_winner(s) ->lead(s)
print(f"The winners are: {lead['players']}\n{entities_playing}")