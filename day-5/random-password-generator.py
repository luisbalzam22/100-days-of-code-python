from random import randint, shuffle

WELCOME_MESSAGE = "Welcome to the PyPassword Generator!"
LETTERS_PROMPT_MSG = "How many letters would you like in your password?\n"
SYMBOLS_PROMPT_SMG = "How many symbols would you like?\n"
NUMBERS_PROMPT_MSG = "How many numbers would you like?\n"
ALLOWED_SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(WELCOME_MESSAGE)
number_of_letters= int(input(LETTERS_PROMPT_MSG)) 
number_of_symbols = int(input(SYMBOLS_PROMPT_SMG))
number_of_numbers = int(input(NUMBERS_PROMPT_MSG))

password_array = []

for letter in range(1, number_of_letters + 1):
    random_char = chr(randint(65,90))
    if randint(0,1) == 1:
        random_char = random_char.lower()
    password_array.append(random_char)

for symbol in range(1, number_of_symbols + 1):
    password_array.append(ALLOWED_SYMBOLS[randint(0, len(ALLOWED_SYMBOLS) - 1)])

for number in range(1, number_of_numbers + 1):
    password_array.append(str(randint(0,9)))
    
shuffle(password_array)

# If want to avoid shuffle():
# for character in range (1, len(password_array) * 2): 
#     password_array.insert(randint(0, len(password_array) -1), password_array.pop())
    
print(f"The final Password is: {''.join(password_array)}")
    

