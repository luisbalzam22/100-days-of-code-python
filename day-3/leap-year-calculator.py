from turtle import goto


WELCOME_MESSAGE = "Welcome to the Leap Year Calculator"
YEAR_PROMPT_MSG = "Please, introduce a valid year\n"

year = int(input(YEAR_PROMPT_MSG))

is_leap_year = False

if year % 4 == 0:
    is_leap_year = True
    if year % 100 == 0:
        is_leap_year = False
        if year % 400 == 0:
            is_leap_year = True
            
if is_leap_year:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")