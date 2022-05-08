import random

WELCOME_MESSAGE = "Welcome to the 'Rock-Paper-Scissors' game"
WIN_MESSAGE = "Congratulations, you win!"
TIE_MESSAGE = "It's a tie!"
INVALID_PICK_MESSAGE = "You introduced an invalid pick"
LOOSE_MESSAGE = "Sorry, you loose"

PIXEL_ART_LIST = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
, 
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

HAND_PROMPT_MSG = "Please, type 0 for Rock, 1 for Paper, and 2 for Scissors\n"


cpu_pick = random.randint(0, 2)


print(WELCOME_MESSAGE)
hand_pick = int(input(HAND_PROMPT_MSG))


if hand_pick >= 0 and hand_pick < 3:
    if (hand_pick == 0 and cpu_pick == 2) or (hand_pick == 1 and cpu_pick == 0) or (hand_pick == 2 and cpu_pick == 1):
        game_status_msg = WIN_MESSAGE
    elif hand_pick == cpu_pick:
        game_status_msg = TIE_MESSAGE
    else:
        game_status_msg = LOOSE_MESSAGE
else:
    game_status_msg = INVALID_PICK_MESSAGE

print(game_status_msg)
if game_status_msg != INVALID_PICK_MESSAGE:
    print(f"You picked:\n{PIXEL_ART_LIST[hand_pick]}\nCPU picked:\n{PIXEL_ART_LIST[cpu_pick]}")
