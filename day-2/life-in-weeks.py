WELCOME_MESSAGE = "Welcome to the age calculator (your life in weeks)"
AGE_PROMPT_MSG = "Please, enter your age\n"
TOTAL_EXPECTED_YEARS = 90

age = int(input(AGE_PROMPT_MSG))

# month 12
# 52
# 365

# days left
years_left = TOTAL_EXPECTED_YEARS - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")
