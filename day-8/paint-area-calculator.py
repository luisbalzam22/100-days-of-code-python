from math import ceil

GREETING_MESSAGE = "Welcome to the Paint Area Calculator"
GET_HEIGHT_PROMPT_MSG = 'Please, enter the height\n'
GET_WIDTH_PROMPT_MSG = 'Please, enter the widh\n'
COVERABLE_PAINT_CAN_AREA = 5 # Square meters

def calculate_needed_cans(wall_heigth, wall_width):
    return ceil(wall_heigth * wall_width / COVERABLE_PAINT_CAN_AREA)

heigth = float(input(GET_HEIGHT_PROMPT_MSG))
width = float(input(GET_WIDTH_PROMPT_MSG))

print(GREETING_MESSAGE)
print(f"You need {calculate_needed_cans(heigth, width)} cans to paint a {heigth}x{width}m wall")