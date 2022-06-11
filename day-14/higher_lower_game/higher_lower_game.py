import os
clear = lambda: os.system('clear')
import random
from game_data import data
from constants import ASCII_LOGO, GET_ANSWER_PROMPT_MSG, REPEAT_GET_ANSWER_MSG, VS_LOGO

def format_entity_info(entity):
    return f"{entity['name']}, a {entity['description']} from {entity['country']}."

def get_versus(original_versus, game_data):
    # in case it's 1st time
    if not len(original_versus):
        return {
            "A": random.choice(game_data),
            "B": random.choice(game_data) 
        }

    bigger_star = get_bigger_star(original_versus)
    b = random.choice(game_data)
    
    while b in [original_versus[item] for item in original_versus]:
        b = random.choice(game_data)

    return {
        "A": bigger_star,
        "B": b
    }

def display_versus(versus):
    print(
        f"Compare \"A\": {format_entity_info(versus['A'])}"
        f"{VS_LOGO}\n"
        f"Against \"B\": {format_entity_info(versus['B'])}"
        )
    
def display_game_status(entity):
    if (entity["alive"]):
        print(f"You're right! Current score: {entity['score']}")
    else:
        print(f"Sorry, that's wrong. Final score: {entity['score']}")

def calculate_player_stats(player, versus):
    new_player_stats = player.copy()
    bigger_star = get_bigger_star(versus)

    if versus[new_player_stats["current_answer"]] != bigger_star:
        new_player_stats["alive"] = False
    else:
        new_player_stats["score"] +=1
        
    return new_player_stats
    
def get_bigger_star(versus):
    if versus["A"]["follower_count"] > versus["B"]["follower_count"]:
        return versus["A"]
    return versus["B"]

def get_answer(msg):
    answer = input(msg).upper()
    while(answer != 'A' and answer != 'B'):
        print(REPEAT_GET_ANSWER_MSG)
        answer = input(msg).upper()
    return answer

player = {
    "score": 0,
    "alive": True,
    "current_answer": None 
}
versus_entities = {}
while (player["alive"]):
    clear()
    print(ASCII_LOGO)
    if (player["current_answer"]):
        display_game_status(player)

    versus_entities = get_versus(versus_entities, data)
    display_versus(versus_entities)
    
    player["current_answer"] = get_answer(GET_ANSWER_PROMPT_MSG)
    player = calculate_player_stats(player, versus_entities)
clear()
print(ASCII_LOGO)
display_game_status(player)