INTRO_ASCII_ART = """
       _         ||
      |-|   m1a  ||
  ____| |____    ||
 /   _| |_   \   //
|  / ,| |. \  |_//
| ( ( '-' ) ) |-'
|  \ `'"'' /  |
|   `-----'   ;
|\___________/|
|             ;
 \___________/
\n"""

WELCOME_MESSAGE = INTRO_ASCII_ART + "Welcome to the Treasure Island Game, let's start our journey"
LEFT_OR_RIGHT_PROMPT_MSG = "Wanna go left, or right? (type 'left' or 'right')\n"
SWIM_OR_WAIT_PROMPT_MSG = "Wanna go swim, or wait? (type 'swim' or 'wait')\n"
DOOR_SELECT_PROMPT_MSG = "Wanna go through the red, blue, or yellow door? (type 'red', 'blue' or 'yellow' to select)\n"
GAME_OVER_MSG = "Game Over"

print(WELCOME_MESSAGE)
# left_or_right = input(LEFT_OR_RIGHT_PROMPT_MSG).lower()

# if left_or_right == 'left':
#     swim_or_wait = input(SWIM_OR_WAIT_PROMPT_MSG).lower()
#     if swim_or_wait == 'wait':
#         selected_door = input(DOOR_SELECT_PROMPT_MSG).lower()
#         if (selected_door == 'yellow'):
#             end_game_msg = 'You win'
#         else:
#             end_game_msg = GAME_OVER_MSG
#     else:
#         end_game_msg = GAME_OVER_MSG
# else:
#     end_game_msg = GAME_OVER_MSG

# print(end_game_msg)

#Optional (not-nested implementation suggestion)
def make_decision(input_msg, success_value):
    if input(input_msg).lower() == success_value:
        return True
    return False


player_alive = True

decisions_to_take = [
    [LEFT_OR_RIGHT_PROMPT_MSG, 'left'], 
    [SWIM_OR_WAIT_PROMPT_MSG, 'wait']
]
current_decision_index = 0
while player_alive and current_decision_index != len(decisions_to_take):
    player_alive = make_decision(decisions_to_take[current_decision_index][0], decisions_to_take[current_decision_index][1])
    if player_alive:
        current_decision_index+=1
    
if current_decision_index == len(decisions_to_take):
    print('You survived')
else:
    print("Game over")