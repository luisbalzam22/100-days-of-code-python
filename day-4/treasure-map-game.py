import random

WELCOME_MESSAGE = "Welcome to the 'Treasure Map' game"
COORDINATES_PROMPT_MSG = "Please, introduce the x and y coordinates of where you think the treasure is (Use the format xy.E.g.: 12 for col = 1 and row = 2):\n"
WIN_MESSAGE = "Congratulations, you just won!"
LOSE_MESSAGE = "Sorry, try again"

map_tiles = [
    ['O','O','O'],
    ['O','O','O'],
    ['O','O','O']
]

random_x_position = random.randint(0,len(map_tiles) -1)
random_y_position = random.randint(0,len(map_tiles) -1)

print(WELCOME_MESSAGE)
coordinates = input(COORDINATES_PROMPT_MSG)

selected_x_position = int(coordinates[1]) -1
selected_y_position = int(coordinates[0]) -1

map_tiles[random_x_position][random_y_position] = '$'
if selected_x_position == random_x_position and selected_y_position == random_y_position:
    print(WIN_MESSAGE)
else:
    map_tiles[selected_x_position][selected_y_position] = 'X'
    print(LOSE_MESSAGE)
print(f"{map_tiles[0]}\n{map_tiles[1]}\n{map_tiles[2]}")
