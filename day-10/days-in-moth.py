def is_leap_year(year):
    is_leap_year = False

    if year % 4 == 0:
        is_leap_year = True
        if year % 100 == 0:
            is_leap_year = False
            if year % 400 == 0:
                is_leap_year = True
    return is_leap_year

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month - 1 % 12]

WELCOME_MSG = "Welcome to the \"Days in Month\" program\nOnly use integers (negative numbers will be converted to positive)\n"
GET_YEAR_PROMPT_MSG = "Please, enter the year\n"
GET_MONTH_PROMPT_MSG = "Please, enter the month\n"

print(WELCOME_MSG)
inputted_year = abs(int(input(GET_YEAR_PROMPT_MSG)))
inputted_month = abs(int(input(GET_MONTH_PROMPT_MSG)))
print(f"Your month on {inputted_year} has {days_in_month(inputted_year, inputted_month)} days")