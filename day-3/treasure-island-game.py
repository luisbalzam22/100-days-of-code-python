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
left_or_right = input(LEFT_OR_RIGHT_PROMPT_MSG).lower()

if left_or_right == 'left':
    swim_or_wait = input(SWIM_OR_WAIT_PROMPT_MSG).lower()
    if swim_or_wait == 'wait':
        selected_door = input(DOOR_SELECT_PROMPT_MSG).lower()
        if (selected_door == 'yellow'):
            end_game_msg = 'You win'
        else:
            end_game_msg = GAME_OVER_MSG
    else:
        end_game_msg = GAME_OVER_MSG
else:
    end_game_msg = GAME_OVER_MSG

print(end_game_msg)