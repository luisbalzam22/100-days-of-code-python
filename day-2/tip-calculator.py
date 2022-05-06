from traceback import print_list
from typing import final


WELCOME_MESSAGE = "Welcome to the tip calculator"
TOTAL_BILL_PROMPT_MSG = "Please, introduce the total bill\n"
TIP_PERCENTAGE_PROMPT_MSG = "Please, introduce the tip percentage you want to offer\n"
PEOPLE_TO_SPLIT_MSG = "Please, introduce the amount of people the bill will be split into\n"

print(WELCOME_MESSAGE)

total_bill = float(input(TOTAL_BILL_PROMPT_MSG))
tip_percentage = float(input(TIP_PERCENTAGE_PROMPT_MSG)) / 100
people_to_split = int(input(PEOPLE_TO_SPLIT_MSG))

final_calculation = (total_bill + (total_bill * tip_percentage)) / people_to_split

print(f'Each person should pay: ${"{:.2f}".format(final_calculation)}')
