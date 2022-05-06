WELCOME_MESSAGE = "Welcome to the BMI calculator"
WEIGHT_PROMPT_MSG = "Please, introduce your weigth in Kilograms\n"
HEIGHT_PROMPT_MSG = "Please, introduce your heigth in Meters\n"

print(WELCOME_MESSAGE)
weight = float(input(WEIGHT_PROMPT_MSG))
height = float(input(HEIGHT_PROMPT_MSG))

print(f"Your current BMI is: {int(weight / (height**2))}")
